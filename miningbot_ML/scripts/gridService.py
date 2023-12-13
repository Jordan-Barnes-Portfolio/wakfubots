from ReadWriteMemory import ReadWriteMemory
import numpy
import struct
import pyautogui as pg
import time

class Grid:
    points = []
    center = (500, 400)

    def __init__(self, points, PID, center = center):
        self.PID = PID
        self.points = points
        self.center = center

    def addPoint(self, x, y):
        self.points.append([x, y])
    
    def getPoints(self):
        return self.points
        
   
    
    """
    Takes in the player state pointer and returns its current value as a 16b integer.
    
    !!! this needs to be refactored.
    
    Unable to reliably find the player animation ptr..
    """
    def readPlayerState(self, stPtr):
        rwm = ReadWriteMemory()
        process = rwm.get_process_by_id(self.PID)
        process.open()
        st_val = process.read(stPtr)

        process.close()
        
        return int(numpy.array(st_val).astype(numpy.int16))
    
    """
    Calculates the amount of cells to move from point a to b
    start is typically the coordinates of the user
    If the amount of cells calculated exceeds the click region,
    our secondary value is flipped to True (Out of bounds)
    
    THIS NEEDS TO BE CHECKED/REFACTORED.
    """
    def calculateMove(start, destination):
        OOB = False
        
        x1 = start[0]
        y1 = start[1]
        
        x2 = destination[0]
        y2 = destination[1]
        
        CTM = [(x2-x1), y2-y1]
        
        if(CTM[0] > 10):
            CTM[0] = 9
            OOB = True
        if(CTM[1] > 10):
            CTM[1] = 9
            OOB = True
            
        return CTM, OOB
    
    
    """
    These functions do exactly what they say, you begin at the starting point
    and move (cells) amount of squares in the direction you want !!EXCLUSIVE!!.
    
    # #Example of moving two cells left, then two cells up
    # left = move_mouse_left(2, center)
    # pg.moveTo(left)
    # up = move_mouse_up(2, left)
    # pg.moveTo(up)
    
    """
    def move_mouse_up(cells, start):
        while(cells>0):
            start = start[0]-51.42857142857143, start[1]-25
            cells-=1
        return(start)
    
    def move_mouse_down(cells, start):
        while(cells>0):
            start = start[0]+51.42857142857143, start[1]+25
            cells-=1
        return(start)
        
    def move_mouse_left(cells, start):
        while(cells>0):
            start = start[0]-51.42857142857143, start[1]+26.42857142857143
            cells-=1
        return(start)
        
    def move_mouse_right(cells, start):
        while(cells>0):
            start = start[0]+51.42857142857143, start[1]-24.42857142857143
            cells-=1
        return(start)
    
    
    
    def MoveX(self, pixels, CTM):
        if(CTM>0):
            pg.moveTo(Grid.move_mouse_down(CTM, pixels))
        else:
            pg.moveTo(Grid.move_mouse_up(abs(CTM), pixels))

    def MoveY(self, pixels, CTM):
        if(CTM>0):
            pg.moveTo(Grid.move_mouse_left(CTM), pixels)
        else:
            pg.moveTo(Grid.move_mouse_right(abs(CTM), pixels))

    
    def harvest_resource(self, start, POI):
        dest = calculateMove(start, POI)
        MoveX(self.center, POI[0])
        time.sleep(0.25)
        MoveY(pg.position(), POI[1])
    
    """
    THIS IS THE UP AND DOWN MATH...
    
    center = 500, 400
    dest = 140, 225
            
    dist = 360, 175
    amount of cells = 7
            
    distance x traveled: 51.42857142857143 per cell
    distance y traveled: 25 per cell
    
    THIS IS THE LEFT AND RIGHT MATH
    center = 500, 400
    dest =   140, 585
    
    dist = 360, -185
    amount of cells = 7
    
    dist x traveled = 51.42857142857143
    dist y traveled = -26.42857142857143
    """
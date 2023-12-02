from ReadWriteMemory import ReadWriteMemory
import numpy
import struct
class Grid:
    points = []

    def __init__(self, points, PID):
        self.PID = PID
        self.points = points

    def addPoint(self, x, y):
        self.points.append([x, y])
    
    def getPoints(self):
        return self.points
        
   
    
    """
    Takes in the player state pointer and returns its current value as a 16b integer.
    
    !!! this needs to be refactored.
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
    GridService movement algorithmn needs to be redone.
    """
    def down(pos, cells):
        if(cells!=1):
            cells = (cells*2)-1
        while(cells>=0):
            pos = pos[0]+36.14*0.58, pos[1]+19.28*0.58
            cells-=1
        return pos

    def right(pos, cells):
        if(cells!=1):
            cells = (cells*2)-1
        while(cells>=0):
            pos = pos[0]+36.14*0.58, pos[1]-19.28*0.58
            cells-=1
        return pos

    def left(pos, cells):
        if(cells!=1):
            cells = (cells*2)-1
        while(cells>=0):
            pos = pos[0]-37.14*0.58, pos[1]+19.28*0.58
            cells-=1
        return pos

    def up(pos, cells):
        if(cells!=1):
            cells = (cells*2)-1
        while(cells>=0):
            pos = pos[0]-34.14*0.62, pos[1]-15.28*0.64
            cells-=1
        return pos
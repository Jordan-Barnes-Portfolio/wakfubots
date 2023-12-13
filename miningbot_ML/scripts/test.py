from gridService import Grid
from player import Player
import utils
import pyautogui as pg
import time

# 00 00 00 00 00 00 60 C1 00 00 C0 41 0? 00 00 0? 00 00 00 00 15 00 00 00 00 00 00 00 ??
# print(scan_memory(process_id, start_address, end_address, search_pattern))

#Scratch paper

from datetime import datetime

# Get the current time
current_time = datetime.now()

# Format the time in military style
time_str = current_time.strftime("%H:%M")

print("Current time: ", time_str)

with open('C:/Users/Jordan/Desktop/Programming/GIT/wakfubots/miningbot_ML/scripts/data/locations.txt', 'r') as file:
    var=file.readlines()

# Example input string
input_string = var[0]

# Parse the input string
output = utils.parse_input(input_string)


"""

OKKKK.. testing the find minerals algorithm


First we need to CTM (Cells to move) (takes a starting input [x,y] and dest input [x,y])
then returns the amount of cells to move (x, y) to get to destination.

ASTRUB:
right is pos y
down is pos x
left is neg y
up is neg x

"""

def harvest_resource(start, POI):
    
    dest = Grid.calculateMove(start, POI)
    Grid.MoveX(self.center, POI[0])
    time.sleep(0.25)
    Grid.MoveY(pg.position(), POI[1])


current = [-83, -4]
print(output[0])

harvest_resource(current, output[0])

# center = (500, 400)

# start = [-81, -3]

# print(start)
# target = output[0]
# dest = Grid.calculateMove(start, target)
# print(dest)
# print(dest[0])

# def MoveX(pixels, CTM):
#     if(CTM>0):
#         pg.moveTo(Grid.move_mouse_down(CTM, pixels))
#     else:
#         pg.moveTo(Grid.move_mouse_up(abs(CTM), pixels))

# def MoveY(pixels, CTM):
#     if(CTM>0):
#         pg.moveTo(Grid.move_mouse_left(CTM), pixels)
#     else:
#         pg.moveTo(Grid.move_mouse_right(abs(CTM), pixels))





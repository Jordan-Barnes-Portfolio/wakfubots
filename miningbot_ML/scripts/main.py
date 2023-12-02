# -*- coding: utf-8 -*-
"""
@author: Jordan
"""

"""
Notes:

    3 cells on x axis up
    4 cells on y axis right
    
"""
import pyautogui as pg
import gridService as gs
import player
from utils import getPID, getWindow, setDimensions
import time
import os

class Main():
    def __init__(self):
        try:
            
            os.system('cls')
            
            print("Initializing...")
            time.sleep(0.25)
            
            #Sets static dimensions of our screen
            setDimensions("WAKFU")    
            
            #Gets gets our window dimensions.
            dim = getWindow("WAKFU")
            
            #Identifies the center of the screen
            center = (dim[2]/2, dim[3]/2)
            
            #Gets the PID of our game window
            PID = getPID("java")
            
            time.sleep(1)
            os.system('cls')
            
            #Pointers to our players position
            xPtr = input("Enter X coordinate memory address found in Cheat Engine.\nIf you do not know how to find this address, please see the README in your install folder.\n")
            
            xPtr = int(xPtr, 16)
            #PTR offset for y coordinate
            offset = 0x0004
            yPtr = xPtr + offset

            #OBJECTS
            Grid = gs.Grid(None, PID)
            Player = player.Player(None, None, PID)
            
            """ 
            HELPFUL COMMANDS:
            pl.position = pl.setPlayerCoords(xPtr, yPtr, pid) // sets our players position
            """
            
            print("Pid:", Player.PID)
            time.sleep(3)
            os.system('cls')
            
            print("Press CNTRL + C to stop the program at any time.")
            
            Player.position = Player.setPlayerCoords(xPtr, yPtr)
            print("\rPlayer starting position: " + str(Player.position), end='', flush=True)
            
            while(True):
                Player.position = Player.setPlayerCoords(xPtr, yPtr)
                temp_coords = Player.position
                time.sleep(0.1)
                if(Player.setPlayerCoords(xPtr, yPtr) != temp_coords):
                    print("\rPlayers current position: ", str(Player.setPlayerCoords(xPtr, yPtr)), end='', flush=True)
        
        except Exception as e:
            if('Invalid window handle.' in str(e)):
                print("ERROR: Ensure that WAKFU is open and runnning..\nExiting..")
            else:
                print("Error: ", str(e))
                
        
        
Main()
    


























# while(True):
#     time.sleep(1)
#     x, y = grid.getPlayerCoords(xPtr, yPtr)
#     integer_value = x
#     float_x = struct.unpack('!f', struct.pack('!i', integer_value))[0]
#     integer_value = y
#     float_y= struct.unpack('!f', struct.pack('!i', integer_value))[0]
    
#     player.position = int(float_x), int(float_y)
    
#     print(player.position)
#     print(calculateMove(player.position, poi[0])[0])
    
#     if(not calculateMove(player.position, poi[0])[1]):
#         moveMouse(calculateMove(player.position, poi[0])[0], center)
    
#     time.sleep(5)
# while(True):
#     player.state = grid.readPlayerState(stPtr)
#     time.sleep(0.25)
#     if(player.state in idleStates):
#         print("Idling..")
#     elif(player.state in actionStates):
#         print("Player is : " + actionStates[player.state])
#     elif(player.state in movementStates):
#         print("Player is moving..")
    
# idleStates = [line.strip() for line in open(r"./data/idle_states.txt").readlines()]
# movementStates = [line.strip() for line in open(r"./data/movement_states.txt").readlines()]

# idleStates = [int(i) for i in idleStates]
# movementStates = [int(i) for i in movementStates]
# movementStates = set(movementStates)

# actionStates_n = [line.strip() for line in open(r"./data/action_states.txt").readlines()]
# actionStates = {}
# for x in actionStates_n:
#     key = ''
#     value = ''
#     counter=0
#     while(counter<len(x)):
#         if(x[counter].isdigit()):
#             key += x[counter]
#         elif(x[counter] != ":" and not x[counter].isdigit()):
#             value+=x[counter]
#         counter+=1
#     actionStates[int(key)] = value
        
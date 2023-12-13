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
from utils import getPID, getWindow, setDimensions, parse_input
import time
import os
import PySimpleGUI as sg
import psutil
import subprocess


class Main():
    def __init__(self):
        try:
            
            os.system('cls')
            
            print("""\
                  Program by: Plastic

                                   ._ o o
                                   \_`-)|_
                                ,""       \ 
                              ,"  ## |   ಠ ಠ. 
                            ," ##   ,-\__    `.
                          ,"       /     `--._;)
                        ,"     ## /
                      ,"   ##    /


                """)
            
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

            print("Use last known memory locations? If you dont know what this is. \nPut N and go to the README\n")
            use_last = input("Y/N: ")
            print(use_last)
            use_last = use_last.lower()
            if(use_last == "n" or use_last == "no"):
                print("Getting game data.")
                executable_path = 'C:\\Program Files\\Cheat Engine 7.5\\Cheat Engine.exe'
                try:
                    # Use subprocess.run() to start the executable
                    subprocess.run([executable_path])
                except FileNotFoundError:
                    print(f"Error: The executable '{executable_path}' was not found.")

                time.sleep(0.25)
                i = 0
                while("cheatengine-x86_64-SSE4-AVX2.exe" in (i.name() for i in psutil.process_iter())):
                    i+=1
                    Processing = "."*i
                    print("\rProcessing"+Processing, end='', flush=True)
                    if(i>3):
                        i=0
                        print("\r                             ", end='', flush=True)
                        continue
                    time.sleep(0.5)
                print("\n")
           
            elif(use_last == "y" or use_last == "yes"):
                print("\nAlright.. I hope you're right..")
            else:
                print("Invalid entry.. idiot. Its Y or N")
                print("Going with last saved data.  If it fails, restart your bot dumbass.")
 
                
            with open("C:/Users/Jordan/Desktop/Programming/GIT/wakfubots/LUA/DATA/DATA.txt", 'r') as file:
                data = file.readlines()
            
            
            xPtr = data[0]
            
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
            
            print("\n Data for nerds below\n-----------------------------")
            print("Pid:", Player.PID)
            print("Player_Mem_Location: ", data)
            print(str(offset))
            time.sleep(2)
            s=0
            i=0
            while(s!=1):
                i+=1
                Processing = "."*i
                print("\rInitializing GUI"+Processing, end='', flush=True)
                if(i>3):
                    i=0
                    print("\r                                               ", end='', flush=True)
                    continue
                time.sleep(0.5)
                s+=1
            
            print("\nDone! Have fun.")
            
            def update_variables(window, variable1, variable2, variable3):
                window['-VAR1-'].update(f"Players position: {variable1}")
                window['-VAR2-'].update(f"Users mouse position: {variable2}")
                window['-VAR3-'].update(f"Points of interest: {variable3}")
            
            sg.theme('DarkGrey')
            
            layout = [
                [sg.Text("Players current position: ", key='-VAR1-')],
                [sg.Text("Players mouse position: ", key='-VAR2-')],
                [sg.Button("Add point of interest")],
                [sg.Text("Points of interest: ", key='-VAR3-')],
                [sg.Button("Harvest Resources")],
                [sg.Button("Save POI's"), sg.Button("DELETE")], 
                [sg.Button("Exit")]
            ]

            window = sg.Window("Wakfu Bots", layout, finalize=True)

            variable1 = 0
            variable2 = 0
            variable3 = 0
            
            with open('C:/Users/Jordan/Desktop/Programming/GIT/wakfubots/miningbot_ML/scripts/data/locations.txt', 'r') as file:
                var=file.readlines()
            
            POI = parse_input(var[0])
            
            while True:
                event, values = window.read(timeout=250)  # Updates every .25 secs

                if event == sg.WIN_CLOSED or event == 'Exit':
                    break
                elif event == "Add point of interest":
                    POI.append(Player.setPlayerCoords(xPtr, yPtr))
                elif event == "Save POI's":
                    with open('C:/Users/Jordan/Desktop/Programming/GIT/wakfubots/miningbot_ML/scripts/data/locations.txt', 'w') as file:
                        file.write(variable3)
                elif event == "DELETE":
                    with open('C:/Users/Jordan/Desktop/Programming/GIT/wakfubots/miningbot_ML/scripts/data/locations.txt', 'w') as file:
                        file.write("")
                        POI = []
                elif event == "Harvest Resources":
                    for x in POI:
                        try:
                            Grid.harvest_resource(list(variable1), list(x))
                            time.sleep(1)
                        except Exception as e:
                            print(variable1)
                            print(x)
                            print("Error: " + str(e))
                
                variable1 = Player.setPlayerCoords(xPtr, yPtr)
                variable2 = str(pg.position())
                variable3 = str(POI)
                update_variables(window, variable1, variable2, variable3)

            window.close()
            
        
        except Exception as e:
            if('Invalid window handle.' in str(e)):
                print("ERROR: Ensure that WAKFU is open and runnning../nExiting..")
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
        
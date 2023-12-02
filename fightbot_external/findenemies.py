# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 09:10:14 2023

@author: Jordan
"""

import pyautogui
import time
import win32api
import ctypes
import ctypes

def findenemy():
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen('resources/enemypos.png', confidence=0.9)
            pyautogui.moveTo(x, y)
            time.sleep(1)
            print("found an enemy")
            return 
            pass
        except Exception:
            pass

def findplayer():
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen('resources/playerpos.png', confidence=0.9)
            pyautogui.moveTo(x, y)
            time.sleep(1)
            print("found player")
            return 
            pass
        except Exception:
            pass

address = "70E1B26A8"
address = int(address,base=16)
ctypes.cast(address,ctypes.py_object).value
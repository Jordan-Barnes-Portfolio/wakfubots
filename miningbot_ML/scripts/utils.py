# -*- coding: utf-8 -*-
"""
@author: Jordan
"""
import psutil
import win32gui

"""
Gets a process ID given its name, IE Java.exe = 32800
"""
def getPID(name):
    pid = None
    for proc in psutil.process_iter():
        if name in proc.name():
           pid = proc.pid
           break
    return pid

"""
Returns the slope of a line given x1,y1,x2,y2
"""
def getSlope(x1, y1, x2, y2):
    return ((y2-y1)/(x2-x1))

"""
Sets the windows frame to a static x, y, w, h value.  Change these
In this function.  this should not change due to line calculations
"""
def setDimensions(name):
    hwnd = win32gui.FindWindow(None, name)
    rect = win32gui.GetWindowRect(hwnd)
    x, y, w, h = rect[0], rect[1], rect[2], rect[3]
    print("Current dimension configuration: ", x, y, w, h)
    print("Setting dimensions static for config purposes.")
    
    win32gui.MoveWindow(hwnd, 0, 0, 1000, 800, True)

"""
Gets a Window handle based on its name, IE "WAKFU"
"""
def getWindow(name):
    hwnd = win32gui.FindWindow(None, name)
    rect = win32gui.GetWindowRect(hwnd)
    x, y, w, h = rect[0], rect[1], rect[2], rect[3]
    return (x, y, w, h)

import ast

def parse_input(input_string):
    try:
        # Safely evaluate the input string as a literal expression
        result = ast.literal_eval(input_string)
        # Check if the result is a list of lists
        if isinstance(result, list) and all(isinstance(sublist, list) and len(sublist) == 2 for sublist in result):
            return result
        else:
            raise ValueError("Input is not a valid list of lists.")
    except (SyntaxError, ValueError) as e:
        print(f"Error: {e}", " ERROR IS HERE")
        return None
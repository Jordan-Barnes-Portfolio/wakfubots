# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 08:16:16 2023

@author: Jordan
"""

import pyautogui as pg
import win32api
import time
import win32gui

def getpixelcolor():
    state_left = win32api.GetKeyState(0x02)
    while True:
        a = win32api.GetKeyState(0x02)
        if a != state_left:  # Button state changed
            state_left = a
            if a < 0:
                print('Grabbing pixel color')
                x, y = pg.position()
                im = pg.screenshot()
                px = im.getpixel((x, y))
                return px
    

def locatepixel(color):
    s = pg.screenshot(region=(getsearcharea("WAKFU")))
    for x in range(s.width):
        for y in range(s.height):
            if s.getpixel((x, y)) == color:
                print(color)
                print(s.getpixel((x, y)))
                pg.move(x, y)
                return
                
def getsearcharea(window_title=None):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            x, y, x1, y1 = win32gui.GetClientRect(hwnd)
            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            return x, y, x1, y1
        else:
            print('Window not found!')
    else:
        return None

def checkforrgbvalues(R, G, B):
    x, y, x1, y1 = getsearcharea('WAKFU')
    start = (x, x1)
    end = (y, y1)
    
    x = int(end[0]-start[0] + 1) #calculates x value between start and end
    y = int(end[1]-start[1] + 1)  #calculates y value between start and end
    how_many_pixels_found = 0 #nothing found yet 
    for x in range(start[0], end[0] + 1, 1): #loops through x value
        for y in range(start[1], end[1] + 1, 1): #loops through y value
            if pg.pixel(x, y)[0] == R and pg.pixel(x, y)[1] == G and pg.pixel(x, y)[2] == B: #checks if the wanted RGB value is in the region
                how_many_pixels_found = how_many_pixels_found + 1 #adds one to the result

            y = y + 1
        x = x + 1
    return how_many_pixels_found #returns the total value of pixels with the wanted color in the region.


    
print(getpixelcolor())
R, G, B = getpixelcolor()

checkforrgbvalues(R, G, B)

    


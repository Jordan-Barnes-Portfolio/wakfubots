# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 07:59:44 2023

@author: Jordan
"""

import pyautogui as pg
import time

try:
    while True:
        print(pg.position())
        time.sleep(2)
except KeyboardInterrupt:
    pass
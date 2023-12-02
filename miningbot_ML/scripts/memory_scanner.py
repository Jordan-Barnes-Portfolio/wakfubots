# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:20:42 2023

@author: Jordan
"""

import pygamehack as gh
import main

class Memory_Scanner():
    
    def __init__(self):
        hack = gh.Hack()
        hack.attach(main.PID)
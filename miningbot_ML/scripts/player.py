# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 20:27:16 2023

@author: Jordan
"""
from ReadWriteMemory import ReadWriteMemory
import numpy
import struct

class Player:
    
    state = None
    position = []
    PID = None
    
    def __init__(self, state, position, PID):
        self.state = state
        self.position = position
        self.PID = PID
        
    """
    Takes in xPtr and yPtr and returns players position..
    """
    def setPlayerCoords(self, xPtr, yPtr):
        
        rwm = ReadWriteMemory()
        process = rwm.get_process_by_id(self.PID)
        process.open()
        x_val = process.read(xPtr)
        y_val = process.read(yPtr)
        process.close()

        integer_value = numpy.array(x_val).astype(numpy.int32)
        float_x = struct.unpack('!f', struct.pack('!i', integer_value))[0]
        integer_value = numpy.array(y_val).astype(numpy.int32)
        float_y= struct.unpack('!f', struct.pack('!i', integer_value))[0]
        return [int(float_x), int(float_y)]
    
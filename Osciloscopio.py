# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:39:33 2019

@author: nicon
"""

import pyvisa
import numpy as np

class Osciloscopio(object):

    def __init__(self, instrument = 1): #Ver cual es 1 y 0 con el generador
        self.rm = pyvisa.ResourceManager()
        if len(self.rm.list_resources()) > 0:
            self.inst = self.rm.open_resource(self.rm.list_resources()[instrument])
        else:
            self.inst = []
            print('No se detectó ningún instrumento')
        if self.inst != []:
            try:
                print('El IDN del instrumento es ', self.inst.query("*IDN?"))
            except:
                print('El instrumento no respondió cuando se le preguntó el nombre.')

    def getData:
        self.inst.query_ascii_values('CURVe?')

    def ReadVoltage:
        ymult = self.inst.query_ascii_values('WFMPRE:YMULT?') #Vertical scale factor
        yzero = self.inst.query_ascii_values('WFMPRE:YZERO?') #Offset Voltage
        yoff = self.inst.query_ascii_values('WFMPRE:YOFF?')   #Vertical Offset
        xincr = self.inst.query_ascii_values('WFMPRE:XINCR?') #Horizontal sampling interval
        #Ver https://www.i3detroit.org/wi/images/2/2d/460-ProgrammerManual.pdf pag 2-43

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:39:33 2019

@author: nicon
"""

import numpy as np
import matplotlib.pyplot as plt
import lantz 
from lantz import MessageBasedDriver


class Osciloscopio(MessageBasedDriver):
        
    def data_encdg_ascii(self):
        self.write('DATA:ENCDG ASCII')
        
    def data_encdg_bin(self):
        self.write('DATA:ENCDG RIBinary')

    def get_data_ascii(self):
        self.data_encdg_ascii()
        read = self.resource.query_ascii_values('CURVe?')
        
        plt.plot(read)
        plt.show()
        
        return read
        
        plt.plot(read)
        plt.show()
        
        return read

    def read_voltage(self):
        
        self.data_encdg_bin()
        read = np.array(self.resource.query_binary_values('CURVe?', datatype = 'b', is_big_endian= True))
        
        ymult = self.resource.query_ascii_values('WFMPRE:YMULT?') #Vertical scale factor
        yzero = self.resource.query_ascii_values('WFMPRE:YZERO?') #Offset Voltage
        yoff = self.resource.query_ascii_values('WFMPRE:YOFF?')   #Vertical Offset

        voltage = yzero + ymult*(read - yoff)
        
       # plt.plot(voltage)
        #plt.show()
        
        return voltage
    
       
    def read_time(self):    
        xincr = self.resource.query_ascii_values('WFMPRE:XINCR?') #Horizontal sampling interval
        xzero = self.resource.query_ascii_values('WFMPRE:XZERO?')
        pt_off = self.resource.query_ascii_values('WFMPRE:PT_Off?')
        
        n = np.linspace(0,2500,2500)
        #Ver https://www.i3detroit.org/wi/images/2/2d/460-ProgrammerManual.pdf pag 2-43
        time = xzero + xincr*(n - pt_off)
        
        return time
    
    def grafico(self):
        voltage = self.read_voltage()
        time = self.read_time()
        
        vpp = 2*max(voltage)
        
        plt.plot(time, voltage)
        plt.xlabel('Time (s)')
        plt.ylabel('Voltage (V)')
        plt.show()
        
        return vpp

    
    def set_timebase(self, seconds):
        self.write('HOR:DEL:SCA {}'.format(seconds))
        
 #%%

with Osciloscopio.via_usb('C102223') as Osc:
     Osc.read_time()
    
        

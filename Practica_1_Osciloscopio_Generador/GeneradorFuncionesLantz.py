# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:30:09 2019

@author: Publico
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 19:16:28 2019
@author: nicon"""


import numpy as np
import matplotlib.pyplot as plt
import time
import lantz 
from lantz import MessageBasedDriver
from lantz.core import mfeats
from Osciloscopio import Osciloscopio

class GeneradorFunciones(MessageBasedDriver):

    
        
    def TurnOn(self, channel = 1):
        self.write("OUTPut{}:STATe ON".format(channel))
        
    def TurnOff(self, channel = 1):
        self.write("OUTPut{}:STATe OFF".format(channel))
        
    def GetFrequency(self, channel = 1):
        return self.query('SOURce{}:FREQuency?'.format(channel))
        
    def SetFrequency(self, freq, channel = 1): #gen.SetFrequency('5 kHz') o por default en Hz
        self.write("SOURce{}:FREQuency {}".format(channel,freq))
    
    def GetShape(self, channel = 1):
        return self.query('SOURce{}:FUNCtion:SHAPe?'.format(channel))
    
    def SetShape(self, shape, channel = 1): #gen.SetShape('SQUare')
        self.write("SOURce{}:FUNCtion {}".format(channel,shape)) 
    
    def GetVoltage(self, channel = 1):
        return self.query('SOURce{}:VOLTage:LEVel:IMMediate:AMPLitude?'.format(channel))
    
    def SetVoltage(self, voltage, channel = 1): #gen.SetVoltage(2) Vpp
        self.write('SOURce{}:VOLTage:LEVel:IMMediate:AMPLitude {}'.format(channel, voltage))
        
    def GetOffset(self, channel = 1):
        return self.query('SOURce{}:VOLTage:LEVel:IMMediate:OFFSet?'.format(channel))        
    
    def SetOffset(self, offset, channel = 1): #gen.SetOffset(1) V
        self.write('SOURce{}:VOLTage:LEVel:IMMediate:OFFSet {}'.format(channel, offset))        
    
    def GeneralSet(self, freq, voltage, offset = '0 V', shape = 'SIN', channel = 1):
        self.SetFrequency(freq, channel)
        self.SetVoltage(voltage, channel)
        self.SetOffset(offset, channel)
        self.SetShape(shape, channel)
    
    def DiscreteSweep(self, freqini, frecfin, step, timeoff = 1,  channel = 1):
        Frequencies = np.array(float(freqini.split(" ")[0]), float(frecfin.split(" ")[0]), float(step.split(" ")[0]))
        #esto es por si el input lo consideramos como "2 kHz" o algo así. el split separa un string
        #en partes, dependiendo del separador (en este caso el separador es un espacio).
        for Fr in Frequencies:
            self.inst.write("SOURce{}:FREQuency {} {}".format(channel, Fr, freqini.split(" ")[1]))
            time.sleep(timeoff)
        
    def ContinuosSweep(self, freqini, freqfin, sweeptime, sweeptype = "LINear", channel = 1):
        self.write('SOURce{}:SWEep:SPACing {}'.format(channel, sweeptype))
        self.write('SOURce{}:SWEep:TIME {}'.format(channel, sweeptime))    
        self.write('SOURce{}:FREQuency:STARt {}'.format(channel, freqini))
        self.write('SOURce{}:FREQuency:STOP {}'.format(channel, freqfin))


#%%
        

with GeneradorFunciones.via_usb('C033248') as Genf:
     with Osciloscopio.via_usb('C065092') as Osc:
        
        Frequencies = np.linspace(100, 1000, 5)
        
        atotal = []
        btotal = []
        for Fr in Frequencies:
            Genf.SetFrequency(Fr)
            #time.sleep(2)
            a = Osc.read_time()
            b = Osc.read_voltage()
            #time.sleep(1)
           #atotal.append(list(a))
            #btotal.append(list(b))
            plt.plot(a, b)
            plt.show()
           # time.sleep(2)
            
        
        
        






# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:37:36 2019

@author: Publico
"""

import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import time


fsamp = 44100

def funcion(tau, frequency, Amplitude = 1, fs = 44100): #por default tiene 44100 y no hay que aclararsela
    myarray = Amplitude*np.sin(np.linspace(0,tau,int(tau*fs))*frequency*(2*np.pi))
    return myarray

#sd.play(funcion(3, fsamp, 440),fsamp)

#sd.stop()

#time.sleep(3)
#array = funcion(3, fsamp, 450)
#plt.plot(array)

def barrido():
    frecuencia = np.linspace(200, 600, 10)
    for f in frecuencia:
        myarray = funcion(1, fsamp, f)
        sd.play(myarray, fsamp)
        time.sleep(1)
        #print(f)
        
#barrido()
def pasaralista(a):
    b = list(a)
    c = []
    i = 0
    while i < len(b):
        c.append(float(b[i]))
        i = i + 1
    return c


def record(tau, fs):
    myrecording = sd.rec(int(tau*fs), samplerate=fs, channels=1, blocking=True)
    time_total = np.linspace(0, tau, int(tau*fs))
    return myrecording, time_total

myrecording, time_total = record(3, fsamp)

#print('my recording ', myrecording)
#print('time total', time_total)

#time.sleep(3)
#sd.wait()

plt.plot(pasaralista(myrecording))
#plt.plot(list(time_total), pasaralista(myrecording))

#plt.plot(myrecording)
#print(len(list(time_total)))
#print(len(list(pasaralista(myrecording))))
plt.show()






# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:16:55 2019

@author: nicon
"""
import numpy as np
import random
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy.signal import find_peaks    

def NoisySin(f):
    x = np.linspace(0, 4*np.pi/f, 5000)
    y = [np.sin(2*np.pi*f*i) + random.random()*0.1 for i in x] 
    return x, y

def CommonSin(x, A, w, phi):
    return A*np.sin(w*x + phi)

def GetFrequency(V, t, Aguess = 1, wguess = 0.5, phiguess = 0):
    params, params_cov = curve_fit(CommonSin, t, V, p0=[Aguess, wguess, phiguess])
    print(params)
    return params[1]

def Frecuencias_FFT(x, y, debug = False):
    yfft = fftpack.fft(y)
    N = len(x)
    T = x[-1]/N
    xf = np.linspace(0, 1/(2*T), int(N/2))
    yf = 2.0/N * np.abs(yfft[:N//2])
    
    
    try:
        PosicionPicos, IntensidadPicos = find_peaks(yf, height=yf[0])
        print('entro en try')
    except ValueError:
        print('entro en except')
        yf = list(np.transpose(yf)[0])
        PosicionPicos, IntensidadPicos = find_peaks(yf, height=yf[0])
    
    VectorFrecuenciaPicos = [xf[i] for i in PosicionPicos]
    if len(list(IntensidadPicos['peak_heights'])) > 0:
        PosicionImax = np.argmax(list(IntensidadPicos['peak_heights']))
        FrecuenciaDelMaximo = VectorFrecuenciaPicos[PosicionImax]
    else:
        FrecuenciaDelMaximo = 0
        
    if debug:
        print('El vector de las frecuencias de los picos es', VectorFrecuenciaPicos)
        print('Las intensidades de los picos son ', IntensidadPicos)
        print('La frecuencia del maximo es ', FrecuenciaDelMaximo)
#    print('La frecuencia es', VectorFrecuenciaPicos)
#    return VectorFrecuenciaPicos
    return xf, yf, FrecuenciaDelMaximo



if __name__ == '__main__':
#    Talter = np.transpose(Variables['reco'][0])[0]
#    xf, yf, fmax = Frecuencias_FFT(list(T[0]), Talter)    
#    plt.plot(xf, yf)
#    plt.plot(list(T[0]), list(V[0]), 'o')
    Pantallas = Variables['reco']
    Tiempos = Variables['tiempos']
    xf, yf, fmax = Frecuencias_FFT(Tiempos[0], np.transpose(Pantallas[0])[0])

    frec_medidas = []
    for i in range(len(Pantallas)):
        xf, yf, fmax = Frecuencias_FFT(Tiempos[i], np.transpose(Pantallas[i])[0])
        frec_medidas.append(fmax)
    

    plt.plot([f/1000 for f in frequency], [g/1000 for g in frec_medidas],'o')
    plt.xlabel('Frecuencia enviada por el generador (kHz)')
    plt.ylabel('Frecuencia medida por la placa de audio (kHz)')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
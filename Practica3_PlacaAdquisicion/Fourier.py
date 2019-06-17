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


def Frecuencias_FFT(x, y, debug = False):
    """
    Versión actualizada y debuggeada. Extrae la frecuencia de mayor
    amplitud de una transformada de fourier de una señal y(x).
    """
    yfft = fftpack.fft(y)
    N = len(x)
    T = x[-1]/N
    xf = np.linspace(0, 1/(2*T), int(N/2))
    yf = 2.0/N * np.abs(yfft[:N//2])
    
    
    try:
        PosicionPicos, IntensidadPicos = find_peaks(yf, height=yf[0])
    except ValueError:
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

    return xf, yf, FrecuenciaDelMaximo



if __name__ == '__main__':

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

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
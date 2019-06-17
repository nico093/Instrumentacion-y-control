# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:16:55 2019

@author: nicon
"""
import numpy as np
import random
from scipy.optimize import curve_fit
from scipy import fftpack
from scipy.signal import find_peaks    

def NoisySin(f):
    """
    Esta funcion crea un seno ruidoso de frecuencia f
    """
    x = np.linspace(0, 4*np.pi/f, 1000)
    y = [np.sin(2*np.pi*f*i) + random.random()*0.1 for i in x] 
    return x, y

def CommonSin(x, A, w, phi):
    """
    Esta funcion devuelve un seno comun. Ok, no es muy sofisticada. 

    Ok, no se por que la hicimos
    """
    return A*np.sin(w*x + phi)

def GetFrequency(V, t, Aguess = 1, wguess = 0.5, phiguess = 0):
    """
    Esta funcion es para ajustar un seno con ciertos parametros iniciales para extraer
    la frecuencia, pero no es muy eficiente.
    """
    params, params_cov = curve_fit(CommonSin, t, V, p0=[Aguess, wguess, phiguess])
    print(params)
    return params[1]

def Frecuencias_FFT_old(x, y):
    """
    Esta funcion es eficiente para extraer la frecuencia de una señal sinusoidal
    La función actualizada está en Fourier.py
    """
    yfft = fftpack.fft(y)
    N = len(x)
    T = x[-1]/N
    xf = np.linspace(0, 1/(2*T), N/2)
    yf = 2.0/N * np.abs(yfft[:N//2])
    PosicionPicos, IntensidadPicos = find_peaks(yf, height=yf[0])
    VectorFrecuenciaPicos = [xf[i] for i in PosicionPicos]
#    print('La frecuencia es', VectorFrecuenciaPicos)
    MaxPeak = max(IntensidadPicos)
    
    return VectorFrecuenciaPicos
    #return xf, yf, N, PosicionPicos



if __name__ == '__main__':

    x, y = NoisySin(100)
#    params, params_cov = curve_fit(CommonSin, x, y, p0=[1, 0.5, 0])
#    plt.plot(x, CommonSin(x, *params))
#    plt.plot(x, y)  

#    xf, yf, N, pp = Frecuencias_FFT(x, y)
#    plt.plot(xf, yf)
    f = Frecuencias_FFT(x, y)    
    print(f)
#    print(Fpicos)
    #plt.plot(x, y)


















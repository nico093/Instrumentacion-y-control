# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:57:50 2019

@author: Publico
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:16:55 2019
@author: nicon
"""
import numpy as np
import random
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def NoisySin(w):
    x = np.linspace(0, 4*np.pi/w, 1000)
    y = [np.sin(w*i) + random.random()*0.1 for i in x]
    return x, y

def CommonSin(x, w, phi):
    return 0.5*np.sin(w*x + phi)

def GetFrequency(V, t, wguess = 1, phiguess = 0):
    params, params_cov = curve_fit(CommonSin, t, V, p0=[wguess, phiguess])
    return params, params_cov

if __name__ == '__main__':

    x, y = NoisySin(0.5)
    params, params_cov = curve_fit(CommonSin, x, y, p0 = [0.5, 3])
    plt.plot(x, CommonSin(x, *params))
    plt.plot(x, y) 
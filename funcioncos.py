# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:33:34 2019

@author: nicon
"""
import numpy as np
import matplotlib.pyplot as plt

#x = np.linspace(0,5*np.pi,50)

#def function(A,w,x):
#    f = A*np.cos(w*x)
#    return f

#plt.plot(x,function(10,1,x))
#plt.plot(x,function(5,1,x),'r')
#plt.show()
    

def GraficarCoseno(A, w):
    periodo = 2*np.pi*(w**(-1))
    print(periodo)
    x = np.linspace(0, 2*periodo, 100)
    cosx = [A*np.cos(w*i) for i in x]
    plt.plot(x, cosx)
    plt.show()

GraficarCoseno(1, 2)
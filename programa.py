import Osciloscopio as osc
import GeneradorFunciones as gf
import numpy as np
import matplotlib.pyploy as plt
import time
import Save as sv
#Creo el objeto generador de funciones:

generador = gf.GeneradorFunciones()
osciloscopio = osc.Osciloscopio()
frec = []
vpp = []

for i in range(10):
    generador.SetFrequency(str(i)) #No se si esto lo va a leer porque no se bien los parametros de la clase.
    vpp = vpp.append(osciloscopio.ReadVoltage()) #hay que ver que mide ymult para hacer la cuenta ahi y que devuelva Vpp.
    frec = frec.append(i)
    time.sleep(1)


f = save('frecuencia.txt', frec)
f.open()

v = save.('vpp.txt', vpp)
v.open()

plt.plot(f,v, 'ro')
plt.show()

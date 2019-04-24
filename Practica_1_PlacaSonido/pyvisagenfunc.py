import pyvisa
import time
import numpy as np

rm = pyvisa.ResourceManager()
print(rm.list_resources())
inst = rm.open_resource('USB0::0x0699::0x0346::C034166::INSTR')
#rm.close()


print('El instrumento es ', inst.query("*IDN?"))

inst.write("OUTPut1:STATe ON")

for i in range(10):
    inst.write("SOURce1:FREQuency " + str(i) + " kHz")
    print("SOURce1:FREQuency " + str(i) + " kHz")
    time.sleep(1)
    

inst.write("OUTPut1:STATe OFF")    

inst.write('SOURce1:SWEep:MODE AUTO')

inst.query('SOURce1:FUNCtion:SHAPe?')

def GenFunc(frec, vpp, offset, shape):
    inst.write("SOURce1:FREQuency " + frec)
    inst.write('SOURce1:VOLTage:LEVel:IMMediate:AMPLitude ' + vpp)
    inst.write('SOURce1:VOLTage:LEVel:IMMediate:OFFSet ' + offset)
    inst.write('SOURce1:FUNCtion ' + shape)
    
GenFunc('8 kHz', '2 Vpp','1 mV','SQUare')


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
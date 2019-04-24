# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:39:33 2019

@author: nicon
"""

import pyvisa
rm = pyvisa.ResourceManager()
inst = rm.open_resource('USB0::0x0699::0x0363::C065093::INSTR')
print(inst.query("*IDN?"))
print(inst.query('MEASUrement:IMMed:TYPe?'), inst.query('MEASUrement:IMMed:VALue?'))


inst.query('CURVe?')







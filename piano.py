# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:59:00 2019

@author: ftrub
"""

import numpy as np 
def sine_wave (t,f) : 
    return(np.sin(2*np.pi*t*f))
 
import matplotlib.pyplot as plt

x=[i/299 for i in range(300)]
y=[sine_wave(i,4) for i in x]
plt.plot (x,y)    

def square_wave (t,f):
    return(1-2*((int(t*2*f))%2))

x=[i/299 for i in range(300)]
y=[square_wave(i,4) for i in x]
plt.plot (x,y)    

def sawtooth_wave (t,f):
    return(-1+((t*2*f)%2))

x=[i/299 for i in range(300)]
y=[sawtooth_wave(i,4) for i in x]
plt.plot (x,y)  

def triangle_wave (t,f):
    return(-1+((t*8*f)%2)/2)

x=[i/299 for i in range(300)]
y=[triangle_wave(i,4) for i in x]
plt.plot (x,y) 
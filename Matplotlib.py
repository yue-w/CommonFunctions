# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 22:23:01 2020

@author: wyue
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,3,500)
y = np.exp(-np.power(x,2)/2)/np.sqrt(2*np.pi)

fig1,ax1 = plt.subplots()
ax1.plot(x,y)
ax1.set(xlabel='x',ylabel=r'$f_X(x)$')

fig1.savefig('test.jpg')
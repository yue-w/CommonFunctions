# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 22:44:02 2020

@author: wyue
Recording the running time
"""

import time
start_time = time.time()
a = 0
for i in range(10000):
    a+=i
print(a)    
print("--- %s seconds ---" % (time.time() - start_time))
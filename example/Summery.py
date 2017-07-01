# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 14:20:00 2017

@author: DKjack
"""

#Summery of Numpy SciPy Matplotlib and Pandas
#%%timeit
total = 0
for i in range(1000):
    for j in range(1000):
        total += i *(-1)**j
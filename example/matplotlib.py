# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 19:55:02 2017

@author: DKjack
"""
#Scipy program
#from pylab import*
#from matplotlib

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,10)
y= x**2
figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()

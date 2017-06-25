# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:14:09 2017

@author: DKjack
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,3,20)
y = np.linspace(0,9,20)
#plt.plot(x,y)
#plt.plot(x,y,'o')


image = np.random.rand(30,30)
#plt.imshow(image, cmap=plt.cm.hot)
#plt.colorbar()

a =np.arange(6) + np.arange(0,51,10)[:,np.newaxis]
print (a)
b = np.diag(np.arange(7))
print (b)
bdelete = np.delete(b,np.s_[:2:],1)
print(bdelete)

mask = np.array([1,0,1,0,0,1],dtype = bool)
print (a[mask,2])

# Broadcasting:
  #  c = np.tile(np.arange(0, 40, 10), (3,1)).T
   # print (c)
  #  b = np.array([0,1,2])
   # print(c+b)
    
x = np.linspace(0,1,20)
y = np.cos(x) + 0.3*np.random.rand(20)
p = np.poly1d(np.polyfit(x,y,3))
t = np.linspace(0,1,200)
plt.plot(x,y, 'o', t, p(t), '-')
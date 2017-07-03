# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 09:51:06 2017

@author: DKjack
"""

##Scientific Computing with Python3 main in Spysder
#Since 11.2016iimport 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import os


#modules and Scipts

def f(x):
    return 2**x +1

z = []
for x in range(10):
        if f(x) >4:
            z.append(x)
        else:
            z.append(-1)
            
print(z)
print(os.getcwd())
#Using modules and nameSpaces
from smartfunctions import *
import smartfunctions as sf
print(sf.f(2))
from smartfunctions import g
print(g(2))

##Chapter2 Variables and Basic Types
N = 10
#following vector contains the Nth roots of unity:
unity_roots = np.array([np.exp(1j*2*np.pi*k/N) for k in range(N)])
#access all the real or imaginary parts with real or imag:axes(aspect = 'equal')
#plt.plot(unity_roots.real, unity_roots.imag, 'o')
np.allclose(unity_roots**N, 1) #Ture
#Your need to add modules included in you functions
##In is ones functions is still a problem to us

##Chapter 3 Container Types:
#lists
L = ['a',20.0,5]
M = [3,['a',-3.0, 5]]
l=list(range(4))
print (l)

#Slicing;切片
L2 = ['C','l','o','u','d','s']
 
a = [1,2,3]
for iteration in range(4):
    print(sum(a[0:iteration-1]))
    
#Strides:截取
L3 =list(range(100))
L3[:10:2]
L3[10:20:3]
#use Strides to resvered order
L4 = list(range(5))
R = L4[::-1]
print(R)
# Some List methods: 
#list.append(x);
#list.expend(L);
#list.insert(i,x);
#list.remove(x);
#list.count(x)
#list.sort(x)
#list.resverse()
#list.pop()

#In-place operations
print(L4)
L4.reverse()
print(L4)
L5 = [6,5,7,5,2,1,3,6,7]
print(L5)
L5.sort()#这个排序是在内部排序使用有专门的使用方法和关键字
print(L5)
#Zip opertion
index = [0,1,2,3,4]
name = ['zhou','chen','john','li']
#print(list(zip(name,index)))

#Arrays :
M = np.array([[1,2,3],[3,4,5]])
v = np.array([[4,5],[6,7]])
#this two Matrix

#Tuples
my_tuple = (1,2,3)


#Dictionaries 
#Creating and altering dictionaries:
truck_wheel = {'name' : 'wheel',
               'mass' : 5.70,
               'Ix'   :20.0,
               'Iy'   :1.,
               'Iz'   :17.0,
               'center of mass' : [0.,0.,0.]}
#for key in truck_wheel.values():
    #print (key)
    
#for item in truck_wheel.items():
    #print(item)
    
#Sets
A = {1,2,3,5,7,100}
B= {2,4,6,8}
C = A.union(B)
D = A.intersection(C)
E = C.difference(A)
print(C)
print(D)
print(E)




# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 15:54:30 2017

@author: DKjack
"""

##This is Linear Algebra in arrays
##Advanced arrays ticks


#Vectors and matrcies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

v1 = np.array([1,2,3])
v2 = np.array([0,2,1])

#scalar multiplications/divisions
print(2*v1)
print(v1/2)

#linear combinations
print(3*v1+2*v2)

#norm
from scipy.linalg import norm
print(norm(v1))

#indexing and slices
v = np.array([1,2,3])
m = np.array([[1,2],[3,4]])
#print (v[0])
v[0] = 10
#print (v[0])
#slices
#print(v[:2])
v[:2] = [0,1]
#print(v[:2])


#Solving a linear system
#from scipy.linalg import solve
#A = np.array([[1.,2.],[3.,4.]])
#b = np.array([1.,4.])
#x = solve(A,b)
#np.allclose(np.dot(A,x),b)
#np.allclose(A @x,b)

#Accessing array items has finish in pervious python files

#Arrays Shape and Reshape
S =np.array(range(10))
S1 = S.reshape(2,5)
print (S1)
print (S1.reshape(5,2))

#Transpore
print("this is Transpore of S1 :\n")
print (S1.T)

#Linear algebra methods in SciPy
##After this is about SciPy lib ,have many lib methods


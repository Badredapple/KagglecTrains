# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 14:25:10 2017

@author: DKjack
"""
##Classification  
#DataSet MNIST
#reference book : hands-on Machine Learning with Scikit-Learn and Tensorflow
from sklearn.datasets import fetch_mldata
mnist = fetch_mldata('MNIST original')
print(mnist)

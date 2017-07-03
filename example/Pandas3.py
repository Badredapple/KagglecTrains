# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:08:17 2017

@author: DKjack
"""
##This pandas Tutorials is mainly for Pandas I/O 
#In this ,more Struct ,functions, and standard opertion will be included
import pandas as pd
import matplotlib.pyplot as plt
import os

#pd.set_option('display.mpl_style','default')
#plt.rcParams['figure.figsize'] = (15,5)
##Please use `matplotlib.pyplot.style.use` instead.
print(os.getcwd())
football_df = pd.read_csv('footballteam.csv')
print(football_df )
print('\n\n')
print(os.getcwd())
print('\n\n')
print(football_df [:3])

fixed_df = pd.read_csv('bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
#print(fixed_df[:3])


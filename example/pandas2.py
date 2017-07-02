# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 14:35:55 2017

@author: DKjack
"""
#Pandas tutorials 2
#from http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
pd.set_option('max_columns',50)
#%matplotlib inline
s = pd.Series([7,'Hiesenberg', 3.14, -17893434,'Happy Eating!'],index = ['1','2','3','4','5'])
#print(s)
d = {'beijing':100,'shanghai':200,'tianjin':300,'sichuan':500}
cities = pd.Series(d)
#print(cities)
less_than_300 = cities < 300
#print(less_than_300)
#print('\n')
#print(cities[less_than_300])
#numpy and pandas :
#print(np.square(cities))
#print('\n')
# add two Series together 
d2 = {'beijing':250, 'guangzhou':300,'hunan':500}
cities2 = pd.Series(d2)
#print (cities2)
#print(cities+cities2)
#null index values is NaN
cities3 = cities+cities2
print(cities3.notnull())
print(cities3[cities3.notnull()])
print('\n\n\n')

#pandas DataFrame
data = {'year':[2000,2001,2002,2003,2004,2005,2006],
        'team':['Bears', 'Lions', 'Lions','Packers','Packers','Bears','Lions'],
        'wins':[5,6,11,2,7,8,2,],
        'losses':[3,6,9,6,9,4,2]}
footballteam = pd.DataFrame(data,columns= ['year','team','wins','losses'])
#print (footballteam)

#read CSV from disk
#print(os.getcwd())
#from_csv = pd.read_csv('mariano-rivera.csv')
#print(from_csv.head())
#print ('\n\n\n')
#read csv and add columns
cols = ['num', 'game','date', 'team', 'home_away', 'oppent',
        'result','quarter','distance','receiver', 'score_before',
        'score_after']
no_headers = pd.read_csv('peyton-passing-TDs-2012.csv',sep =',', header = None,names = cols)
#print(no_headers.head())

#add to csv files
footballteam.to_csv('footballteam.csv')
#pandas read mysql 
print('\n\n')
#import pandas as pd
#import mysql.connector as sql
#mysql_cn = sql.connect(host ='localhost',port = 3306, user = 'root',password = 'root')
#dfMysql = pd.read_sql('SELECT *FROM t_book;',con =mysql_cn)
#mysql_cn.close()
#need python sql dirvers

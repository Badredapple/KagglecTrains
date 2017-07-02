# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 21:15:20 2017

@author: DKjack
"""

#Pandas tutorial basic
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([100, "python", "Soochow", "Qiwsir"])
print (s)
s1 =pd.Series([100, "python", "Soochow", "Qiwsir"],index=["mark", "title", "university", "name"])
print (s1)
sd = {"python":800, "C++":300, "C#":402}
s2 = pd.Series(sd)
print (s2)
s3 = pd.Series(sd, index = ["java","python","golang","C#"])
print (s3) 
s3.index = ["p1", "p2", "p3", "p4"]
print (s3)

dates = pd.date_range('20130101', periods = 6)
print (dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns= list('ABCD'))
print (df)

#df2 = df.copy()
#df2['E'] = ['1','2','3','4'.'5'.'6']
#print(df2)
#Missing Data
df3 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df3.loc[dates[0]:dates[1],'E'] = 1
print(df3)


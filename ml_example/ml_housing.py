# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 11:56:35 2017

@author: DKjack
"""
import os
import pandas as pd
#import scipy as 
import numpy as np
import matplotlib.pyplot as plt
import hashlib




#def load_housing_data(housing_path = HOUSING_PATH):
 #   csv_path = os.path.jion(housing_path,"housing.csv")
  #  return pd.read_csv(csv_path)
#this could be simple use pd.read_scv
def load_housing_data(): 
    print(os.getcwd())
    csv_name=input("Input Csv name ,which you want load:")
    print("you want to load:"+csv_name)
    return pd.read_csv(csv_name)

housing = load_housing_data()
##Mtaplotlib work
#housing.hist(bins=50,figsize=(20,15))
#plt.show()

#Create Test Set
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

train_set,test_set = split_train_test(housing,0.2)
print(len(train_set), "train+", len(test_set),"test")


#add a hash identifier index column
def test_set_check(idfentifier,test_ratio, hash):
    return hash(np.int64(idfentifier)).diget()[-1] < 256*test_ratio

def split_train_test_by_id(data,test_ratio, id_column, hash=hashlib.md5):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id: test_set_check(id, test_ratio, hash))
    return data.loc[~in_test_set], data.loc[in_test_set]

#use row index as ID 
housing_with_id = housing.reset_index()
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")

#


  
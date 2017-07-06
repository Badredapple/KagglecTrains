# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 19:11:04 2017

@author: DKjack
"""

##This is ml_housing 2 main for Machine Learning Algorithms
import numpy as np
import os
import pandas as pd




#load housing data:
def load_housing_data(): 
    print(os.getcwd())
    csv_name=input("Input Csv name ,which you want load:")
    print("you want to load:"+csv_name)
    return pd.read_csv(csv_name)

housing = load_housing_data()

#print(housing.head())
#drop some attributes :
housing.drop("total_bedrooms",axis =1)
#print(housing.head())
#deal with missing values: use Imputer
from sklearn.preprocessing import Imputer
imputer = Imputer(strategy = "median")

housing_num = housing.drop("ocean_proximity",axis = 1)
imputer.fit(housing_num)
#print(imputer.statistics_)
#print(housing_num.median().values)
 
X=imputer.transform(housing_num)
 
housing_tr =pd.DataFrame(X, columns = housing_num.columns)


#handling Text and Categorical Attibutes
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
housing_cat = housing["ocean_proximity"]
housing_cat_encoded = encoder.fit_transform(housing_cat)
print(housing_cat_encoded)
print(encoder.classes_)


#convert integer catrgorical values into one-hot vetor
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
housing_cat_hot = encoder.fit_transform(housing_cat_encoded.reshape(-1,1))
print(housing_cat_hot)


from sklearn.preprocessing import LabelBinarizer
encoder = LabelBinarizer()
housing_cat_1hot = encoder.fit_transform(housing_cat)
print(housing_cat_1hot)

##This is a small transformer class that adds the combined attributes 
from sklearn.base import BaseEstimator, TransformerMixin
rooms_ix, bedrooms_ix,population_ix, household_ix = 3,4,5,6
class CombindedAttributesAdder(BaseEstimator, TransformerMixin):
   # def __init__(self, add_bedroom_per_room =True):
   #     self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self,X, y = None):
        return self
    def transform(self, X, y=None):
        rooms_per_household = X[:,rooms_ix] / X[:,household_ix]
        population_per_household = X[:, population_ix]/X[:,household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:,rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]
attr_adder = CombindedAttributesAdder(add_bedrooms_per_room = False)
housing_extra_attribs = attr_adder.transform(housing.values)

housing_extra_attribs = pd.DataFrame(housing_extra_attribs, columns=list(housing.columns)+["rooms_per_household", "population_per_household"])
print(housing_extra_attribs.head())
 
 ##Feature Scaling
    
##Transformation Pipelines
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

num_pipeline =Pipeline([
        ('imputer', Imputer(strategy = "median")),
        ('attribs_adder', CombindedAttributesAdder()),# null Parameter.....
        ('std_caler',StandardScaler()),
        ])

housing_num_tr = num_pipeline.fit_transform(housing_num)
#This Section because of CombindedAttributesAdder() need a Parameter ,SO it cash...


##Join two pipeline into together:
from sklearn,pipeline import FeatureUnion

num_attribs = list(housing_num)
cat_attribs = ["ocean_proximity"]

num_pipeline = Pipeline([
            ('selector',DataFrameSelextor(num_attribs)),
            ('imputer',Imputer(stragtegy = "median")),
            ('attribs_adder',CombinedAttributesAdder())
            ('std_scaler', StandardScaler()),
        ])















###Now will try to select and train a model                                                                     
 #Train and Evaluate your training Set
#from sklearn.linear_model import LinearRegression

#lin_reg = LinearRegression()
#lin_reg.fit(housing_prepared, housing_labels)
#output some instances:
#some_data = housing.iloc[:5]
#some_labels = housing_labels.iloc[:5]

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
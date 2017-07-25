# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 10:47:41 2017

@author: DKjack

"""
import json
import pandas as pd
import numpy as np

def load(json_name):
    with open(json_name) as json_file:
        data = json.load(json_file)
        return data


file_dict = load('E:/DataScience/Code/training/粥粥_Sensors_20105_Android_2017-07-18-10-12-24-992507.json')
sensors_list = file_dict.get('sensors')
#print(file_dict.get('sensors'))

temp_list = []
for i in range(len(sensors_list)):
    l = sensors_list[i].split(',')
    if i == 0:
        temp_list = np.matrix(l)
    temp_list = np.vstack((temp_list,l))
dataframe_list = pd.DataFrame(temp_list)
dataframe_list.columns=['timestamp','accelerate_x','accelerate_y','accelerate_z','gyroscope_x','gyroscope_y','gyroscope_x', 'gravity_x','gravity_y','gravity_z','magnetic_x','magnetic_y','magnetic_z','linear_accelerate_x','linear_accelerate_y','linear_accelerate_z','world_orientation_x','world_orientation_y','world_orientation_z','world_accelerometer_x','world_accelerometer_y','world_accelerometer_z','rotation_vector_x','rotation_vector_y','rotation_vector_z','game_rotation_vector_x','game_rotation_vector_y','game_rotation_vector_z','light','pressure','temperature']

usefulData =dataframe_list[['timestamp','world_accelerometer_x','world_accelerometer_y','world_accelerometer_z','world_orientation_x','world_orientation_y','world_orientation_z']]

#make plot
import matplotlib as plt



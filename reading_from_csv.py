# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 12:55:13 2020

@author: rajam
"""

import pandas as pd 
import os
# where is the file path
file_path =  os.path.abspath("D:\\py-automation\\pandas\\demos\\collection-master\\artwork_data.csv")
#print (file_path)
#print (os.getcwd())
# Now let me learn and create pandas dataframe by just learning 3 rows
usefull_columns = ["id","artist","title","medium","year","acquisitionYear","height","width","units"]
dataframe_1_reading = pd.read_csv(file_path,nrows = 3,index_col="id",usecols = usefull_columns )
#print (dataframe_1_reading)
#reading all
dataframe_2_reading = pd.read_csv(file_path,index_col="id",usecols = usefull_columns )

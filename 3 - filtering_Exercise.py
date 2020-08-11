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
#index_col means index
dataframe_1_reading = pd.read_csv(file_path,nrows = 3,index_col="id",usecols = usefull_columns )
#print (dataframe_1_reading)
#reading all
dataframe_2_reading = pd.read_csv(file_path,index_col="id",usecols = usefull_columns )
#########################
#Practicing filtering
############################

########################
#1 - row filtering using loc
########################
#1.1 - LEtS find the work done by Blake, William
# NOTE ":" represents wildcard
blake_William_work = dataframe_2_reading.loc[dataframe_2_reading["artist"] == "Blake, William",:]
#1.2 - LEtS find the work done by Blake, William on the year 1796
blake_William_work_year_1796 = blake_William_work.loc[blake_William_work["year"]=="1796"]

#######################
#2 - filtering using iloc
#######################

#2.1 - selecting value in first column and first row
first_column_and_row = dataframe_2_reading.iloc[0,0]
#2.2 - selecting value in first row and all column
first_column_all = dataframe_2_reading.iloc[0,:]
#2.3 - selecting value in fifth row and all column
fifthrow_column_all = dataframe_2_reading.iloc[4,:]
#2.4 - selecting values from the first four rows
firstfourrows_allcolumn = dataframe_2_reading.iloc[0:4,:]
#2.5 - selecting values from the first 2 rows and first 2 columns
firsttworows_firsttwocolumns = dataframe_2_reading.iloc[0:2,0:2]

##########################
# 3 - filtering columns
##########################

artistandyear = dataframe_2_reading[["artist","year"]]

########################
#4 - stats on distinct count
########################

#4.1 - finding unique artist and their unique count
artists =  dataframe_2_reading["artist"]
unique_artists = pd.unique(artists)
print(unique_artists)
print (len(unique_artists))

##########################
# 5 - checking for a condition match and store them in boolean
##########################
#5.1 - finding number of work done in the year 1825 ,1803,1794,1795
workin_year_1825 = dataframe_2_reading ["year"] == "1825"
workin_year_1825_count = workin_year_1825.value_counts()
workin_year_1803 = dataframe_2_reading ["year"] == "1803"
workin_year_1803_count = workin_year_1825.value_counts()
workin_year_1794 = dataframe_2_reading ["year"] == "1794"
workin_year_1794_count = workin_year_1794.value_counts()
workin_year_1795 = dataframe_2_reading ["year"] == "1795"
workin_year_1795_count = workin_year_1795.value_counts()

############################
# 6 doing a countby like sumologic
############################

# 6.1 doing a count by number of years and artist
count_by_years = dataframe_2_reading ["year"].value_counts()
count_by_artists = dataframe_2_reading["artist"].value_counts()

# 6.2 doing a count by years,artist

count_by_artists_years = dataframe_2_reading.groupby(["artist","year"]).size()
count_by_artists_years_2 = dataframe_2_reading.groupby(["artist","year"]).size().reset_index(name="_count")


#############################
#7 - Assigning new column with name area
#############################

area = dataframe_2_reading["height"]*dataframe_2_reading["width"]
dataframe_2_reading =  dataframe_2_reading.assign(area = area)

#############################
# Saving to excel
############################

blake_William_work.to_excel("example.xlsx")
#ignoring index
blake_William_work.to_excel("example.xlsx",index=False)
#selecting columns
blake_William_work.to_excel("example.xlsx",Columns=["artist","title"])

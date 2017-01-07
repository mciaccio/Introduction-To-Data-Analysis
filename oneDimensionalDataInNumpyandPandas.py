'''
Created on Jan 6, 2017

@author: Menfi
'''
# github colon bracket slice 

import os

import unicodecsv
#import csv

import pandas as pd

print("")

DATADIR = '/Users/Menfi/Documents/gitBaseDirectory/IntroToDataAnalysis/dataFiles'

ENGAGEMENT_FN = 'daily_engagement.csv'
ENGAGEMENT_DF = os.path.join(DATADIR, ENGAGEMENT_FN)

# Example read from disk file -> Python Dictionary -> list
# ENGAGEMENT_DF = 'daily_engagement.csv'
with open (ENGAGEMENT_DF, 'rb') as f:
    engagementReader = unicodecsv.DictReader(f)
    daily_engagement = list(engagementReader)

# print("type(daily_engagement) - {}".format(type(daily_engagement)))
# type(daily_engagement) - <class 'list'>
# print("len(daily_engagement) - {}".format(len(daily_engagement)))
#        len(daily_engagement) - 136240

# Example access part of a Python list colon bracket
print("daily_engagement[0:2] -> ")
print(daily_engagement[0:2])
print("")

# Example declare an empty set
unique_engagement_students = set()

# Example populate a Python set 
# Example get the unique accounts 
for myEngagement in daily_engagement:
    unique_engagement_students.add(myEngagement['acct'])
# print("unique_engagement_students - {}".format(unique_engagement_students))
#        unique_engagement_students - {'793', '540', '1116', '1140',
# print("len(unique_engagement_students) - {}".format(len(unique_engagement_students)))
#        len(unique_engagement_students) - 1237

# THIS TIME USE PANDAS - *** Runs faster *** - lecture notes 
# Example read a csv disk file into a Pandas DataFrame  
# Example csv file -> Pandas DataFrame
# Example create a Pandas DataFrame from a csv disk file 
daily_engagement_panda = pd.read_csv(ENGAGEMENT_DF)
# print("type(daily_engagement_panda) - {}".format(type(daily_engagement_panda)))
#        type(daily_engagement_panda) - <class 'pandas.core.frame.DataFrame'>
# print("len(daily_engagement_panda) - {}".format(len(daily_engagement_panda)))
#        len(daily_engagement_panda) - 136240

# Example create Pandas numpy.ndarray from Pandas DataFrame
# Using Pandas get the unique accounts  
daily_engagement_panda['acct'].unique()
print("daily_engagement_panda['acct'].unique() - {}".format(daily_engagement_panda['acct'].unique()))
# daily_engagement_panda['acct'].unique() - [   0    1    2 ..., 1302 1303 1305]
# print("type(daily_engagement_panda['acct'].unique()) - {}".format(type(daily_engagement_panda['acct'].unique())))
#        type(daily_engagement_panda['acct'].unique()) - <class 'numpy.ndarray'>
# print("len(daily_engagement_panda['acct'].unique()) - {}".format(len(daily_engagement_panda['acct'].unique())))
#      len(daily_engagement_panda['acct'].unique()) - 1237

myPandaArray = daily_engagement_panda['acct'].unique()
# print("type(myPandaArray) - {}".format(type(myPandaArray)))
#        type(myPandaArray) - <class 'numpy.ndarray'>

# Example, Best Example, array, colon, bracket [0:3], slice, range, give me the zeroth (first) one through the third, three total, (upper bound not inclusive)
print("myPandaArray[0:3] - {}".format(myPandaArray[0:3]))
#        myPandaArray[0:3] - [0 1 2]
# Example, Best Example, array, colon, bracket [1:3], slice, range, give me the second one (zero based indexing) through the third, two total, (upper bound not inclusive)
print("myPandaArray[1:3] - {}".format(myPandaArray[1:3]))
#      myPandaArray[1:3] - [1 2]

# Example iterate through a Panda array 
for myAcct in myPandaArray:
    # print("myAcct - {}".format(myAcct)) # works
    pass



 






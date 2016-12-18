

import os 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



print("")

DATADIR = '/Users/Menfi/Documents/gitBaseDirectory/IntroToDataAnalysis/dataFiles/twoDimensional'
SUBWAY_FN = 'nyc_subway_weather.csv'
SUBWAYFile = os.path.join(DATADIR, SUBWAY_FN) # string

# Build a NumPy Array First Python list
myList = [1, 3, 2, 4, 1, 6, 4]
print("myList - {}".format(myList))
print("")
# print("type(myList) - {}".format(type(myList)))
# type(myList) - <class 'list'>

# Build the Numpy Array from the Python list
myNumPyArray = np.array(myList)
print("myNumPyArray - {}".format(myNumPyArray))
# print("type(myNumPyArray) - {}".format(type(myNumPyArray)))
# type(myNumPyArray) - <class 'numpy.ndarray'>
print("")

# values = np.array([1, 3, 2, 4, 1, 6, 4]) # udacity example
# print("values - {}".format(values))
# print("type(values) - {}".format(type(values)))
# type(values) - <class 'numpy.ndarray'>

# Populate the values variable with the NumPy Array
values = np.array(myNumPyArray) # MGC
print("values - {}".format(values))
print("")
# print("type(values) - {}".format(type(values)))
# type(values) - <class 'numpy.ndarray'>

# Populate Pandas DataFrame with NumPy Array
# DataFrame column reference another column
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

print("example_df -> ")
print(example_df)
# print("type(example_df) - {}".format(type(example_df)))
#type(example_df) - <class 'pandas.core.frame.DataFrame'>
print("")

# Examine groups group by the 'even' column
# returns Python Dictionary
grouped_data = example_df.groupby('even')
# The groups attribute is a dictionary mapping keys to lists of row indexes
print ("grouped_data.groups 'even' -> ")
print (grouped_data.groups)
# {False: ['a', 'b', 'e'], True: ['c', 'd', 'f', 'g']}
# print("type(grouped_data.groups) - {}".format(type(grouped_data.groups)))
# type(grouped_data.groups) - <class 'dict'>
# gives insight into what is going on, debugging tool
print("")

grouped_data.sum()
print("grouped_data.sum() 'even' -> ")
# print(grouped_data.groups) - gives insight into what is going on, debugging tool
# {False: ['a', 'b', 'e'], True: ['c', 'd', 'f', 'g']}
print(grouped_data.sum())
"""
grouped_data.sum() 'even' -> 
       above_three  value                                  ***
even                        -> even - example_df.groupby('even')
False          0.0      5
True           3.0     16
total count of even False - (odds!) (1,3,1)   - above_three = 0, sum of value = 1+3+1   = 5
total count of even True  - (evens) (2,4,6,4) - above_three = 3, sum of value = 2+4+6+4 = 16
"""
print("")

# Just get the specified column - value 
print ("print grouped_data.sum()['value'] ->")
print (grouped_data.sum()['value'])
"""
even            -> even - example_df.groupby('even')
False     5     -> even False - (odds!) (1,3,1)   - sum of value = 1+3+1   = 5
True     16     -> even True  - (evens) (2,4,6,4) - sum of value = 2+4+6+4 = 16
Name: value, dtype: int64
"""

print("")

# print grouped_data['value'].sum() - instructor 
print ("grouped_data['value'].sum() ->")
print (grouped_data['value'].sum())
print("")

# Group by multiple columns
# DataFrame value column - values
# DataFrame even column - criteria
# DataFrame above_three column - criteria
# find values that meet BOTH criteria, neither criter ia etc 
grouped_data = example_df.groupby(['even', 'above_three'])
print ("grouped_data 'even', 'above_three' -> ")
# print (grouped_data)
# <pandas.core.groupby.DataFrameGroupBy object at 0x11207fba8>
# print("type(grouped_data) - {}".format(type(grouped_data)))
# type(grouped_data) - <class 'pandas.core.groupby.DataFrameGroupBy'>
print (grouped_data.groups)
# gives insight into what is going on, debugging tool
# {(True, False): ['c'], (False, False): ['a', 'b', 'e'], (True, True): ['d', 'f', 'g']}
#print("type(grouped_data.groups) - {}".format(type(grouped_data.groups)))
# type(grouped_data.groups) - <class 'dict'>
print("")

# ***
# *** begin subway CSV File
# ***

# read csv file into a Pandas dataFrame 
subwayPandasDataFrame = pd.read_csv(SUBWAYFile)

"""
print("type(subwayPandasDataFrame) - {}".format(type(subwayPandasDataFrame)))
type(subwayPandasDataFrame) - <class 'pandas.core.frame.DataFrame'>
"""

# head() of a DataFrame - similar to unix head, tail etc 
print("subwayPandasDataFrame.head() -> ")
print(subwayPandasDataFrame.head())
print("")

# generate a small Pandas DataFrame from the csv file for development, testing
partialSubwayFile = pd.read_csv(SUBWAYFile,nrows=6)
print("partialSubwayFile -> ")
print(partialSubwayFile)
print("partialSubwayFile.describe -> ")
print(partialSubwayFile.describe)
print("")

#

subwayPandasDataFrame_grouped_unit = subwayPandasDataFrame.groupby(['UNIT'])
print("")
print("subwayPandasDataFrame_grouped_unit -> ")
print(subwayPandasDataFrame_grouped_unit)
#<pandas.core.groupby.DataFrameGroupBy object at 0x11307f6a0>
print("")

# groups - get the applicable rows
# rows associated with the 'UNIT'
# print("subwayPandasDataFrame_grouped_unit.groups -> ")
# print(subwayPandasDataFrame_grouped_unit.groups)
#<pandas.core.groupby.DataFrameGroupBy object at 0x11307f6a0>

# print (subwayPandasDataFrame_grouped_unit.sum())
print("157..........................")
#print (subwayPandasDataFrame_grouped_unit.sum()['rain'])
print (subwayPandasDataFrame_grouped_unit.sum()['rain'])
print (subwayPandasDataFrame_grouped_unit['rain', 'ENTRIESn', 'ENTRIESn_hourly', 'meanwspdi'].sum()) 
print("161")


"""
instructor - group the subway data by the day of the week
groupby method (['day_week'] of the class 'pandas.core.frame.DataFrame'
returns - class 'pandas.core.groupby.DataFrameGroupBy

print("type(subwayPandasDataFrame) - {}".format(type(subwayPandasDataFrame)))
       type(subwayPandasDataFrame) - <class 'pandas.core.frame.DataFrame'>
print("type(subwayPandasDataFrame.groupby) - {}".format(type(subwayPandasDataFrame.groupby)))
       type(subwayPandasDataFrame.groupby) - <class 'method'>
"""
subwayPandasDataFrame_groupedby_dayWeek = subwayPandasDataFrame.groupby(['day_week'])
"""
print("type(subwayPandasDataFrame_groupedby_dayWeek) - {}".format(type(subwayPandasDataFrame_groupedby_dayWeek)))
type(subwayPandasDataFrame_groupedby_dayWeek) - <class 'pandas.core.groupby.DataFrameGroupBy'>
"""

"""
mean for each numeric variable for each day of week
""" 
print ("subwayPandasDataFrame_groupedby_dayWeek.mean() -> ")
print (subwayPandasDataFrame_groupedby_dayWeek.mean())
print("")

"""
mean for just the ['ENTRIESn_hourly'] data 
both work
Series not a DataFrame 
print("type(subwayPandasDataFrame_groupedby_dayWeek['ENTRIESn_hourly'].mean()) - {}".format(type(subwayPandasDataFrame_groupedby_dayWeek['ENTRIESn_hourly'].mean())))
type(subwayPandasDataFrame_groupedby_dayWeek['ENTRIESn_hourly'].mean()) - <class 'pandas.core.series.Series'>
"""
print ("subwayPandasDataFrame_groupedby_dayWeek.mean() -> ")
print (subwayPandasDataFrame_groupedby_dayWeek.mean()['ENTRIESn_hourly']) # works
print (subwayPandasDataFrame_groupedby_dayWeek['ENTRIESn_hourly'].mean()) # works
print("")

"""
csv -> DataFrame -> groupby(['day_week']
"""
ridership_by_day = subwayPandasDataFrame_groupedby_dayWeek['ENTRIESn_hourly'].mean()
print ("ridership_by_day -> ")
print (ridership_by_day)
"""
print("type(ridership_by_day) - {}".format(type(ridership_by_day)))
type(ridership_by_day) - <class 'pandas.core.series.Series'>
"""
print("")

"""
plot() method series class 
print("type(ridership_by_day.plot()) - {}".format(type(ridership_by_day.plot())))
type(ridership_by_day.plot()) - <class 'matplotlib.axes._subplots.AxesSubplot'>

print("type(plt.show()) - {}".format(type(plt.show())))
type(plt.show()) - <class 'NoneType'>
"""

"""
plotting DataFrame -> Series data - working example
"""
ridership_by_day.plot()
plt.ylabel('mean subway ridership')
plt.show()

x = 5
print("x - {}".format(x))
print("type(x) - {}".format(type(x)))
print("")

print("x -> ")
print(x)
print("")
print("type(x) - {}".format(type(x)))
print("")



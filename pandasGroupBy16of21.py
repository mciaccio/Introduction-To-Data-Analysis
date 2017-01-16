'''
Created on Jan 15, 2017

@author: Menfi
'''

# github *** DataFrameGroupBy object ***, *** .groups - understand what is going on *** make plots, matplotlib, seaborn

print("\nBegin\n")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# Change False to True for each block of code to see what it does

# Examine DataFrame
if True:
    # print("type(values) - {}".format(type(values)))
    # type(values) - <class 'numpy.ndarray'>

    # print("type(example_df) - {}".format(type(example_df)))
    # type(example_df) - <class 'pandas.core.frame.DataFrame'>

    # print example_df
    print("example_df -> ")
    print(example_df)
    print("")
    
# Examine groups
# Example - group the data then print the groups - get some idea what is going on 
if False :
    grouped_data = example_df.groupby('even')
    # Example - *** DataFrameGroupBy object *** groups insight into what is going on 
    # print("type(grouped_data) - {}".format(type(grouped_data)))
    # type(grouped_data) - <class 'pandas.core.groupby.DataFrameGroupBy'>

    # The groups attribute is a dictionary mapping keys to lists of row indexes
    # print grouped_data.groups
    print("grouped by 'even' - grouped_data.groups -> ")
    print(grouped_data.groups)
    # print("type(grouped_data.groups) - {}".format(type(grouped_data.groups)))
    # type(grouped_data.groups) - <class 'dict'>
    # Example - *** groupby('even') *** only two cases True and false - here we see the grouping based on these two cases - the indexes of even True, or even False
    # {False: ['a', 'b', 'e'], True: ['c', 'd', 'f', 'g']}
    print("")
    
# Group by multiple columns
# Example - group Pandas DataFrame by multiple columns
if False:
    grouped_data = example_df.groupby(['even', 'above_three'])
    print("type(grouped_data) - {}".format(type(grouped_data)))
    # type(grouped_data) - <class 'pandas.core.groupby.DataFrameGroupBy'>

    # print grouped_data.groups
    # Example - 6 is BOTH even and above 3 - (True, True) - f the index of 6, groups - insight into what is going on 
    print("grouped_data.groups -> ")
    print(grouped_data.groups)
    print("")
    
# Get sum of each group
if False:
    # Explanation - none above three that were not even - odd
    grouped_data = example_df.groupby('even')
    print("grouped_data.groups -> ")
    print(grouped_data.groups)
    print("")
    
    # print grouped_data.sum()
    print("grouped by even - grouped_data.sum() -> ")
    print(grouped_data.sum())
    print("")
    
# Limit columns in result
# Example *** two ways to sum *** 
if False:
    grouped_data = example_df.groupby('even')
    
    # You can take one or more columns from the result DataFrame
    # print grouped_data.sum()['value']
    print("grouped_data.sum()['value'] -> ")
    print(grouped_data.sum()['value'])
    # print("type(grouped_data.sum()['value']) - {}".format(type(grouped_data.sum()['value'])))
    #        type(grouped_data.sum()['value']) - <class 'pandas.core.series.Series'>

    print("")
    
    # print '\n' # Blank line to separate results
    
    # You can also take a subset of columns from the grouped data before 
    # collapsing to a DataFrame. In this case, the result is the same.
    # print grouped_data['value'].sum()
    print("grouped_data['value'].sum() -> ")
    print(grouped_data['value'].sum())
    # print("type(grouped_data['value'].sum()) - {}".format(type(grouped_data['value'].sum())))
    #        type(grouped_data['value'].sum()) - <class 'pandas.core.series.Series'>
    print("")
    
# filename = '/datasets/ud170/subway/nyc_subway_weather.csv'
filename = '/Users/Menfi/Documents/gitBaseDirectory/IntroToDataAnalysis/dataFiles/twoDimensional/nyc_subway_weather.csv'
# filename = '/Users/Menfi/Documents/gitBaseDirectory/IntroToDataAnalysis/dataFiles/twoDimensional/shorter'
subway_df = pd.read_csv(filename)
# print("type(subway_df) - {}".format(type(subway_df)))
# type(subway_df) - <class 'pandas.core.frame.DataFrame'>

### Write code here to group the subway data by a variable of your choice, then
### either print out the mean ridership within each group or create a plot.
# print("subway_df -> ")
# print(subway_df)
# print("")

grouped_data = subway_df.groupby('day_week')
# print("type(grouped_data) - {}".format(type(grouped_data)))
# type(grouped_data) - <class 'pandas.core.groupby.DataFrameGroupBy'>

# print("grouped_data.groups -> ")
# print(grouped_data.groups)
# print("")

# Example - sum all columns that can be summed, integers etc
# print("grouped_data.sum() -> ")
# print(grouped_data.sum())
# print("")

# Limit columns in result
# Example - sum specified column - ENTRIESn
# print("grouped_data.sum()['ENTRIESn'] -> ")
# print(grouped_data.sum()['ENTRIESn'])
# print("")
ridershipDayOfWeek = grouped_data.sum()['ENTRIESn']

# print("type(ridershipDayOfWeek) - {}".format(type(ridershipDayOfWeek)))
# type(ridershipDayOfWeek) - <class 'pandas.core.series.Series'>

# Example - simple Pandas Series working plot 
ridershipDayOfWeek.plot(kind = 'bar')
plt.show() # required !!

print("\nEnd\n")

'''
Created on Jan 19, 2017

@author: Menfi
'''

# github scatter plot, DataFrame, groupby,  as_index=False

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import pylab # scatter plot, fix scatter plot will not show or render
 
print("\nBegin\n")


# Example - create, instantiate, populate Pandas DataFrame, NumPy array -> Pandas DataFrame, with index 
values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# Change False to True for this block of code to see what it does

# groupby() without as_index
if True:
    print("example_df -> ")
    print(example_df)
    # print("type(example_df) - {}".format(type(example_df)))
    # type(example_df) - <class 'pandas.core.frame.DataFrame'>
    print("")

    example_dfGroupbyEven = example_df.groupby('even')
    # print example_dfGroupbyEven not much help
    # print("example_dfGroupbyEven -> ")
    # print(example_dfGroupbyEven) # groupby not much help 
    # <pandas.core.groupby.DataFrameGroupBy object at 0x10ae9c940>
    # print("type(example_dfGroupbyEven) - {}".format(type(example_dfGroupbyEven)))
    #        type(example_dfGroupbyEven) - <class 'pandas.core.groupby.DataFrameGroupBy'>
    # print("")
    
    print("example_dfGroupbyEven.groups -> ")
    print(example_dfGroupbyEven.groups) # groupby some help
    # {False: ['a', 'b', 'e'], True: ['c', 'd', 'f', 'g']}
    # print("type(example_dfGroupbyEven.groups) - {}".format(type(example_dfGroupbyEven.groups)))
    #        type(example_dfGroupbyEven.groups) - <class 'dict'>
    print("")
    
    list(example_dfGroupbyEven) 
    print("list(example_dfGroupbyEven) -> ")
    print(list(example_dfGroupbyEven)) # groupby more helpful 
    # print("type(list(example_dfGroupbyEven)) - {}".format(type(list(example_dfGroupbyEven))))
    #        type(list(example_dfGroupbyEven)) - <class 'list'>

    print("")
    
    first_even = example_df.groupby('even').first()
    # print first_even
    print("first_even -> ")
    print(first_even)
    # print("type(first_even) - {}".format(type(first_even)))
    #        type(first_even) - <class 'pandas.core.frame.DataFrame'>
    print("")
    
    
    # first_even -> 
    #            above_three      value   *** big deal 'even' is not a column, as_index=False NOT used, see fix below ***
    # even                    
    # False      False            1
    # True       False            2

    # Example - error 'even' no longer column in DataFrame  
    # print first_even['even'] # Causes an error. 'even' is no longer a column in the DataFrame
    # print("first_even -> ")
    # print(first_even['even'])
    # print("type(first_even['even']) - {}".format(type(first_even['even'])))
    # print("")
    
    # groupby *** as_index=False used fix ***
    first_even1 = example_df.groupby('even', as_index=False).first()    
    print("first_even1 -> ")
    print(first_even1)
    # print("type(first_even1) - {}".format(type(first_even1))) # Note - type - DataFrame 
    # type(first_even1) - <class 'pandas.core.frame.DataFrame'>
    print("")
    
#     first_even1 -> 
#         even    above_three value # *** big deal as_index=False used, 'even' STILL a column name 
#     0   False   False       1
#     1   True    False       2


# groupby() with as_index=False
if False:
    first_even = example_df.groupby('even', as_index=False).first()
    # print first_even
    print("first_even -> ")
    print(first_even)
    print("type(first_even) - {}".format(type(first_even)))
    print("")
    
    # print first_even['even'] # Now 'even' is still a column in the DataFrame
    print("first_even['even'] -> ")
    print(first_even['even'])
    print("type(first_even['even']) - {}".format(type()))
    print("")

# Example - read csv file into a DataFrame, csv -> DataFrame 
# filename = '/datasets/ud170/subway/nyc_subway_weather.csv'
filename = '/Users/Menfi/Documents/gitBaseDirectory/IntroToDataAnalysis/dataFiles/twoDimensional/nyc_subway_weather.csv'
# filename = '/Users/Menfi/Documents/gitBaseDirectory/IntroToDataAnalysis/dataFiles/twoDimensional/shorter'
subway_df = pd.read_csv(filename)

## Make a plot of your choice here showing something interesting about the subway data.
## Matplotlib documentation here: http://matplotlib.org/api/pyplot_api.html
## Once you've got something you're happy with, share it on the forums!

print("subway_df -> ")
print(subway_df)
print("type(subway_df) - {}".format(type(subway_df)))
print("")

# plt.scatter(subway_df.weather.lat, subway_df.weather.lon)
# Example accessing *** DataFrame *** columns using *** dot notation ***
print("subway_df.latitude -> ")
print(subway_df.latitude)
print("")

print("subway_df.longitude -> ")
print(subway_df.latitude)
# print("type(subway_df.longitude) - {}".format(type(subway_df.longitude)))
#        type(subway_df.longitude) - <class 'pandas.core.series.Series'>
print("")
  
# plt.scatter(subway_df.latitude, subway_df.longitude) # scatterplot WORKS 
# plt.show()

# Example groupby, 2, two column names 
data_by_location = subway_df.groupby(['latitude', 'longitude'])
print("data_by_location.groups -> ")
print(data_by_location.groups)
# print("type(data_by_location) - {}".format(type(data_by_location)))
#        type(data_by_location) - <class 'pandas.core.groupby.DataFrameGroupBy'>
print("")

print("list(data_by_location.groups) -> ")
print(list(data_by_location.groups))
# print("type(list(data_by_location.groups)) - {}".format(type(list(data_by_location.groups))))
#        type(list(data_by_location.groups)) - <class 'list'>
print("")

# Example - as_index = False groupby keep column names, groupby 2, two column names  
data_by_location_mean = subway_df.groupby(['latitude', 'longitude'], as_index = False).mean()
print("data_by_location_mean -> ")
print(data_by_location_mean)
# print("type(data_by_location_mean)) - {}".format(type(data_by_location_mean)))
#        type(data_by_location_mean)) - <class 'pandas.core.frame.DataFrame'>
print("")

print("data_by_location_mean['latitude'] -> ")
print(data_by_location_mean['latitude'])
print("type(data_by_location_mean['latitude'])) - {}".format(type(data_by_location_mean['latitude'])))
# type(data_by_location_mean['latitude'])) - <class 'pandas.core.series.Series'>
print("")

print("data_by_location_mean['longitude'] -> ")
print(data_by_location_mean['longitude'])
print("type(data_by_location_mean['longitude'])) - {}".format(type(data_by_location_mean['longitude'])))
# type(data_by_location_mean['latitude'])) - <class 'pandas.core.series.Series'>
print("")

#Example - fix scatter plot dot size, dots too big otherwise  
scaledEntries = data_by_location_mean['ENTRIESn_hourly'] / data_by_location_mean['ENTRIESn_hourly'].std()
print("scaledEntries -> ")
print(scaledEntries)
print("type(scaledEntries) - {}".format(type(scaledEntries)))
print("")

# plt.scatter(data_by_location_mean['latitude'], data_by_location_mean['longitude'])
plt.scatter(data_by_location_mean['latitude'], data_by_location_mean['longitude'], s = scaledEntries) # scatter plot WORKS
# plt.scatter(subway_df.latitude, subway_df.longitude) # scatterplot WORKS 
# Example - Fixed nasty scatter plot not rendering, not showing up 
pylab.show()

print("\nEnd\n")



"""
github - diff() AND shift(1) - same result numpy, pandas, ndarray, DataFrame iterating looping through Pandas groupby objects DataFrameGroupBy SeriesGroupBy 
"""

import numpy as np
import pandas as pd

def standardize(pandasSeries_xs):
    print("Begin standardize(pandasSeries_xs)")
    print("pandasSeries_xs -> ")
    print(pandasSeries_xs)
    print("")
    """
    print("type(pandasSeries_xs) - {}".format(type(pandasSeries_xs)))
           type(pandasSeries_xs) - <class 'pandas.core.series.Series'>
    """
    
    seriesMean = pandasSeries_xs.mean()
    print("seriesMean - {}".format(seriesMean))
    # seriesMean - 4.0
    """
    print("type(seriesMean) - {}".format(type(seriesMean)))
           type(seriesMean) - <class 'float'>
    """
    
    seriesStd = pandasSeries_xs.std()
    print("seriesStd - {}".format(seriesStd))
    """
    print("type(seriesStd) - {}".format(type(seriesStd)))
           type(seriesStd) - <class 'float'>
    """
    
    standardizedSeriesValues = (pandasSeries_xs - seriesMean) / seriesStd
    print("End standardize(pandasSeries_xs)\n")

    return standardizedSeriesValues
#    return (pandasSeries_xs - pandasSeries_xs.mean()) / pandasSeries_xs.std()

def second_largest(xsSeries):
    """
    iterated through TWICE for each call to this function
    once for the Series True key and once for the Series False key.
    """
    print("Begin second_largest function")
    
    print("xsSeries -> ")
    print(xsSeries)
    print("")
    
    """
    print("type(xsSeries) - {}".format(type(xxsSeries))
           type(xsSeries) - <class 'pandas.core.series.Series'>
    """

    sorted_xs = xsSeries.sort_values(inplace=False, ascending=False)
    
    print("sorted_xs -> ")
    print(sorted_xs)
    
    print("")
    
    """
    print("type(sorted_xs) - {}".format(type(sorted_xs)))
           type(sorted_xs) - <class 'pandas.core.series.Series'>
    """
    
    # example .iloc dot iloc - used to access class 'pandas.core.series.Series' elements
    # example .iloc used to access Pandas Series elements 
    secondLargest = sorted_xs.iloc[1]        
    print("secondLargest - {}".format(secondLargest))
    print("")
    
    """
    print("type(secondLargest) - {}".format(type(secondLargest)))
           type(secondLargest) - <class 'numpy.int64'>
    """
    print("End second_largest function")

    return sorted_xs.iloc[1]

print("")


values = np.array([1, 3, 2, 4, 1, 6, 4])
"""
print("type(values) - {}".format(type(values)))
type(values) - <class 'numpy.ndarray'>
populate DataFrame keys with numpy.ndarray (np.array)
"""

example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
"""
print("type(example_df) - {}".format(type(example_df)))
type(example_df) - <class 'pandas.core.frame.DataFrame'>
"""


print("example_df DataFrame-> ")
print(example_df)
print("")
"""
print("type(example_df) - {}".format(type(example_df)))
type(example_df) - <class 'pandas.core.frame.DataFrame'>
"""

"""
even - 'even': values % 2 == 0 - resolves to either True or False 
keys of  DataFrameGroupBy Python Dictionary - True, False
groupby('even') - all even values are associated with the True Key
groupby('even') - all odd values are associated with the False Key
"""
grouped_data_even = example_df.groupby('even')

"""
print("type(grouped_data_even) - {}".format(type(grouped_data_even)))
type(grouped_data_even) - <class 'pandas.core.groupby.DataFrameGroupBy'>
"""

print("grouped_data_even.groups -> ")
print(grouped_data_even.groups)
# {False: ['a', 'b', 'e'], True: ['c', 'd', 'f', 'g']}
print("")

"""
print, output, dump DataFrameGroupBy object
First get the corresponding Python Dictionary
"""
groups_even = dict(list(grouped_data_even))
"""
print("type(groups_even) - {}".format(type(groups_even)))
type(groups_even) - <class 'dict'>

iterate, loop through the Python Dictionary representation of the Pandas DataFrameGroupBy object
"""
print ("grouped_data_even - DataFrameGroupBy -> ")
for key in groups_even:
    # print key, 'corresponds to', d[key]
    #print("key -> {} - group -> {}".format(key, groups[key] ))
    print("KEY - {}".format(key))
    print(groups_even[key])
    
print("")  
"""
print("type(grouped_data_even['value']) - {}".format(type(grouped_data_even['value'])))
       type(grouped_data_even['value']) - <class 'pandas.core.groupby.SeriesGroupBy'>
"""
print("grouped_data_even['value'].groups -> ")
print(grouped_data_even['value'].groups)
print("")

"""
print, output, dump SeriesGroupBy object
First get the corresponding Python Dictionary
"""
valueObject = dict(list(grouped_data_even['value']))
"""
iterate, loop through the Python Dictionary representation of the Pandas SeriesGroupBy object
"""
print ("grouped_data_even['value'] - SeriesGroupBy -> ")
for key in valueObject:
    # print key, 'corresponds to', d[key]
    #print("key -> {} - group -> {}".format(key, groups[key] ))
    print("KEY - {}".format(key))
    print(valueObject[key])
print("")

"""
called twice once for each key in the
class 'pandas.core.groupby.SeriesGroupBy' - the True key and the False key  
"""

"""
standardizedValues = grouped_data_even['value'].apply(standardize)
print("standardizedValues -> ")
print(standardizedValues)
"""

"""
print("type(standardizedValues) - {}".format(type(standardizedValues)))
       type(standardizedValues) - <class 'pandas.core.series.Series'>
"""

"""
the second_largest function is applied to 
<class 'pandas.core.groupby.SeriesGroupBy'>
The <class 'pandas.core.groupby.SeriesGroupBy'> has two keys True  and False
The <class 'pandas.core.groupby.SeriesGroupBy'> was created as follows: 
grouped_data_even = example_df.groupby('even')
The even column had 2 distinct entries True and False
The value(s) associated with the True  key are the even values
The value(s) associated with the False key are the odd values
The second_largest function is called or applied twice each time
Once for the True key and once for the false key 
"""
# secondLargest = grouped_data_even['value'].apply(second_largest)


# --- Quiz ---
# DataFrame with cumulative entries and exits for multiple stations

ridership_df = pd.DataFrame({
    'UNIT': ['R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051'],
    'TIMEn': ['00:00:00', '02:00:00', '04:00:00', '06:00:00', '08:00:00', '10:00:00', '12:00:00', '14:00:00', '16:00:00'],
    'ENTRIESn': [3144312, 8936644, 3144335, 8936658, 3144353, 8936687, 3144424, 8936819, 3144594],
    'EXITSn': [1088151, 13755385,  1088159, 13755393,  1088177, 13755598, 1088231, 13756191,  1088275]
})

"""
get rid of TIMEn - DataFrame - DataFrame.shift(1) will work
get rid of string, can't subtract strings
"""

ridership_df1 = pd.DataFrame({
#    'UNIT': ['R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051'],
#    'TIMEn': ['00:00:00', '02:00:00', '04:00:00', '06:00:00', '08:00:00', '10:00:00', '12:00:00', '14:00:00', '16:00:00'],
    'ENTRIESn': [3144312, 8936644, 3144335, 8936658, 3144353, 8936687, 3144424, 8936819, 3144594],
    'EXITSn': [1088151, 13755385,  1088159, 13755393,  1088177, 13755598, 1088231, 13756191,  1088275]
})

def get_hourly_entries_and_exits(entries_and_exits):
    '''
    Fill in this function to take a DataFrame with cumulative entries
    and exits and return a DataFrame with hourly entries and exits.
    The hourly entries and exits should be calculated separately for
    each station (the 'UNIT' column).
    
    Hint: Use the `get_hourly_entries_and_exits()` function you wrote
    in a previous quiz, DataFrame Vectorized Operations, and the `.apply()`
    function, to help solve this problem.
    '''
    
    print("Begin get_hourly_entries_and_exits\n")

    """
    Print the original DataFrame
    """
    print("entries_and_exits DataFrame -> ")
    print(entries_and_exits)
    print("")
    """
    print("type(entries_and_exits) - {}".format(type(entries_and_exits)))
           type(entries_and_exits) - <class 'pandas.core.frame.DataFrame'>
    """
    
    """
    create DataFrameGroupBy object - groupby "UNIT"
    associate DataFrame rows with the corresponding "UNIT" 
    """
    UNIT_groupby = entries_and_exits.groupby("UNIT")
    """
    print("type(UNIT_groupby) - {}".format(type(UNIT_groupby)))
    type(UNIT_groupby) - <class 'pandas.core.groupby.DataFrameGroupBy'>
    
    print(" -> UNIT_groupby.groups")
    print(UNIT_groupby.groups)
    {'R079': [1, 3, 5, 7], 'R051': [0, 2, 4, 6, 8]}
    
    print("type(UNIT_groupby.groups) - {}".format(type(UNIT_groupby.groups)))
           type(UNIT_groupby.groups) - <class 'dict'>
    """
    
    """
    UNIT_groupby information - developer, development, troubleshooting, debugging 
    get dump print DataFrame groupby object - first create a Python Dictionary
    """    
    UNIT_groupbyDictionary = dict(list(UNIT_groupby))

    """
    Next loop, iterate through the Python Dictionary
    The "UNIT" list of the original DataFrame has two unique values 
    'UNIT': ['R051', 'R079'
    groupby("UNIT") - generates two unique keys in the Dictionary 'R051', 'R079'
    The values of those keys are the DatFrame rows that corrspond to the "UNIT" value keys
    
    """
    for key in UNIT_groupbyDictionary:
        print("key\t- {}".format(key))
        print("UNIT_groupbyDictionary[key] -> ")
        print(UNIT_groupbyDictionary[key])
        print("")
    
    """
    print("type(UNIT_groupby.shift(1)) - {}".format(type(UNIT_groupby.shift(1))))
    type(UNIT_groupby.shift(1)) - <class 'pandas.core.frame.DataFrame'>
    """
    
    """
    strings removed can't subtract strings
    """
    print("original DataFrame strings removed - ridership_df1 DataFrame -> ")
    print(ridership_df1)
    print("")
    print("original DataFrame strings removed shift(1) shifted - drop row by 1 - ridership_df1.shift(1) -> ") # top row zeroth row Nan
    print(ridership_df1.shift(1))
    print("")
    print("ridership_df1 - ridership_df1.shift(1)")
    print(ridership_df1 - ridership_df1.shift(1))
    print("")
    
    """
    Two instructor solutions 
    DataFrame.diff() and (DataFrame - DataFrame.shift(1)) - SAME result - Two instructor solutions 
    """
    print("ridership_df1.diff() -> ")
    print(ridership_df1.diff())
    print("")
    
    
    
                                            
    
    print("End get_hourly_entries_and_exits")
    
    return None

def getHourly(df):
    x = df.diff()
    
    print("324x - >")
    print(x)
    print("")
    



get_hourly_entries_and_exits(ridership_df)

"""
how to access part of a DataFrame 'ENTRIESn', 'EXITSn' - combined with groupby 
"""
ridership_df.groupby('UNIT')[['ENTRIESn', 'EXITSn']].apply(getHourly)


print("")
 
x = 5
print("x - {}".format(x))
print("type(x) - {}".format(type(x)))
print("")

print("x -> ")
print(x)
print("")
print("type(x) - {}".format(type(x)))
print("")

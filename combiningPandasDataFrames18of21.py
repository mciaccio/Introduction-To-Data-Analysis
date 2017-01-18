'''
Created on Jan 18, 2017

@author: Menfi
'''

# github  = DataFrame, DataFrames - groupby multiple columns, merge multiple columns
# Example - DataFrame groupby 2, two column headings *** subwayCSVDataFrame.groupby(['latitude', 'longitude'], as_index = False) ***

# submissions.merge(enrollments, on='account_key', how = 'left')
# inner - only rows with account keys in both tables kept *** used here see below ***
# outer - all rows from both tables kept 
# right - rows from right hand table, enrollments, would have been kept even if no matching entry in the submissions table
# left - rows present in left table, not present in right table kept

print("\nBegin\n")

import pandas as pd

subway_df = pd.DataFrame({
    'UNIT': ['R003', 'R003', 'R003', 'R003', 'R003', 'R004', 'R004', 'R004',
             'R004', 'R004'],
    'DATEn': ['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
              '05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11'],
    'hour': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'ENTRIESn': [ 4388333,  4388348,  4389885,  4391507,  4393043, 14656120,
                 14656174, 14660126, 14664247, 14668301],
    'EXITSn': [ 2911002,  2911036,  2912127,  2913223,  2914284, 14451774,
               14451851, 14454734, 14457780, 14460818],
    'latitude': [ 40.689945,  40.689945,  40.689945,  40.689945,  40.689945,
                  40.69132 ,  40.69132 ,  40.69132 ,  40.69132 ,  40.69132 ],
    'longitude': [-73.872564, -73.872564, -73.872564, -73.872564, -73.872564,
                  -73.867135, -73.867135, -73.867135, -73.867135, -73.867135]
})

weather_df = pd.DataFrame({
    'DATEn': ['05-01-11', '05-01-11', '05-02-11', '05-02-11', '05-03-11',
              '05-03-11', '05-04-11', '05-04-11', '05-05-11', '05-05-11'],
    'hour': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'latitude': [ 40.689945,  40.69132 ,  40.689945,  40.69132 ,  40.689945,
                  40.69132 ,  40.689945,  40.69132 ,  40.689945,  40.69132 ],
    'longitude': [-73.872564, -73.867135, -73.872564, -73.867135, -73.872564,
                  -73.867135, -73.872564, -73.867135, -73.872564, -73.867135],
    'pressurei': [ 30.24,  30.24,  30.32,  30.32,  30.14,  30.14,  29.98,  29.98,
                   30.01,  30.01],
    'fog': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'rain': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'tempi': [ 52. ,  52. ,  48.9,  48.9,  54. ,  54. ,  57.2,  57.2,  48.9,  48.9],
    'wspdi': [  8.1,   8.1,   6.9,   6.9,   3.5,   3.5,  15. ,  15. ,  15. ,  15. ]
})

# This time 'date' does not match 'DATEn'
weatherDifferent_df = pd.DataFrame({
    'date': ['05-01-11', '05-01-11', '05-02-11', '05-02-11', '05-03-11',
              '05-03-11', '05-04-11', '05-04-11', '05-05-11', '05-05-11'],
    'hour': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'latitude': [ 40.689945,  40.69132 ,  40.689945,  40.69132 ,  40.689945,
                  40.69132 ,  40.689945,  40.69132 ,  40.689945,  40.69132 ],
    'longitude': [-73.872564, -73.867135, -73.872564, -73.867135, -73.872564,
                  -73.867135, -73.872564, -73.867135, -73.872564, -73.867135],
    'pressurei': [ 30.24,  30.24,  30.32,  30.32,  30.14,  30.14,  29.98,  29.98,
                   30.01,  30.01],
    'fog': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'rain': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'tempi': [ 52. ,  52. ,  48.9,  48.9,  54. ,  54. ,  57.2,  57.2,  48.9,  48.9],
    'wspdi': [  8.1,   8.1,   6.9,   6.9,   3.5,   3.5,  15. ,  15. ,  15. ,  15. ]
})


def combine_dfs(subway_df, weather_df):
    '''
    Fill in this function to take 2 DataFrames, one with subway data and one with weather data,
    and return a single dataframe with one row for each date, hour, and location. Only include
    times and locations that have both subway data and weather data available.
    '''

    print("subway_df -> ")
    print(subway_df)
    # print("type(subway_df) - {}".format(type(subway_df)))
    # type(subway_df) - <class 'pandas.core.frame.DataFrame'>
    print("")

    # I thought grouping of both DataFrames going into the merge was required.  The instructor solution did not do this. 
    # subwayGrouped = subway_df.groupby('UNIT') 
    # subwayGrouped = subway_df.groupby(['UNIT'])
    # Example - not needed here, but, working example, group by two, 2 columns, column names, groupby multiple columns 
    # subwayGrouped = subway_df.groupby(['UNIT', 'DATEn', 'hour']) 
    # groupby(['latitude', 'longitude'], as_index = False)
        
    # Not useful 
    # print("subwayGrouped -> ")
    # print(subwayGrouped)
    # <pandas.core.groupby.DataFrameGroupBy object at 0x1118901d0>
    # print("type(subwayGrouped) - {}".format(type(subwayGrouped)))
    #        type(subwayGrouped) - <class 'pandas.core.groupby.DataFrameGroupBy'>
    # print("")

    # groupby groups - somewhat useful 
    # print("subwayGrouped.groups -> ")
    # print(subwayGrouped.groups)
    # {'R003': [0, 1, 2, 3, 4], 'R004': [5, 6, 7, 8, 9]}
    # print("")
    
    # groupby - Not very useful
    # print("list(subwayGrouped.groups)) -> ")
    # print(list(subwayGrouped.groups))
    # ['R004', 'R003']
    # print("")
    
    # groupby - more useful 
    # print("list(subwayGrouped)) -> ")
    # print(list(subwayGrouped))
    # print("")
    
    print("weather_df -> ")
    print(weather_df)
    # print("type(weather_df) - {}".format(type(weather_df)))
    # type(weather_df) - <class 'pandas.core.frame.DataFrame'>
    print("")
    
    # I thought grouping of both DataFrames going into the merge was required.  The instructor solution did not do this. 
    # Example - not needed here, but, working example, group by two, 2 columns, column names 
    # weatherGrouped = weather_df.groupby(['latitude', 'longitude', 'DATEn', 'hour']) 
    # weatherGrouped = weather_df.groupby(['DATEn',]) 
    
    # print("list(weatherGrouped)) -> ")
    # print(list(weatherGrouped))
    # print("")
    
    # Example merge DataFrame, DataFrames, on more than one column, multiple columns - instructor solution  
    # inner - only rows with account keys in both tables kept
    # Multiple columns to merge on arrived at determined, they EXISTED in BOTH DataFrames to be merged 
    mergedDataFrame = subway_df.merge(weather_df, on = ['DATEn', 'hour', 'latitude', 'longitude'], how = 'inner')
    
    print("mergedDataFrame -> ")
    print(mergedDataFrame)
    # print("type(mergedDataFrame) - {}".format(type(mergedDataFrame)))
    #        type(mergedDataFrame) - <class 'pandas.core.frame.DataFrame'>
    print("")
    
    # This time 'date' does not match 'DATEn'
    # Example merge DataFrame, DataFrames when the column headings, columns, names do not match, *** merge DataFrames, column names do not match
    mergedDataFrame1 = subway_df.merge(weatherDifferent_df,
    left_on = ['DATEn', 'hour', 'latitude', 'longitude'],
    right_on = ['date', 'hour', 'latitude', 'longitude'],
    how = 'inner')
    
    print("mergedDataFrame1 -> ")
    print(mergedDataFrame1)
    print("")

    return None

combine_dfs(subway_df, weather_df)

print("\nEND\n")

    
    
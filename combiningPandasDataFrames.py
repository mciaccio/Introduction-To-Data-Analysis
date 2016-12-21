
# "github - How to merge DataFrames"

"""
combining two DataFrames
combining the rows in to DataFrames

    LEFT             RIGHT
submissions.merge(enrollments, on= 'account_key', how = 'left')

how - what to do when 'account_key' present in one table but not both 
inner - only rows with account_key in both DataFrames are kept 
outer - all rows from both DataFrames kept 
right - enrollments row kept even if no corresponding row in the submissions DataFrame 
left - rows present ONLY in the left DataFrame (submissions) - kept 
"""

import pandas as pd

"""
example how to populate initialize a DataFrame
"""
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

"""
NOTE DATEn CHANGED to - date
"""
weather_df1 = pd.DataFrame({
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
    
    NOT CALLED - all work done below 
    
    Fill in this function to take 2 DataFrames, one with subway data and one with weather data,
    and return a single dataframe with one row for each date, hour, and location. Only include
    times and locations that have both subway data and weather data available.
    '''
    
    """
    submissions.merge(enrollments, on= 'account_key', how = 'left')
    """
    
    mergedDataFrame = subway_df.merge(weather_df, on= 'DATEn', how = 'inner')
    print("mergedDataFrame -> ")
    print(mergedDataFrame)
    
    '''
    print("type(mergedDataFrame) - {}".format(type(mergedDataFrame)))   
           type(mergedDataFrame) - <class 'pandas.core.frame.DataFrame'>
     '''
    
    print("")

    return None
    
"""
example how to print dump the top head of a DataFrame 
"""
print("\nsubway_df.head(3) -> ")
print(subway_df.head(3))
    
print("\nweather_df.head(3) -> ")
print(subway_df.head(3))

"""
merge DataFrames keys, column headings MATCH 
how to merge DataFrames multiple keys, multiple "on" arguments 
requirement - one row for each date, hour, and location
therefore ON arguments include 'DATEn', 'hour', 'latitude', 'latitude'

requirement - have BOTH  subway data and weather data available
how = inner
"""
mergedDataFrame = subway_df.merge(weather_df, on = ['DATEn', 'hour', 'latitude', 'latitude'], how = 'inner') 

print("\nmergedDataFrame.head(3) -> ")
print(mergedDataFrame.head(3))
print("")

print("\nweather_df1.head(3) -> ")
print(weather_df1.head(3))
print("")


"""
merge DataFrames keys, column headings DO NOT MATCH 
NOTE - DATEn UPPERCASE, n suffix
subway_df.head(3) -> 
      DATEn  ENTRIESn   EXITSn  UNIT  hour   latitude  longitude
0  05-01-11   4388333  2911002  R003     0  40.689945 -73.872564

NOTE - date - lower case
weather_df1.head(3) -> 
       date  fog  hour   latitude  longitude  pressurei  rain  tempi  wspdi
0  05-01-11    0     0  40.689945 -73.872564      30.24     0   52.0    8.1
1  05-01-11  

merge with right_on, left_on to match up the two otherwise unique column headings 

"""
mergedDataFrame1 = subway_df.merge(weather_df1, left_on = ['DATEn', 'hour', 'latitude', 'latitude'], right_on = ['date', 'hour', 'latitude', 'latitude'], how = 'inner')

print("\nmergedDataFrame1.head(3) -> ")
print(mergedDataFrame1.head(3))
print("")

print("")
x = 5
print(" - {}".format(x))
print("type() - {}".format(type(x)))
print("")

print(" -> ")
print()
print("type() - {}".format(type(x)))
print("")


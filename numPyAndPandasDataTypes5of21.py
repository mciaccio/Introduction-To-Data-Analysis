'''
Created on Jan 12, 2017

@author: Menfi
'''

# github Panda DataFrames, each column assumed to be a different type, access ROW, access COLUMN, access ELEMENT, argmax, mean 
# Example use Panda DataFrames DataFrame - each column assumed to be of a different type
# Example Panda DataFrames have indexes, index, similar to Panda Series, index value for each row, name for each column 

import numpy as np
import pandas as pd

print("\nBegin\n")

# Example - create instantiate, populate numPy array, native Python list -> numpyArray with values 
my_numPyArray =  np.array([1, 2, 3, 4, 5]) 
# print("type(my_numPyArray) - {}".format(type(my_numPyArray)))
#        type(my_numPyArray) - <class 'numpy.ndarray'>

# Example - get the dtype of the numPyArray 
print("my_numPyArray.dtype -> ")
print(my_numPyArray.dtype)
# int64
print("")

enrollments = np.array([
['account_key', 'status', 'join_date'],
['488', 'canceled', '2014-11-10']
])

print("enrollments -> ")
print(enrollments)
print(enrollments.dtype) # <U11 unicode can't do math 
print("")
# print("type(enrollments) - {}".format(type(enrollments)))
#        type(enrollments) - <class 'numpy.ndarray'>

# Example - access 2 dimensional numPy array using both integers and slice, colon, bracket
print(" -> ")
print(enrollments[1,0])
print(enrollments[1,0].dtype) # <U3 can't do math
print(enrollments[1:2,0:1])
print(enrollments[1:2,0:1].dtype) # <U11 can't do math
print("")

# Example - create, instantiate, populate Pandas DataFrame, native Python Dictionary -> Panda DataFrame 
enrollments_df = pd.DataFrame({
    'account_key' : [448, 448, 448, 448, 448],
    'status' : ['canceled', 'canceled', 'canceled', 'canceled', 'current'],
    'days_to_cancel' : [65, 5, 0, 0, np.nan ]
    })
# print("type(enrollments_df) - {}".format(type(enrollments_df)))
#        type(enrollments_df) - <class 'pandas.core.frame.DataFrame'>

# Example - print Pandas DataFrame - displays nicely, column headers at top, row indexes starting with zero  
print("enrollments_df -> ")
print(enrollments_df)
print("")

# Example - Pandas DataFrame - *** CAN DO MATH ***, works on math friendly, numerical columns 
print("enrollments_df.mean() -> ")
print(enrollments_df.mean())
print("")

print("enrollments_df['account_key'] -> ")
print(enrollments_df['account_key'])
print("")

# Accessing Elements of a DataFrame 6 of 21
# Subway ridership for 5 stations (columns, axis = 0) on 10 different days (rows, axis = 1)
# Example - create, populate, instantiate Panda DataFrame, with hardcoded column headings, hardcoded index labels (strings), data attribute (argument), index attribute (argument), columns attribute (argument)
ridership_df = pd.DataFrame(
    data=[[   0,    0,    2,    5,    0],
          [1478, 3877, 3674, 2328, 2539],
          [1613, 4088, 3991, 6461, 2691],
          [1560, 3392, 3826, 4787, 2613],
          [1608, 4802, 3932, 4477, 2705],
          [1576, 3933, 3909, 4979, 2685],
          [  95,  229,  255,  496,  201],
          [   2,    0,    1,   27,    0],
          [1438, 3785, 3589, 4174, 2215],
          [1342, 4043, 4009, 4665, 3033]],
    index=['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
           '05-06-11', '05-07-11', '05-08-11', '05-09-11', '05-10-11'],
    columns=['R003', 'R004', 'R005', 'R006', 'R007']
)

# Change False to True for each block of code to see what it does
# DataFrame creation
if False:
    # Example - create, instantiate, populate Panda DataFrame - native Python Dictionary -> Panda DataFrame
    # Example - You can create a DataFrame out of a dictionary mapping column names to values, native Python Dictionary -> Panda DataFrame
    # Example - Panda DataFrame - print entire DataFrame, prints DataFrame data, column headings, and row indexes
    df_1 = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
    # print df_1
    print("df_1 -> ")
    print(df_1)
    print("")

    # Example - create, instantiate, populate Panda DataFrame - native Python list of lists + *** columns attribute *** -> Panda DataFrame
    # You can also use a list of lists or a 2D NumPy array
    # print Panda DataFrame - column headings, row indexes, DataFrame data 
    df_2 = pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=['A', 'B', 'C'])
    # print df_2
    print("df_2 -> ")
    print(df_2)
    print("")

# Accessing elements
if False:
    # Example - print Pandas DataFrame data, access first ROW by .iloc position, COLUMN headings printed too   
    # print ridership_df.iloc[0]
    print("ridership_df.iloc[0] -> ")
    print(ridership_df.iloc[0])
    print("")
    
    # Example - print Pandas DataFrame data, access fifth row by label string, row heading printed too    
    # print ridership_df.loc['05-05-11']
    print("ridership_df.loc['05-05-11'] -> ")
    print(ridership_df.loc['05-05-11'])
    print("")
    
    # Example - Pandas DataFrame access COLUMN by string label
    # print ridership_df['R003']
    print("ridership_df['R003'] -> ")
    print(ridership_df['R003'])
    print("")
    
    # Example - Pandas DataFrame - access by ROW, COLUMN, .iloc example *** zero based for both row and column ***
    # print ridership_df.iloc[1, 3]
    print("ridership_df.iloc[1, 3] -> ")
    print(ridership_df.iloc[1, 3])
    print("")
    
# Accessing multiple rows
if False:
    # Example - Pandas DatFrame - access, print multiple rows
    # print ridership_df.iloc[1:4]
    print("ridership_df.iloc[1:4] -> ")
    print(ridership_df.iloc[1:4])
    print("")
    
# Accessing multiple columns
# Example - Pandas DataFrame - access, print multiple rows, print two and only two rows
if False :
    # print ridership_df[['R003', 'R005']]
    print("ridership_df[['R003', 'R005']] -> ")
    print(ridership_df[['R003', 'R005']])
    print("")
    
# Pandas axis
if True:
    df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})

    # print df.sum()
    # Example Pandas DataFrame - sum
    print("df.sum() -> ")
    print(df.sum())
    print("")    
    
    # print df.sum(axis=1)
    # Example Pandas DataFrame - row sum, axis = 1
    print("df.sum(axis=1) -> ")
    print(df.sum(axis=1))
    print("")
    
    # print df.values.sum()
    # Example Pandas DataFrame - Pandas DataFrame -> values (numPy array) -> sum  
    print("df.values.sum() -> ")
    print(df.values.sum())
    
    # print("type(df.values) - {}".format(type(df.values)))
    #        type(df.values) - <class 'numpy.ndarray'>
    # print("type(df.values.sum()) - {}".format(type(df.values.sum())))
    #        type(df.values.sum()) - <class 'numpy.int64'>
    print("")
    
def mean_riders_for_max_station(ridership):
    '''
    Fill in this function to find the station with the maximum riders on the
    first day, then return the mean riders per day for that station. Also
    return the mean ridership overall for comparsion.
    
    This is the same as a previous exercise, but this time the
    input is a Pandas DataFrame rather than a 2D NumPy array.
    '''
    
    # Example - Pandas DataFrame get the first row, column heading names printed too
    print("190ridership.iloc[0] -> ")
    print(ridership.iloc[0])
    print("")

    # Example - Pandas DataFrame get the position, *** column heading *** of the maximum value 
    print("ridership.iloc[0] -> ")
    print(ridership.iloc[0].argmax())
    print("")
    
    # Example - Pandas DataFrame get the position, *** column heading *** of the maximum value 
    firstDayMaxStationColumn = ridership.iloc[0].argmax()
    print("firstDayMaxStationColumn - {}\n".format(firstDayMaxStationColumn))

    # Example - Pandas DataFrame, access the column by column label, column heading       
    ridersPerDay = ridership[firstDayMaxStationColumn]
    print("ridersPerDay -> ")
    print(ridersPerDay)
    print("")

    # Example - Pandas DataFrame, access the mean of the specified column
    print("ridersPerDay.mean() -> ")
    print(ridersPerDay.mean())
    print("")
    
    # Example - Pandas DataFrame, access the mean of the specified column
    # mean_for_max = None # Replace this with your code
    mean_for_max = ridersPerDay.mean()

    # Example - Pandas DataFrame, get the overall mean
    overall_mean = ridership.values.mean()
    print("overall_mean -> ")
    print(overall_mean)
    print("")
    
    overall_mean = None # Replace this with your code
    
    return (overall_mean, mean_for_max) 

mean_riders_for_max_station(ridership_df)

 
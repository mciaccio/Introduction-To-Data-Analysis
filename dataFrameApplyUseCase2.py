

import numpy as np
import pandas as pd

df = pd.DataFrame({
    'a': [4, 5, 3, 1, 2],
    'b': [20, 10, 40, 50, 30],
    'c': [25, 20, 5, 15, 10]
})

print("")
print("Start dataFrameApplyUseCase2.py ")
# print("type(df) - {}".format(type(df)))
# type(df) - <class 'pandas.core.frame.DataFrame'>
print("")

print("print the DataFrame -> ")
print(df)
print("")

# DataFrame - CLASS
print("type(df) - {}".format(type(df)))
# type(df) - <class 'pandas.core.frame.DataFrame'>
# apply - METHOD
print("type(df.apply) - {}".format(type(df.apply)))
# type(df.apply) - <class 'method'>
print("")

# Can't reasonably sort entire DataFrame, different columns in different order 
# Begin by sorting one of the columns
# latter we will use the apply() Method of the DataFrame Class
# to apply() the sort to each of the columns 
print("df.sort_values(by='a') -> ")
print(df.sort_values(by='a', ascending = 0))
print("")

# Change False to True for this block of code to see what it does
# DataFrame apply() - use case 2
if True:   
    
    # np.mean function of the NumPy module
    # print("type(np.mean) - {}".format(type(np.mean)))
    #type(np.mean) - <class 'function'>
    
    # apply the NumPy module mean function to EACH column of the df DataFrame 
    print("df.apply(np.mean) -> ")
    print(df.apply(np.mean))
    print("")

    # apply the NumPy module mean function to EACH column of the df DataFrame 
    # print df.apply(np.max)
    print("df.apply(np.max) -> ")
    print(df.apply(np.max))
    print("")
    
def second_largest_in_column(column):
    
    print("column -> ")
    print(column)
    print("")

    # print("type(column) - {}".format(type(column)))
    # type(column) - <class 'pandas.core.series.Series'>

    # sort descending that way index 0 will be the largest, index 1 will be the next to largest  
    sorted_column = column.sort_values(ascending=False)    
    print("sorted_column -> ")
    print(sorted_column)
    # print("type(sorted_column) - {}".format(type(sorted_column)))
    # <class 'pandas.core.series.Series'>
    print("")
    return sorted_column.iloc[1] # return index 1 second largest 
    print("")
    
def second_largest(df):
    '''
    Fill in this function to return the second-largest value of each 
    column of the input DataFrame.
    '''
    # No sort_value run against a pandas Series not a pandas DataFrame
    # columns in different order, can't sort the columns container, the DataFrame
    # print("df.sort_values(ascending=False) -> ")
    # print(df.sort_values(ascending=False))
 
    # second_largest_in_column function proven to return the second largest value in the one column - development - testing
    # now apply() the proven function to the DataFrame to each column
    return df.apply(second_largest_in_column)
    print("")
    
    return None

secondLargestValueInColumn = second_largest_in_column(df['a'])

print("secondLargestValueInColumn -> ")
print(secondLargestValueInColumn)
# print("type(secondLargestValueInColumn) - {}".format(type(secondLargestValueInColumn)))
# type(secondLargestValueInColumn) - <class 'numpy.int64'>
print("")

answer = second_largest(df)
print("answer -> ")
print(answer)
print("")
















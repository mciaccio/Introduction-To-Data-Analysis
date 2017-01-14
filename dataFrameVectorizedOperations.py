'''
Created on Jan 13, 2017

@author: Menfi
'''

# github Pandas DataFrame, Vectorized Operations, addition, indexes, *** shift ***

print("\nBegin\n")

import pandas as pd

# Examples of vectorized operations on DataFrames:
# Change False to True for each block of code to see what it does

# Example - vectorized operations on Panda DataFrame, addition, column names 
# Adding DataFrames with the column names, look like keys to dictionary
if False:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    df2 = pd.DataFrame({'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 90]})
    
    # print df1 + df2
    print("df1 + df2 -> ")
    print(df1 + df2)
    print("")

# Example - vectorized operations on Panda DataFrame, addition, column names 
# Adding DataFrames with overlapping column names, look like keys to dictionary
if False:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    df2 = pd.DataFrame({'d': [10, 20, 30], 'c': [40, 50, 60], 'b': [70, 80, 90]})
    
    # print df1 + df2
    print("df1 + df2 -> ")
    print(df1 + df2)
    print("")
    
# Example - vectorized operations on Panda DataFrame, addition, indexes, indices  
# Adding DataFrames with overlapping row indexes, *** indexes *** drove the addition
if True:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]},
                       index=['row1', 'row2', 'row3'])
    df2 = pd.DataFrame({'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 90]},
                       index=['row4', 'row3', 'row2'])
    
    print("df1 -> ")
    print(df1)
    print("")
    
    print("df2 -> ")
    print(df2)
    print("")
    
    # print df1 + df2
    print("df1 + df2 -> ")
    print(df1 + df2)
    print("")

# Example - create, instantiate, populate Panda DataFrame, column headings, - native Python list -> Panda DataFrame 
# --- Quiz ---
# Cumulative entries and exits for one station for a few hours.
entries_and_exits = pd.DataFrame({
    'ENTRIESn': [3144312, 3144335, 3144353, 3144424, 3144594,
                 3144808, 3144895, 3144905, 3144941, 3145094],
    'EXITSn': [1088151, 1088159, 1088177, 1088231, 1088275,
               1088317, 1088328, 1088331, 1088420, 1088753]
})

def get_hourly_entries_and_exits(entries_and_exits):
    '''
    Fill in this function to take a DataFrame with cumulative entries
    and exits (entries in the first column, exits in the second) and
    return a DataFrame with hourly entries and exits (entries in the
    first column, exits in the second).
    '''
    
    # print("type(entries_and_exits) - {}".format(type(entries_and_exits)))
    #        type(entries_and_exits) - <class 'pandas.core.frame.DataFrame'>

    shiftedEntriesAndExits = entries_and_exits.shift()
    print(" -> ")
    print(shiftedEntriesAndExits)
    # print("type(shiftedEntriesAndExits) - {}".format(type(shiftedEntriesAndExits)))
    #        type(shiftedEntriesAndExits) - <class 'pandas.core.frame.DataFrame'>
    print("")
    
    differenceEntriesAndExits = entries_and_exits - shiftedEntriesAndExits
    print("differenceEntriesAndExits -> ")
    print(differenceEntriesAndExits)
    print("type(differenceEntriesAndExits) - {}".format(type(differenceEntriesAndExits)))
    print("")
    
    # Example Pandas DataFrame - arithmetic difference, subtraction, diff, diff() method
    instructorAnswer = entries_and_exits.diff()
    print("instructorAnswer -> ")
    print(instructorAnswer)
    print("type(instructorAnswer) - {}".format(type(instructorAnswer)))
    print("")
    
    myDataFrameAnswer = instructorAnswer.fillna(0)
    print("myDataFrameAnswer -> ")
    print(myDataFrameAnswer)
    print("type(myDataFrameAnswer) - {}".format(type(myDataFrameAnswer)))
    print("")

    return None

get_hourly_entries_and_exits(entries_and_exits)

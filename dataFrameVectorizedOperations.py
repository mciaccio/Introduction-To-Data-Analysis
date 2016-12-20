

import pandas as pd
import numpy as np

# Examples of vectorized operations on DataFrames:
# Change False to True for each block of code to see what it does

print("")

# Adding DataFrames with the column names
if False:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    df2 = pd.DataFrame({'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 90]})
    # print df1 + df2
    # <class 'pandas.core.frame.DataFrame'>
    # print("type(df1) - {}".format(type(df1)))
    print("df1 -> ")
    print(df1)
    print("")
    
    print("type(df2) - {}".format(type(df2)))
    # <class 'pandas.core.frame.DataFrame'>
    # print("df2 -> ")
    print(df2)
    print("")
    
    # type(df1 + df2) - <class 'pandas.core.frame.DataFrame'>
    # print("type(df1 + df2) - {}".format(type(df1 + df2)))
    # added them up as expected 
    print("df1 + df2 -> ")
    print(df1 + df2)
    print("")
    
# Adding DataFrames with overlapping column names 
# NaN when value missing
if False:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    df2 = pd.DataFrame({'d': [10, 20, 30], 'c': [40, 50, 60], 'b': [70, 80, 90]})
    # print df1 + df2
    print("Adding Panda DataFrames with overlapping column names")
    print("df1 + df2 -> ")
    print(df1 + df2)
    print("")

# Adding DataFrames with overlapping row indexes
# NaN when ronN index missing
# This was hard - print off df1 and df2 2 first - then more intuitive 
if False:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]},
                       index=['row1',        'row2',         'row3'])
    
    df2 = pd.DataFrame({'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 90]},
                       index=['row4',      'row3',             'row2'])
    # print df1 + df2
    print("Adding Panda DataFrames with overlapping row indexeszzz")
    
    print("df1-> ")
    print(df1)
    print("")
    
    print("df2-> ")
    print(df2)
    print("")
    
    print("df1 + df2 -> ")
    print(df1 + df2)
    print("")
    

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
    
    print("type(entries_and_exits) - {}".format(type(entries_and_exits)))
    # type(entries_and_exits) - <class 'pandas.core.frame.DataFrame'>

    # first list used to populate panda series
    # then panda Series used to populate panda DataFrame 
    hourlyEntriesList = []
    hourlyExitsList = []
    
    # simple declaration of an empty DataFrame 
    hourlyData = pd.DataFrame()
    print("")
 
    print("entries_and_exits['ENTRIESn'] -> ")
    print(entries_and_exits['ENTRIESn'])
    print("")
    # print("type(entries_and_exits['ENTRIESn']) - {}".format(type(entries_and_exits['ENTRIESn'])))
    # type(entries_and_exits['ENTRIESn']) - <class 'pandas.core.series.Series'>
    
    # for index, row in entries_and_exits['ENTRIESn'].iterrows():
    # loop through the entries_and_exits['ENTRIESn'] panda Series
    # populate the hourlyEntriesList
    lastValue = 0
    for index, value in entries_and_exits['ENTRIESn'].iteritems():
        newValue = value - lastValue
        print("index - {}, value - {}, lastValue - {}, newValue - {}".format(index, value, lastValue, newValue))
        lastValue = value
        if index > 0:
            # populate the hourlyEntriesList list
            hourlyEntriesList.append(newValue)
        # populate a list then panda Series with NaN - np.nan
        elif index == 0:
            hourlyEntriesList.append(np.nan)
    print("")
    
    print("hourlyEntriesList -> {}\n".format(hourlyEntriesList))
    
    # populate the panda Series with the list
    hourlyData['hourlyEntries'] = pd.Series(hourlyEntriesList)
    
    lastValue = 0
    for index, value in entries_and_exits['EXITSn'].iteritems():
        newValue = value - lastValue
        print("index - {}, value - {}, lastValue - {}, newValue - {}".format(index, value, lastValue, newValue))
        lastValue = value
        if index > 0:
            # populate the hourlyExitsList list
            hourlyExitsList.append(newValue)
        # populate a list then panda Series with NaN - np.nan
        elif index == 0:
            hourlyExitsList.append(np.nan)
    print("")
    
    print("hourlyExitsList -> {}\n".format(hourlyExitsList))
    
    # populate the panda Series with the list
    hourlyData['hourlyExits'] = pd.Series(hourlyExitsList)
    
    print("hourlyEntries DataFrame -> ")
    print(hourlyData)
    print("")
    
    print("hourlyEntries['hourlyEntries'] series -> ")
    print(hourlyData['hourlyEntries'])
    print("")
    
    print("hourlyEntries['hourlyExits'] series -> ")
    print(hourlyData['hourlyExits'])
    print("")
    
    # from instructor
    # one line answer, also see vectorized operations subtraction below 
    print("entries_and_exits.diff() -> ")
    print(entries_and_exits.diff())
    print("")
    
    print("entries_and_exits.shift() -> ")
    print(entries_and_exits.shift(1))
    print("")
    
    #print("type(entries_and_exits) - {}".format(type(entries_and_exits)))
    # type(entries_and_exits) - <class 'pandas.core.frame.DataFrame'>
    
    print("entries_and_exits -> ") 
    print(entries_and_exits)
    print("")
    
    dataFrameRow1 = entries_and_exits.ix[:0] # zeroth row only 
    print("dataFrameRow1 -> ")
    print(dataFrameRow1)
#       ENTRIESn   EXITSn
#0   3144312  1088151
    print("")

    dataFrameColumn1 = entries_and_exits.ix[:,0] # zeroth column only, index on left
    print("dataFrameColumn1 -> ")
    print(dataFrameColumn1)
    print("")

    dataFrameColumn2 = entries_and_exits.ix[:,1] # column2 index on left
    print("dataFrameColumn2 -> ")
    print(dataFrameColumn2)
    # index on left, column 2 value on right
    print("")
    
    dataFrameColumn1 = entries_and_exits.ix[:0]
    print("dataFrameColumn1 -> ")
    print(dataFrameColumn1) # zeroth ROW
#     ENTRIESn   EXITSn
# 0   3144312  1088151
    print("")
    
    dataFrameRow1 = entries_and_exits.ix[0]
    print("dataFrameRow1 -> ")
    print(dataFrameRow1) # zeroth row
#     ENTRIESn    3144312
#     EXITSn      1088151
#     Name: 0, dtype: int64
    print("")

    # think [row, column]
    x = entries_and_exits.ix[0,0]
    # move 1 to the next column
    y= entries_and_exits.ix[0,1]
    print("dataFrameApplyMap -> ")
    print(x)
    #3144312
    print("y -> ")
    print(y)
    #1088151
    print("")
    
    print ("Begin")
    print (entries_and_exits.ix[:,1]) # column 2 index on right
    print("")
    print (entries_and_exits.ix[:1]) # top two rows, row index and column headings
    print("")
    print (entries_and_exits.ix[0:1]) # same as [:1]
    print("")
    print (entries_and_exits.ix[:0,0]) # row zero column zero -  0    3144312 same as [0,0]
    print (entries_and_exits.ix[:0,1]) # row zero column one - 0    1088151
    print (entries_and_exits.ix[0:0]) # first row
#        ENTRIESn   EXITSn
# 0   3144312  1088151

    print("")
    print (entries_and_exits.ix[3:5,1]) # column1 not column zero, rows 3 - 5, zero based indexing 
    print("..............")
    
    print("")
    print (entries_and_exits.ix[3:5]) # columns 0 and 1, rows 3 -5, zero based indexing
    
    print("")
    print (entries_and_exits.ix[3:5,0]) # zeroth column only, only 1 column
    print("")
    
    print (entries_and_exits.ix[3:5]) # both columns
    print("")
    
    # one line answer from instructor
    # does the same subtraction as is done in my manual looping above  
    # vectorized operations - subtraction
    (entries_and_exits - entries_and_exits.shift(1))
    #entries_and_exists - entries_and_exists.shift(1) 

    return None


get_hourly_entries_and_exits(entries_and_exits)
print("")

x = 5
print("dataFrameApplyMap - {}".format(x))
print("type(dataFrameApplyMap) - {}".format(type(x)))

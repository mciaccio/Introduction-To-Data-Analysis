'''
Created on Jan 16, 2017

@author: Menfi  
'''

# github "groupby, call or *** apply *** custom Python function to a Panda Series, then to a DataFrameGroupBy", specify DataFrame columns

print("\nBegin\n")

import numpy as np
import pandas as pd

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# print("example_df -> ")
# print(example_df)
# print("type(example_df) - {}".format(type(example_df)))
# type(example_df) - <class 'pandas.core.frame.DataFrame'>
# print("")

# print("example_df['value'] -> ")
# print(example_df['value'])
# print("type(example_df['value']) - {}".format(type(example_df['value'])))
#        type(example_df['value']) - <class 'pandas.core.series.Series'>
# print("")

# Change False to True for each block of code to see what it does

# Standardize each group
# called twice, evens passed in, standardized values returned -  odds passed in, standardized values returned 
if False:
    def standardize(xs):
        print("standardize function xs -> ")
        print(xs)
        # print("type(xs) - {}".format(type(xs)))
        #        type(xs) - <class 'pandas.core.series.Series'>
        print("")
        
        print("xs.mean() -> ")
        print(xs.mean())
        # print("type(xs.mean()) - {}".format(type(xs.mean())))
        #        type(xs.mean()) - <class 'float'>
        print("")
        
        print("xs.std() -> ")
        print(xs.std())
        # print("type(xs.std()) - {}".format(type(xs.std())))
        # type(xs.std()) - <class 'float'>
        print("")

        print("(standardized values xs - xs.mean()) / xs.std() -> ")
        print((xs - xs.mean()) / xs.std())
        # print("type((xs - xs.mean()) / xs.std()) - {}".format(type((xs - xs.mean()) / xs.std())))
        #        type((xs - xs.mean()) / xs.std()) - <class 'pandas.core.series.Series'>
        print("")

        return (xs - xs.mean()) / xs.std()
    
    # Example groupby('even') - 'even' boolean, True (4), False(3)
    # Example groupby('even') - 'even' boolean, groups - *** echo debug grouping ***  
    grouped_data = example_df.groupby('even')

    print("grouped_data -> ")
    print(grouped_data)
    # <pandas.core.groupby.DataFrameGroupBy object at 0x10a67dac8> NOT USEFUL
    # print("type(grouped_data) - {}".format(type(grouped_data)))
    #        type(grouped_data) - <class 'pandas.core.groupby.DataFrameGroupBy'>
    print("")

    print("-- even -- grouped_data.groups -> ")
    print(grouped_data.groups)
    # {False: ['a', 'b', 'e'], True: ['c', 'd', 'f', 'g']} # echo debug grouping
    # print("type(grouped_data.groups) - {}".format(type(grouped_data.groups)))
    #        type(grouped_data.groups) - <class 'dict'>
    print("")

    print("-- even -- list(grouped_data).groups -> ")
    print(list(grouped_data.groups)) # cast to list not very useful
    # [False, True]
    print("")
    
    # USEFUL - LIST TO SEE CONTENTS, SCOPE OF VARIABLE - TOO MANY COLUMNS HERE 
    print("-- even -- list(grouped_data) -> ") # *** BAD ALL COLUMNS, CAN"T PASS NON NUMERIC
    print(list(grouped_data))
    # print("type(list(grouped_data)) - {}".format(type(list(grouped_data))))
    # type(list(grouped_data)) - <class 'list'>
    print("")
     
    # LIMIT TO NUMERIC COLUMN
    print("grouped_data['value'] -> ")
    print(grouped_data['value'])
    # <pandas.core.groupby.SeriesGroupBy object at 0x11308f908> # NOT USEFUL
    # print("type(grouped_data['value']) - {}".format(type(grouped_data['value'])))
    #        type(grouped_data['value']) - <class 'pandas.core.groupby.SeriesGroupBy'>
    print("")

    print("grouped_data['value'].groups -> ")
    print(grouped_data['value'].groups)
    # {False: ['a', 'b', 'e'], True: ['c', 'd', 'f', 'g']} # NOT VERY USEFUL
    # print("type(grouped_data['value'].groups) - {}".format(type(grouped_data['value'].groups)))
    #        type(grouped_data['value'].groups) - <class 'dict'>

    print("list(grouped_data['value'].groups -> ")
    print(list(grouped_data['value'].groups)) # NOT VERY USEFUL
    # [False, True]
    # print("type(list(grouped_data['value'].groups) - {}".format(type(list(grouped_data['value'].groups))))
    #        type(list(grouped_data['value'].groups) - <class 'list'>
    print("")

    # USEFUL - LIST TO SEE CONTENTS, SCOPE OF VARIABLE - JUST NUMERIC ['value'] COLUMN HERE  
    # *** PASS, apply, THIS TO THE PYTHON standardize FUNCTION  
    # **** LIMIT TO ['value'] NUMERIC COLUMN ****
    # **** VERY USEFUL, SHOWS -- even -- GROUPING, SHOWS ONLY NUMERIC COLUMN ****
    # **** ****
    print("list(grouped_data['value']) -> ")
    print(list(grouped_data['value']))
    # print("type(list(grouped_data['value'])) - {}".format(type(list(grouped_data['value']))))
    #        type(list(grouped_data['value'])) - <class 'list'>
    print("") 
        
    # apply python standardize function to - <class 'pandas.core.groupby.SeriesGroupBy'>
    # apply changes class 'pandas.core.groupby.SeriesGroupBy' *** to *** 
    # class 'pandas.core.series.Series' -- SEE standardize Python FUNTION
    # *** summary grouped by 'even', pass ['value'] numeric column to function ***
    # *** pass 1 column to function ***
    # grouped_data['value'].apply(standardize)
    
    # remember grouped by 'even', so standardize function *** called twice *** , one for the evens, and once for the odds
    myStandardizedValues = grouped_data['value'].apply(standardize)
    print("myStandardizedValues -> ")
    print(myStandardizedValues)
    # print("type(myStandardizedValues) - {}".format(type(myStandardizedValues)))
    # type(myStandardizedValues) - <class 'pandas.core.series.Series'>

    print("")

# Find second largest value in each group
# called twice, evens passed in, second largest returned -  odds passed in, second largest returned 
if True:
    def second_largest(xs):
        # print(pandasSeries.sort_values(ascending = 0))
        sorted_xs = xs.sort_values(inplace = False, ascending = False)
        # sorted_xs = xs.sort(inplace=False, ascending=False)
        return sorted_xs.iloc[1]
    grouped_data = example_df.groupby('even')
    print("type(grouped_data) - {}".format(type(grouped_data)))
    #      type(grouped_data) - <class 'pandas.core.groupby.DataFrameGroupBy'>
    
    print("list(grouped_data['value']) -> ")
    print(list(grouped_data['value']))
    print("")
    
    # print grouped_data['value'].apply(second_largest)
    print("grouped_data['value'].apply(second_largest) -> ")
    print(grouped_data['value'].apply(second_largest))
    # print("type(grouped_data['value'].apply(second_largest)) - {}".format(type(grouped_data['value'].apply(second_largest))))
    #        type(grouped_data['value'].apply(second_largest)) - <class 'pandas.core.series.Series'>
    print("")   

# --- Quiz ---
# DataFrame with cumulative entries and exits for multiple stations
ridership_df = pd.DataFrame({
    'UNIT': ['R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051'],
    'TIMEn': ['00:00:00', '02:00:00', '04:00:00', '06:00:00', '08:00:00', '10:00:00', '12:00:00', '14:00:00', '16:00:00'],
    'ENTRIESn': [3144312, 8936644, 3144335, 8936658, 3144353, 8936687, 3144424, 8936819, 3144594],
    'EXITSn': [1088151, 13755385,  1088159, 13755393,  1088177, 13755598, 1088231, 13756191,  1088275]
})

def getanswer(df):
    print("getanswer df -> ")
    print(df)
    print("type(df) - {}".format(type(df)))
    #        type(df) - <class 'pandas.core.frame.DataFrame'>
    print("")
    
    # Course work solution - shift the Panda DataFrame passed in - once for each station, UNIT group
    shiftedDataFrame = df.shift()
    print("getanswer shiftedDataFrame -> ")
    print(shiftedDataFrame)
    # print("type(shiftedDataFrame) - {}".format(type(shiftedDataFrame)))
    #        type(shiftedDataFrame) - <class 'pandas.core.frame.DataFrame'>
    print("")
    
    # df.subtract(shiftedDataFrame)

    df['ENTRIESn'] 
    df[['ENTRIESn']] 
    df[['ENTRIESn', 'EXITSn']] 
    df[['ENTRIESn', 'EXITSn']]
    shiftedDataFrame[['ENTRIESn', 'EXITSn']]
    
    # Course work solution - vectorized, subtract the DataFrames, get hourly ENTRIESn', 'EXITSn' from cumulative ENTRIESn', 'EXITSn' DataFrame subtract specific columns
    # My method do math on specific specified columns - see instructor method below  
    differenceDataFrame = df[['ENTRIESn', 'EXITSn']] - shiftedDataFrame[['ENTRIESn', 'EXITSn']]
    differenceDataFrame = df[['ENTRIESn', 'EXITSn']].sub(shiftedDataFrame[['ENTRIESn', 'EXITSn']])
    differenceDataFrame = df[['ENTRIESn', 'EXITSn']].subtract(shiftedDataFrame[['ENTRIESn', 'EXITSn']])
    differenceDataFrame = df[['ENTRIESn', 'EXITSn']].sub(shiftedDataFrame[['ENTRIESn', 'EXITSn']])

    # print("type(df[['ENTRIESn', 'EXITSn']]) - {}".format(type(df[['ENTRIESn', 'EXITSn']])))
    #        type(df[['ENTRIESn', 'EXITSn']]) - <class 'pandas.core.frame.DataFrame'>
    # print("type(df[['ENTRIESn', 'EXITSn']].sub) - {}".format(type(df[['ENTRIESn', 'EXITSn']].sub)))
    #        type(df[['ENTRIESn', 'EXITSn']].sub) - <class 'method'>

    # Course work solution - correct answer here 
    print("differenceDataFrame -> ")
    print(differenceDataFrame)
    # print("type(differenceDataFrame) - {}".format(type(differenceDataFrame)))
    #         type(differenceDataFrame) - <class 'pandas.core.frame.DataFrame'>
    print("")    
    return differenceDataFrame

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
    
    print("entries_and_exits -> ")
    print(entries_and_exits)
    # print("type(entries_and_exits) - {}".format(type(entries_and_exits)))
    #        type(entries_and_exits) - <class 'pandas.core.frame.DataFrame'>
    print("")
    
    # Course work solution, first goupby the station - UNIT column of Panda DataFrame
    groupedByStation = entries_and_exits.groupby('UNIT')
    # This printing debugging NOT helpful
    # print("groupedByStation -> ")
    # print(groupedByStation)
    # <pandas.core.groupby.DataFrameGroupBy object at 0x11306f978>
    # print("type(groupedByStation) - {}".format(type(groupedByStation)))
    #        type(groupedByStation) - <class 'pandas.core.groupby.DataFrameGroupBy'>
    print("")

    # Get more DataFrameGroupBy object information groups - from instructor
    print("groupedByStation.groups -> ")
    print(groupedByStation.groups)
    # {'R079': [1, 3, 5, 7], 'R051': [0, 2, 4, 6, 8]}
    # print("type(groupedByStation.groups) - {}".format(type(groupedByStation.groups)))
    #        type(groupedByStation.groups) - <class 'dict'>
    print("")
    
    # Get more DataFrameGroupBy object information - indices
    print("groupedByStation.indices -> ")
    print(groupedByStation.indices)
    # {'R051': array([0, 2, 4, 6, 8]), 'R079': array([1, 3, 5, 7])}
    print("")
     
    # Get more DataFrameGroupBy object information - get a station, UNIT
    print("groupedByStation.get_group('R079') -> ")
    print(groupedByStation.get_group('R079'))
    # print("type(groupedByStation.get_group('R079')) - {}".format(type(groupedByStation.get_group('R079'))))
    #        type(groupedByStation.get_group('R079')) - <class 'pandas.core.frame.DataFrame'>
    print("")
 
    # Create DataFrame subset of another DataFrame, specific columns, specify columns 
    print("entries_and_exits.loc[:,'ENTRIESn' : 'EXITSn'] -> ")
    print(entries_and_exits.loc[:,'ENTRIESn' : 'EXITSn'])
    # print("type(entries_and_exits.loc[:,'ENTRIESn' : 'EXITSn']) - {}".format(type(entries_and_exits.loc[:,'ENTRIESn' : 'EXITSn'])))
    # type(entries_and_exits.loc[:,'ENTRIESn' : 'EXITSn']) - <class 'pandas.core.frame.DataFrame'>
    print("")

    # Get more DataFrameGroupBy object information - list 
    print("list(groupedByStation) -> ")
    print(list(groupedByStation))
    print("")
    
    # Get more DataFrameGroupBy object information, column detail - list 
    print("list(groupedByStation['ENTRIESn'] -> ")
    print(list(groupedByStation['ENTRIESn']))
    print("")

    # Get more DataFrameGroupBy object information, column detail - list      
    print("list(groupedByStation['EXITSn']) -> ")
    print(list(groupedByStation['EXITSn']))
    print("")
           
    # return None
    # Course work solution - apply the getanswer function to the groupedByStation (pandas.core.groupby.DataFrameGroupBy)
    return groupedByStation.apply(getanswer)
    
    # working *** INSTRUCTOR *** method - limit DataFrameGroupBy columns apply applied to custom Python function, pass ONLY the specific, specified numeric columns for math 
    # return groupedByStation[['ENTRIESn', 'EXITSn']].apply(getanswer) # instructor specify specific columns of groupby object

# Course work solution
answer = get_hourly_entries_and_exits(ridership_df)
print("answer -> ")
print(answer)
print("type(answer) - {}".format(type(answer)))
print("")

print("\nEnd\n")



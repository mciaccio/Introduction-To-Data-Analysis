import pandas as pd

# Subway ridership for 5 stations on 10 different days
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

print("")
# print("ridership_df ->")
# print(ridership_df)
#       (ridership_df) - <class 'pandas.core.frame.DataFrame'>
# print("(ridership_df) - {}".format(type(ridership_df)))
print("")


# Accessing elements
if False:
    print("Begin Accessing elements ILOC required loc will not work")
    print("")
    # print (ridership_df.iloc[0]) # column headings - zeroth ROW, zero based indexing
    print("")

    x = ridership_df.iloc[0]
    # type(x) - <class 'pandas.core.series.Series'>
    # print("type(x) - {}".format(type(x)))
    print("")
    
    # print (ridership_df.iloc[9]) # column headings - ninth ROW, zero based indexing
    print("")

    # print (ridership_df.loc['05-05-11']) # column headings - fourth ROW, zero based indexing
    
    print("")
    # print (ridership_df['R003']) # row labels, zeroth COLUMN - zero based indexing
    print("")
    
    # print (ridership_df.iloc[1, 3]) # no headings or labels - first row, third column zero based indexing
    print("")
    print("End Accessing elements\n")
        
# Accessing multiple rows
if False:
    print("")
    #print (ridership_df.iloc[1:4]) # column headings, row labels - rows 1,2,3 - zero based indexing
    print("")
    
    
# Accessing multiple columns
if True:
    # print (ridership_df[['R003', 'R005']]) # column headings, row labels,  column zero, column two - zero based indexing 
    print("")
    
# Pandas axis
if False :
    df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
    
    print(df)
    print("")
    
    # print (df.sum()) # column headings - column sums 
    print("")

    # print (df.sum(axis=1)) # row index - row sums
    print("")
    
    # x = df.values.sum()
    # type(x) - <class 'numpy.int64'>
    # print("type(x) - {}".format(type(x)))
    # print("")

    # print (df.values.sum()) # sum of all values in Data Frame - 15 
    print("")
   






# Change False to True for each block of code to see what it does

# DataFrame creation
# print Data Frame 
df_1 = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
if False:
    # You can create a DataFrame out of a dictionary mapping column names to values
    # Dictionary key value pairs - value is 
    df_1 = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
    #        type(df_1) - <class 'pandas.core.frame.DataFrame'>
    # print("type(df_1) - {}".format(type(df_1)))

    # print df_1
    # print entire DataFrame Data Frame
    print("Entire Panda Data Frame df_1 -> ")
    print(df_1)
    print("")
    
# print Data Frame Rows     
if False:    
    print("First ROW df_1.loc[0] -> ")
    print(df_1.loc[0])
    print("First ROW ILOC df_1.iloc[0] -> ")
    print(df_1.iloc[0])
    print("")
    print("Second ROW df_1.loc[2] -> ")
    print(df_1.loc[2])
    print("Second ROW ILOC df_1.iloc[2] -> ")
    print(df_1.iloc[2])
    print("")
    
# print Data Frame Columns     
if False:
    print("zeroth ILOC COLUMN df_1.iloc[:,0] -> ")
    print(df_1.iloc[:,0]) # zeroth column
    print("")
    
    print("first ILOC COLUMN df_1.iloc[:,1] -> ")
    print(df_1.iloc[:,1]) # zeroth column
    print("")
    
# print Data Frame Elements 
if False:
    print("zero ROW, ZERO Column, df_1.loc[0][1] -> ")
    print(df_1.loc[0][1])
    print("")
    print("zero ROW, ZERO Column, df_1.loc[2][0] -> ")
    print(df_1.loc[2][1])
    print("")





    
    
    
    # print("zero ROW, ONE Column, df_1.loc[0][1] -> ")
    # print(df_1.loc[0][1])
    # print("zero ROW, ONE Column, ILOC, df_1.iloc[0][1] -> ")
    # print(df_1.iloc[0][1])
    # print("")
# 
#     print("...........52first ROW df_1.loc[:0] -> ")
#     print(df_1.loc[:0])
#     print("")
#     print("first two ROWS df_1.loc[:1] -> ")
#     print(df_1.loc[:1])
#     print("")
#     print("all three ROWS df_1.loc[:2] -> ")
#     print(df_1.loc[:2])
#     print("")
#     print(".....61all ROWS first COLUMN df_1.loc[:3,0] -> ")
#     # print(df_1.loc[0]) # zeroth row
#     print(df_1.iloc[:,0]) # zeroth column
#     print(df_1.iloc[:,1]) # first column
#     print(df_1.loc[1])
#     print(df_1.loc[0:0])
#     print(df_1.loc[0:1])
#     print(df_1.loc[1:])
#     print(df_1.loc[0][0])
#     print(df_1.loc[0][1])
#     print("")
#     print("all ROWS second COLUMN df_1.loc[:3,1] -> ")
#     print(df_1.iloc[:3,1])
#     print("")
#     print("df_1.loc[2] -> ")
#     print(df_1.loc[2])
#     print("")
#     
    # You can also use a list of lists or a 2D NumPy array
    df_2 = pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=['A', 'B', 'C'])
    # print df_2
#     print("Panda Data Frame df_2 -> ")
#     print(df_2)
#     print("")


# Accessing elements
if False:
    # print ridership_df.iloc[0]
    print("ILOC ridership_df.iloc[0]) -> ")
    print(ridership_df.iloc[0])
    print("")


    # print ridership_df.loc['05-05-11']
    print("ridership_df.loc['05-05-11'] -> ")
    print(ridership_df.loc['05-05-11'])
    print("")

    #print ridership_df['R003']
    print("ridership_df['R003'] -> ")
    print(ridership_df['R003'])
    print("")
    
    # print ridership_df.iloc[1, 3]
    print("ridership_df.iloc[1, 3] -> ")
    print(ridership_df.iloc[1, 3])
    print("")


    
# Accessing multiple rows
if False:
    # print ridership_df.iloc[1:4]
    print("ridership_df.iloc[1:4] -> ")
    print(ridership_df.iloc[1:4])
    print("")
    
# Accessing multiple columns
if False:
    # print ridership_df[['R003', 'R005']]
    print("ridership_df[['R003', 'R005']] -> ")
    print(ridership_df[['R003', 'R005']])
    print("")

# Pandas axis
if False:
    df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
    
    # print df.sum()
    print("df -> ")   
    print(df)   
    print("")    
    
    # print df.sum()
    print("sum of A COLUMN, sum of B COLUMN - df.sum() -> ")   
    print(df.sum())   
    print("")

    # print df.sum(axis=1)
    print("132 ... sum of all ROWS - df.sum(axis=1) -> ") 
    print(df.sum(axis=1)) 
    print("")

    
    #print df.values.sum()
    # print values of Data Frame 
    print("SUM OF ALL VALUES in Data Frame df.values.sum() -> ")
    print(df.values.sum())
    print("")

def mean_riders_for_max_station(ridership):
    '''
    Fill in this function to find the station with the maximum riders on the
    first day, then return the mean riders per day for that station. Also
    return the mean ridership overall for comparsion.
    
    This is the same as a previous exercise, but this time the
    input is a Pandas DataFrame rather than a 2D NumPy array.
    '''
    overall_mean = None # Replace this with your code
    mean_for_max = None # Replace this with your code
    
    return (overall_mean, mean_for_max)
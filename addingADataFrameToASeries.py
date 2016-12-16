
# Adding a DataFrame to a Series
# adds each value of the Series to one column of the DataFrame 
# matches up the Series to the DataFrame using the index of the Series
# and the column names of the DataFrame 

import pandas as pd

# Change False to True for each block of code to see what it does

# Adding a Series to a square DataFrame - square - same number of rows and columns 
# 0:. 1:, 2:, 3: - column names, column headings
# addition driven by indexes 0 - 4
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    #print df
    print("")
    print("df -> ")
    print(df)
    print("")
    
    print("s -> ")
    print(s)
    print("")
    
    # 1 added to the first column 
    # 2 added to the second column 
    # 3 added to the third column 
    # 4 added to the fourth column 
    #print df + s
    print("")
    print("df + s -> ")
    print(df + s)
    print("")
    
# Adding a Series to a one-row DataFrame 
# One added to each COLUMN
# value from Series add to DataFrame column 
#
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({0: [10], 1: [20], 2: [30], 3: [40]})
    
    #print df
    print("")
    print("df -> ")
    print(df)
    print("")
    
    print("s -> ")
    print(s)
    print("")
     
    #print df + s
    print("")
    print("df + s -> ")
    print(df + s)
    print("")

# Adding a Series to a one-column DataFrame
# one added to the zeroth column
# columns 1 - 3 zero based indexing - NaN
if False    :
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({0: [10, 20, 30, 40]})
    
        #print df
    print("")
    print("df -> ")
    print(df)
    print("")
    
    print("s -> ")
    print(s)
    print("")
     
    #print df + s
    print("")
    print("df + s -> ")
    print(df + s)
    print("")
    
    
    
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({0: [10, 20, 30, 40]})
    
        #print df
    print("")
    print("df -> ")
    print(df)
    print("")
    
    print("s -> ")
    print(s)
    print("")
     
    #print df + s
    print("")
    print("df + s -> ")
    print(df + s)
    print("")
    
    print(df.add(s))
    print("")
    
    # axis = 0 rows, axis = 1 columns
    print(df.add(s, axis=0)) # gives us what we want - (DataFrame Series Axis Working Example)
    print("") 
    
# Adding when DataFrame column names match Series index
# addition driven by index matching
# DataFrame values at index 'b' - 50, 60, 70, 80
# Bumped by Series value at index b - 2 
if False:
    s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    df = pd.DataFrame({
        'a': [10, 20, 30, 40],
        'b': [50, 60, 70, 80],
        'c': [90, 100, 110, 120],
        'd': [130, 140, 150, 160]
    })
    
    
    #print df
    print("")
    print("df -> ")
    print(df)
    print("")
    
    print("s -> ")
    print(s)
    print("")
     
    #print df + s
    print("")
    print("df + s -> ")
    print(df + s)
    print("")
    
    #print df
    #print '' # Create a blank line between outputs
    #print df + s
    
# Adding when DataFrame column names don't match Series index
# column headings extended
# from a   b   c   d to -> 
#      a   b   c   d   0   1   2   3
# All values Nan
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        'a': [10, 20, 30, 40],
        'b': [50, 60, 70, 80],
        'c': [90, 100, 110, 120],
        'd': [130, 140, 150, 160]
    })
    
    #print df
    print("")
    print("df -> ")
    print(df)
    print("")

    print("s -> ")
    print(s)
    print("")
     
    #print df + s
    print("")
    print("df + s -> ")
    print(df + s)
    print("")
    
if True:
    s = pd.Series([1, 2, 3, 4], index = ['b', 'c', 'd', 'e', ])
    # column names of DataFrame is a, b, c, d
    df = pd.DataFrame({
        'a': [10, 20, 30, 40],
        'b': [50, 60, 70, 80],
        'c': [90, 100, 110, 120],
        'd': [130, 140, 150, 160]
    })
    
    print("")
    print("df -> ")
    print(df)
    print("")

    print("s -> ")
    print(s)
    print("")
    
    #print df + s
    print("")
    print("df + s -> ")
    print(df + s)
    print("")

print("")
x = 5
print("x - {}".format(x))
print("type(x) - {}".format(type(x)))
print("")

print("x -> ")
print(x)
print("type(x) - {}".format(type(x)))
print("")

# Adding a DataFrame to a Series
# adds each value of the Series to one column of the DataFrame 
# matches up the Series to the DataFrame using the index of the Series
# and the column names of the DataFrame 


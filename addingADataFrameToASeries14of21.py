'''
Created on Jan 15, 2017

@author: Menfi
'''

# github use *** axis *** argument, parameter, when adding a Pandas Series to a Pandas DataFrame

import pandas as pd 

print("\nBegin\n")

# Change False to True for each block of code to see what it does

# Example - Adding a Series to a square DataFrame
# integers of the Pandas Series are added to the integers of the Pandas DataFrame 
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    # print df
    # print '' # Create a blank line between outputs
    # print df + s
    
    # print("df -> ")
    print(df)
    # print("type(df) - {}".format(type(df)))
    #        type(df) - <class 'pandas.core.frame.DataFrame'>

    print("")
    
    # print("df + s -> ")
    print(df + s)
    # print("type(df + s) - {}".format(type(df + s)))
    #        type(df + s) - <class 'pandas.core.frame.DataFrame'>

    print("")
    
# Adding a Series to a one-row DataFrame 
# integers of the Pandas Series are added to the integers of the Pandas DataFrame 
# Example - create, instantiate, populate 1 row Pandas DataFrame  
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({0: [10], 1: [20], 2: [30], 3: [40]})
    
    # print df
    # print '' # Create a blank line between outputs
    # print df + s
    
    # print("df -> ")
    print(df)
    # print("type(df) - {}".format(type(df)))
    #        type(df) - <class 'pandas.core.frame.DataFrame'>

    # print("")
    
    # print("df + s -> ")
    print(df + s)
    # print("type(df + s) - {}".format(type(df + s)))
    #        type(df + s) - <class 'pandas.core.frame.DataFrame'>

    print("")

# Adding a Series to a one-column DataFrame
# Pandas Series Integers added to the first column, NaN all the rest 
# Example - create, instantiate, populate 1 column Pandas DataFrame  
# Example - use *** axis *** argument, parameter, when adding a Pandas Series to a Pandas DataFrame  
if True:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({0: [10, 20, 30, 40]})
    
    # print df
    # print '' # Create a blank line between outputs
    # print df + s
    
    # print("df -> ")
    print(df)
    # print("type(df) - {}".format(type(df)))
    # type(df + s) - <class 'pandas.core.frame.DataFrame'>

    # print("")
    
    # print("80df + s -> ")
    print(df + s)
    # print("type(df + s) - {}".format(type(df + s)))
    # type(df + s) - <class 'pandas.core.frame.DataFrame'>
    print("")
    
    print(df.add(s))
    print("92")
    # Example - axis = 0 fixes problem - add a Pandas Series to a one (1) column DataFrame, use axis = 0 for expected results  
    print(df.add(s, axis = 0)) # works
    print(df.add(s, axis = 'columns')) # does not work - Nan
    print(df.add(s, axis = 'rows')) # works Pandas Series integers add to Pandas DataFrame integers  
    print(df.add(s, axis = 'index')) # instructor method - works Pandas Series integers add to Pandas DataFrame integers  
    
# Adding when DataFrame column names match Series index
# Pandas Series integers successfully added to Pandas DataFrame integers 
if False  :
    s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    df = pd.DataFrame({
        'a': [10, 20, 30, 40],
        'b': [50, 60, 70, 80],
        'c': [90, 100, 110, 120],
        'd': [130, 140, 150, 160]
    })
    
    # print df
    # print '' # Create a blank line between outputs
    # print df + s
    
    # print("df -> ")
    print(df)
    # print("type(df) - {}".format(type(df)))
    # type(df) - <class 'pandas.core.frame.DataFrame'>

    print("")
    
    # print("df + s -> ")
    print(df + s)
    # print("type(df + s) - {}".format(type(df + s)))
    # type(df + s) - <class 'pandas.core.frame.DataFrame'>

    print("")
    
# Adding when DataFrame column names don't match Series index
# Result large Pandas DataFrame all Nan 
if False :
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        'a': [10, 20, 30, 40],
        'b': [50, 60, 70, 80],
        'c': [90, 100, 110, 120],
        'd': [130, 140, 150, 160]
    })
    
    # print df
    # print '' # Create a blank line between outputs
    # print df + s

    print("df -> ")
    print(df)
    # print("type(df) - {}".format(type(df)))
    # type(df) - <class 'pandas.core.frame.DataFrame'>
    
    print("")
    
    print("df + s -> ")
    print(df + s)
    # print("type(df + s) - {}".format(type(df + s)))
    # type(df + s) - <class 'pandas.core.frame.DataFrame'>

    print("")


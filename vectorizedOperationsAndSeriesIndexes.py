import pandas as pd

# Change False to True for each block of code to see what it does

# Addition when indexes are the same
if False:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
    # print s1 + s2
    print("")
    print("s1 + s2 ->")
    print(s1 + s2)
    print("")


# Indexes have same elements in a different order
# addition by index NOT position
if False:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['b', 'd', 'a', 'c'])
    # print s1 + s2
    print("")
    print("s1 + s2 ->")
    print(s1 + s2)
    print("")


# Indexes overlap, but do not have exactly the same elements
# Note Nan
if False:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
    # print s1 + s2
    print("..")
    print("s1 + s2 ->")
    # a NaN, b NaN, c 13.0, d 24.0, e NaN, f NaN
    print(s1 + s2)

# Get rid of Nan, missing values removed 
if True:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
    # print s1 + s2
    print("44")
    # print("s1 + s2 ->")
    # a NaN, b NaN, c 13.0, d 24.0, e NaN, f NaN
    # print(s1 + s2)
    mySum = s1 + s2
    
    print("mySum ->")
    print(mySum)
    print("")
    
    print("mySum.dropna() ->")
    print(mySum.dropna())
    print("")
    
    print("mySum.fillna(0) ->")
    print(mySum.fillna(0))
    print("")
    
    print("s1.add(s2, fill_value = 0) ->")
    print(s1.add(s2, fill_value = 0))
    print("")
    
    # type(mySum) - <class 'pandas.core.series.Series'>
    # print("type(mySum) - {}".format(type(mySum)))

    
    #type(mySum) - <class 'pandas.core.series.Series'>
    # print("type(mySum) - {}".format(type(mySum)))


# Indexes do not overlap
# a NaN, b NaN, c NaN, d NaN, e NaN, f NaN
if False:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['e', 'f', 'g', 'h'])
    # print s1 + s2
    print("")
    print("s1 + s2 ->")
    print(s1 + s2)
    
    
    
    
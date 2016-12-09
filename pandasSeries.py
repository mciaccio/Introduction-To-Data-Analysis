import pandas as pd

countries = ['Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
             'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
             'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
             'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia']

life_expectancy_values = [74.7,  75. ,  83.4,  57.6,  74.6,  75.4,  72.3,  81.5,  80.2,
                          70.3,  72.1,  76.4,  68.1,  75.2,  69.8,  79.4,  70.8,  62.7,
                          67.3,  70.6]

gdp_values = [ 1681.61390973,   2155.48523109,  21495.80508273,    562.98768478,
              13495.1274663 ,   9388.68852258,   1424.19056199,  24765.54890176,
              27036.48733192,   1945.63754911,  21721.61840978,  13373.21993972,
                483.97086804,   9783.98417323,   2253.46411147,  25034.66692293,
               3680.91642923,    366.04496652,   1175.92638695,   1132.21387981]

# Life expectancy and gdp data in 2007 for 20 countries
life_expectancy = pd.Series(life_expectancy_values)
gdp = pd.Series(gdp_values)

# Change False to True for each block of code to see what it does

print("")

# Accessing elements and slicing
if True:
    print("life_expectancy[0] - {}\n".format(life_expectancy[0]))
    # type(life_expectancy) - <class 'pandas.core.series.Series'>
    # print("type(life_expectancy) - {}".format(type(life_expectancy)))
    # <class 'numpy.float64'>
    # print("type(life_expectancy[0]) - {}".format(type(life_expectancy[0])))

    # print("gdp[3:6] - {}\n".format(gdp[3:6]))
    print(gdp[3:6])
    print("")
    
# Looping
if True:
    for country_life_expectancy in life_expectancy:
        print ('country_life_expectancy - {}'.format(country_life_expectancy))
        # print ('Examining life expectancy {}\n'.format(country_life_expectancy))
print("")
        
# Pandas functions
if True:
    print("life_expectancy.mean() - {}".format(life_expectancy.mean()))
    print("life_expectancy.std() - {}\n".format(life_expectancy.std()))
    print("gdp.max() - {}".format(gdp.max()))
    print("gdp.sum() - {}\n".format(gdp.sum()))

# Vectorized operations and index arrays
if True:
    a = pd.Series([1, 2, 3, 4])
    b = pd.Series([1, 2, 1, 2])
    
    # 0 - 3 will be the index zero based indexing 
    print("a ->")
    print(a)
    print("")
    
    print("b ->")
    print(b)
    print("")

    print("a + b ->")
    print(a + b)
    print("")
    
    print("a * 2 ->")
    print(a * 2)
    print("")

    print("a >= 3 ->")
    print(a >= 3)
    print("")
    
    print("a[a >= 3] ->")
    print(a[a >= 3])
    print("")
    
    
def variable_correlation(variable1, variable2):
    '''
    Fill in this function to calculate the number of data points for which
    the directions of variable1 and variable2 relative to the mean are the
    same, and the number of data points for which they are different.
    Direction here means whether each value is above or below its mean.
    
    You can classify cases where the value is equal to the mean for one or
    both variables however you like.
    
    Each argument will be a Pandas series.
    
    For example, if the inputs were pd.Series([1, 2, 3, 4]) and
    pd.Series([4, 5, 6, 7]), then the output would be (4, 0).
    This is because 1 and 4 are both below their means, 2 and 5 are both
    below, 3 and 6 are both above, and 4 and 7 are both above.
    
    On the other hand, if the inputs were pd.Series([1, 2, 3, 4]) and
    pd.Series([7, 6, 5, 4]), then the output would be (0, 4).
    This is because 1 is below its mean but 7 is above its mean, and
    so on.
    '''
    num_same_direction = None        # Replace this with your code
    num_different_direction = None   # Replace this with your code
    
    return (num_same_direction, num_different_direction)

print("len(life_expectancy_values) - {}".format(len(life_expectancy_values)))
print("len(life_expectancy) - {}".format(len(life_expectancy))) 
print("life_expectancy.mean() - {}\n".format(life_expectancy.mean()))

print("len(gdp_values) - {}".format(len(gdp_values)))
print("len(gdp) - {}".format(len(gdp)))
print("gdp.mean() - {}\n".format(gdp.mean()))

print("life_expectancy[0] - {}".format(life_expectancy[0]))
print("gdp[0] - {}\n".format(gdp[0]))

num_same_direction = 0
num_different_direction = 0
life_expectancy_mean = life_expectancy.mean()
gdp_mean = gdp.mean()

# for i in range(0, 20):
for i in range(0, len(gdp)):
    #print("i - {}".format(i))
    print("life_expectancy[i] - {}".format(life_expectancy[i]))
    print("gdp[i] - {}\n".format(gdp[i]))
    if ((life_expectancy[i] > life_expectancy_mean) and (gdp[i] > gdp_mean)) or ((life_expectancy[i] < life_expectancy_mean) and (gdp[i] < gdp_mean)):
        num_same_direction += 1
    elif ((life_expectancy[i] < life_expectancy_mean) and (gdp[i] > gdp_mean)) or ((life_expectancy[i] > life_expectancy_mean) and (gdp[i] < gdp_mean)):
        num_different_direction += 1
        
print("num_same_direction - {}".format(num_same_direction))
print("num_different_direction - {}\n".format(num_different_direction))

# instructor solution 
both_above = (life_expectancy > life_expectancy.mean()) & (gdp > gdp.mean())
both_below = (life_expectancy < life_expectancy.mean()) & (gdp < gdp.mean())
print("both_above - {}".format(both_above)) # False True False ...
print("both_below - {}".format(both_below)) # False False False ...
# typboth_above() - <class 'pandas.core.series.Series'>
# print("type(both_above()) - {}".format(type(both_above)))
is_same_direction = both_above | both_below
print("is_same_direction - {}".format(is_same_direction))
print("len(is_same_direction) - {}".format(len(is_same_direction))) # has all 20 True AND False
# type(is_same_direction) - <class 'pandas.core.series.Series'>
# print("type(is_same_direction) - {}".format(type(is_same_direction)))
# How many are True?
num_same_direction = is_same_direction.sum()
print("num_same_direction - {}\n".format(num_same_direction)) # counted the 17 True, ignored the 3 False     
# print("len(num_same_direction) - {}".format(len(num_same_direction)))
# type(num_same_direction) - <class 'numpy.int64'>
# print("type(num_same_direction) - {}".format(type(num_same_direction)))

print("Panda Series - has index!")
myList = [74.7, 75., 83.4, 57.600001]
myIndex = ['Albania', 'Algeria', 'Andorra', 'Angola'] # on left see below
life_expectancy_panda_series = pd.Series(myList, myIndex)
print("life_expectancy -")
print(life_expectancy_panda_series)
print("")
#type(life_expectancy) - <class 'pandas.core.series.Series'>
#print("type(life_expectancy) - {}".format(type(life_expectancy)))

print("life_expectancy[0] (element (position) of panda series) - {}\n".format(life_expectancy[0]))
# type(life_expectancy[0]) - <class 'numpy.float64'>
# print("type(life_expectancy[0]) - {}\n".format(type(life_expectancy[0])))

print("element (index, Angola is in myIndex - life_expectancy_panda_series.loc['Angola'] -")
print(life_expectancy_panda_series.loc['Angola'])
print("")

print("element (POSITION, the zeroth POSITION ) - life_expectancy[0] -")
print(life_expectancy[0])
print("")

# type(life_expectancy_panda_series) - <class 'pandas.core.series.Series'>
# print("type(life_expectancy_panda_series) - {}".format(type(life_expectancy_panda_series)))
print("element (POSITION, zeroth POSITION) - life_expectancy_panda_series.iloc[0] -")
print(life_expectancy_panda_series.iloc[0])
print("element (POSITION, zeroth POSITION) - life_expectancy_panda_series[0] -")
print(life_expectancy_panda_series[0])
print("")
















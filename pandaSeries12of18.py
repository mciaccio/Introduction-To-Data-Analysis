'''
Created on Jan 8, 2017

@author: Menfi
'''

print("\nBegin\n")  

import pandas as pd
import numpy as np

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

# Example instantiate (create) and populate a Panda Series, Python list -> Panda Series  
# Life expectancy and gdp data in 2007 for 20 countries
life_expectancy = pd.Series(life_expectancy_values)

# Example instantiate (create) and populate a Panda Series, Python list -> Panda Series  
# Life expectancy and gdp data in 2007 for 20 countries
# Example *** describe() *** used with *** Panda Series *** 
gdp = pd.Series(gdp_values)
print("type(gdp) - {}".format(type(gdp)))
print("gdp.describe() -> ")
print(gdp.describe())
print("")

# Change False to True for each block of code to see what it does

# Accessing elements and slicing
if False:
    # print life_expectancy[0]
    # print("life_expectancy[0] - {}\n".format(life_expectancy[0]))

    # Example, slice, bracket, colon fourth one (zero based indexing), do not include the sixth (zero based indexing) 
    # print gdp[3:6]
    print("gdp[3:6] - {}\n".format(gdp[3:6]))

    
# Looping
if False:
    for country_life_expectancy in life_expectancy:
        print ('Examining life expectancy - {}'.format(country_life_expectancy))
        
# Pandas functions
# Example Pandas math functions
if False:
    # print life_expectancy.mean()
    print("life_expectancy.mean() - {}".format(life_expectancy.mean()))
    
    # print life_expectancy.std()
    print("life_expectancy.std() - {}".format(life_expectancy.std()))
    
    # print gdp.max()
    print("gdp.max() - {}".format(gdp.max()))

    # print gdp.sum()
    print("gdp.sum() - {}".format(gdp.sum())) 
    
    
# Vectorized operations and index arrays
# Example Panda Series, Vectorized operations and index arrays
if True:
    a = pd.Series([1, 2, 3, 4])
    b = pd.Series([1, 2, 1, 2])
  
    # print a + b
    # Example add two Panda Series, get zero the index on the left 
    print("a + b -> ")
    print(a + b)
    print("")

    # print a * 2
    # Example multiple Panda Series times a scalar, get zero the index on the left 
    print("a * 2 -> ")
    print(a * 2)
    print("")

    # print a >= 3
    # Example Panda Series index array, True, False ..., *** dtype: bool ***, boolean, get zero the index on the left
    print("a >= 3 -> ")
    print(a >= 3)
    print("")

    # Example Panda Series, prints *** elements *** that match the criteria of the index array, True, False ..., get the zero based index on the left
    # print a[a >= 3]
    print("a[a >= 3] -> ")
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


lifeExpectancyBool = life_expectancy >= life_expectancy.mean()
print("type(lifeExpectancyBool) - {}".format(type(lifeExpectancyBool)))
print("len(lifeExpectancyBool) - {}".format(len(lifeExpectancyBool)))
print("lifeExpectancyBool -> ")
print(lifeExpectancyBool)
print("")

gdpBool = gdp >= gdp.mean()
print("type(gdpBool) - {}".format(type(gdpBool)))
print("len(gdpBool) - {}".format(len(gdpBool)))
print("gdpBool -> ")
print(gdpBool)
print("")

print("type(lifeExpectancyBool & gdpBool) - {}".format(type(lifeExpectancyBool & gdpBool)))
print("lifeExpectancyBool & gdpBool -> ")
print(lifeExpectancyBool & gdpBool)
print("")

print("np.sum(lifeExpectancyBool & gdpBool) -> ")
print(np.sum(lifeExpectancyBool & gdpBool))
print("")

num_same_direction = np.sum(lifeExpectancyBool & gdpBool)
print("num_same_direction - {}".format(num_same_direction))

# print("type(num_same_direction) - {}".format(type(num_same_direction)))
# print("len(lifeExpectancyBool & gdpBool) - {}".format(len(lifeExpectancyBool & gdpBool)))

num_different_direction = len(lifeExpectancyBool & gdpBool) - num_same_direction 
print("num_different_direction - {}".format(num_different_direction))


print("type(lifeExpectancyBool  gdpBool) - {}".format(type(lifeExpectancyBool & gdpBool)))
print("lifeExpectancyBool & gdpBool -> ")
print(lifeExpectancyBool & gdpBool)
print("")


# print("type(lifeExpectancyBool) - {}".format(type(lifeExpectancyBool)))
#      type(lifeExpectancyBool) - <class 'pandas.core.series.Series'>

# Example iterate, loop through Panda Series getting *** both *** index and value 
# Series.iteritems()[source]
# Lazily iterate over (index, value) tuples

num_different_direction = 0
for index, value in lifeExpectancyBool.iteritems():
    print("index - {}, value - {}".format(index, value))
    print("xxx- {}".format(gdpBool[index]))
    if value != gdpBool[index]:
        num_different_direction +=1

print("num_different_direction - {}".format(num_different_direction))
print("len(lifeExpectancyBool) - {}".format(len(lifeExpectancyBool)))
print("len(gdpBool) - {}".format(len(gdpBool)))
num_same_direction = len(gdpBool) - num_different_direction 
print("num_same_direction - {}\n".format(num_same_direction))

# instructor solution 

# corresponding values (same index), in different Panda Series, if BOTH *** & *** True both_above index vaue = True 
both_above = (life_expectancy > life_expectancy.mean()) & (gdp > gdp.mean()) 
print("both_above - {} ->")
print(both_above)
# print("type(both_above) - {}".format(type(both_above)))
#        type(both_above) - <class 'pandas.core.series.Series'>

lifeBelow = life_expectancy < life_expectancy.mean()
gdpBelow = gdp < gdp.mean()

print("lifeBelow -> ")
print(lifeBelow)
print("")

print("gdpBelow -> ")
print(gdpBelow)
print("")

# corresponding values (same index), in different Panda Series, if BOTH *** & *** True both_below index vaue = True 
both_below = (life_expectancy < life_expectancy.mean()) & (gdp < gdp.mean()) 
print("both_below - {} ->")
print(both_below)

# If True in EITHER Panda Series *** not or | *** populate is_same_direction Panda Series with True
is_same_direction = both_above | both_below
print("is_same_direction -> ")
print(is_same_direction)
print("")

# Finally count up all the True - get a count of all True in is_same_direction 
print("is_same_direction.sum() -> ")
print(is_same_direction.sum())

# Different direction = length - same direction 
print("num_different_direction -> ")
print(len(life_expectancy) -  is_same_direction.sum())
print("") 




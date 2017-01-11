'''
Created on Jan 10, 2017

@author: Menfi
'''


print("\nBegin\n")

import numpy as np
import pandas as pd

# Example - declare, create instantiate NumPy Array, Python list -> NumPy Array
myNumPyArray = np.array([1,2,3,4])
print("myNumPyArray - {}\n".format(myNumPyArray))
# print("type(myNumPyArray) - {}".format(type(myNumPyArray)))
#        type(myNumPyArray) - <class 'numpy.ndarray'>

# Example - declare, create instantiate Pandas Series, Python list -> Pandas Series, no hard coded index attribute, hence index 0, 1, 2 ...
myPandasSeries = pd.Series([5,6,7,8])
print("myPandasSeries -> ")
print(myPandasSeries)
print("")
'''
*** position zero NOT index zero 
myPandasSeries -> 
0    5
1    6
2    7
3    8
dtype: int64
'''
# print("type(myPandasSeries ) - {}".format(type(myPandasSeries )))
#        type(myPandasSeries ) - <class 'pandas.core.series.Series'>

# Example - Panda Series describe() function
print("myPandasSeries.describe() -> ")
print(myPandasSeries.describe())
print("")

# Example - declare, create instantiate Panda Series, Python list -> Pandas Series, with hard coded index, Country Names (Albania ...) are the index of the Panda Series
life_expectancy = pd.Series([74.7,75., 83.4, 57.6],
    index = ['Albania', 'Algeria', 'Andorra', 'Angola'])
print('life_expectancy -> ')
print(life_expectancy)

# index value (Albania ...) matched to corresponding data point (74.7 ...) 
# life_expectancy -> 
# Albania    74.7
# Algeria    75.0
# Andorra    83.4
# Angola     57.6
# dtype: float64

print('')

# Example - access Panda series element by position, location "zero based indexing", hard coded index not used 
life_expectancy[0]
print('Access Panda Series by POSITION, see *** iloc for best pratcice *** - *** position zero *** bracket - life_expectancy[0] - {}\n'.format(life_expectancy[0]))
# life_expectancy[0] - 74.7
# print("type(life_expectancy[0]) - {}".format(type(life_expectancy[0])))
#        type(life_expectancy[0]) - <class 'numpy.float64'>

# Example - access Panda series element by LOCATION *** loc, .loc dot loc, dotloc *** bracket   
print('Access Panda Series, access element by - *** loc, .loc dot loc, dotloc ***, bracket, life_expectancy.loc["Angola"] - {} \n'.format(life_expectancy.loc['Angola']))

# Example - access Panda Series by POSITION *** iloc, eyeloc, .iloc dot iloc, dotiloc ***
print('Access Panda Series, access element by POSITION, best practice - *** iloc, eyeloc, .iloc dot iloc, dotiloc ***, bracket, life_expectancy.iloc[1] - {}'.format(life_expectancy.iloc[1]))
print(life_expectancy.iloc[1])
# 75.0
print("")


# Example using a Python list for Panda Series index
countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
]

# Example using a Python list for PandaSeies Values 
employment_values = [
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
]

# Example using a *** Python list for Panda Seies Values, using a Python list for Panda Series index ***, declare, create instantiate
# Employment data in 2007 for 20 countries
employment = pd.Series(employment_values, index=countries)

def max_employment(employment):
    '''
    Fill in this function to return the name of the country
    with the highest employment in the given employment
    data, and the employment in that country.
    
    The input will be a Pandas series where the values
    are employment and the index is country names.
    
    Try using the Pandas argmax() function. Documention is
    here: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.argmax.html
    '''
    max_country = None      # Replace this with your code
    max_value = None   # Replace this with your code

    return (max_country, max_value)

# print("type(employment) - {}".format(type(employment)))
#        type(employment) - <class 'pandas.core.series.Series'>


# Example - access Panda Series maximum VALUE using .max(), dot max() 
print('employment.max() -> ')
print(employment.max())
print("")

# Example - access Panda Series POSITION, *** index ***, maximum value, corresponding to the maximum value, .argmax()
print('employment.argmax() -> ')
print(employment.argmax())
print("")

# instructor
max_country = employment.argmax()
print("max_country -> ")
print(max_country)

# Example best practices, instructor method, accessing Panda Series value by location *** loc, .loc, dotloc, *** 
max_value = employment.loc[max_country]
print("max_value -> ")
print(max_value)
print("") 
    

 














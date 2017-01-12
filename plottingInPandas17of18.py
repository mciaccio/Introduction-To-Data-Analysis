'''
Created on Jan 12, 2017

@author: Menfi
'''   
 
import pandas as pd
import seaborn as sns

# The following code reads all the Gapminder data into Pandas DataFrames. You'll
# learn about DataFrames next lesson.

path = '/datasets/ud170/gapminder/'
employment = pd.read_csv(path + 'employment_above_15.csv', index_col='Country')
female_completion = pd.read_csv(path + 'female_completion_rate.csv', index_col='Country')
male_completion = pd.read_csv(path + 'male_completion_rate.csv', index_col='Country')
life_expectancy = pd.read_csv(path + 'life_expectancy.csv', index_col='Country')
gdp = pd.read_csv(path + 'gdp_per_capita.csv', index_col='Country')

# The following code creates a Pandas Series for each variable for the United States.
# You can change the string 'United States' to a country of your choice.

employment_us = employment.loc['United States']
female_completion_us = female_completion.loc['United States']
male_completion_us = male_completion.loc['United States']
life_expectancy_us = life_expectancy.loc['United States']
gdp_us = gdp.loc['United States']

# Uncomment the following line of code to see the available country names
# print employment.index.values
print("employment.index.values - {}".format(employment.index.values))

print("type(employment.index.values) - {}".format(type(employment.index.values)))
#   type(employment.index.values) - <type 'numpy.ndarray'>

# print("type(employment) - {}".format(type(employment)))
#        type(employment) - <class 'pandas.core.frame.DataFrame'>
# print("type(employment_us) - {}".format(type(employment_us)))
#        type(employment_us) - <class 'pandas.core.series.Series'>

# Use the Series defined above to create a plot of each variable over time for
# the country of your choice. You will only be able to display one plot at a time
# with each "Test Run".

# Example Panda Series histogram - worked in udacity browser only, data files not downloaded locally to Mac  
employment_us.hist()



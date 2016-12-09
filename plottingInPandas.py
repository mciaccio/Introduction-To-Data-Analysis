


# this will not work in eclipse
# this DID work in the udacity browser - all 5 plots generated
# this file is for documentation, reference  ONLY.
# see .plot() below

# more notes from lecture
# import matplotlib.pyplot as plt
# plt.hist(data) - data - NumPy Array OR Pandas Series

# data Pandas Series
# data.hist()
# data.plot()



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

# Use the Series defined above to create a plot of each variable over time for
# the country of your choice. You will only be able to display one plot at a time
# with each "Test Run".


# all of these worked
# employment_us.plot()
# female_completion_us.plot()
# male_completion_us.plot()
# life_expectancy_us.plot()
gdp_us.plot()

# years or index of series - labels for the x axis, values on the y axis 


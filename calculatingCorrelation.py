
import os
import pandas as pd
import numpy as np



DATADIR = '/Users/Menfi/Documents/gitBaseDirectory/IntroToDataAnalysis/dataFiles/twoDimensional'

SUBWAY_FN = 'nyc_subway_weather.csv'
SUBWAY_DF = os.path.join(DATADIR, SUBWAY_FN)

"""
loadingDataIntoADataFrame.py
 
DataFrames good representation of csv file.
Two dimensional, different Type for each column.

import pandas as pd
load csv into DataFrame 
pd.read_csv('filename.csv')
pd.read_csv('nyc_subway_weather.csv')

head() - returns smaller DataFrame
subway_def.head() - column headers, integer index on left 
subway_def.describe() - statistics about each column (mean, standard deviation) 

"""

"""
When standardizing both X and Y - need to pass argument ddof = 0 
to Panda's Standard Deviation function
Controls "corrected -  ddof = 1" or "uncorrected -  ddof = 0" Standard Deviation calculation.
When calculation Pearson's r - use the Standard Deviation
Bessel's correction turned off.

NumPy's corrcoef() function can be used to calculate Pearson's r, also known as the correlation coefficient.
"""

print("")

# filename = '/datasets/ud170/subway/nyc_subway_weather.csv'
subway_df = pd.read_csv(SUBWAY_DF)
print("subway_df.sample(1) -> ")
 
# print("type(subway_df) -> {}".format(type(subway_df)))
# <class 'pandas.core.frame.DataFrame'>

print(subway_df.sample(1))
print("")


def correlation(x, y):
    '''
    input x and y - twp panda series 
    Fill in this function to compute the correlation between the two
    input variables. Each input is either a NumPy array or a Pandas
    Series.
    
    correlation = average of (x in standard units) times (y in standard units)
    
    Remember to pass the argument "ddof=0" to the Pandas std() function!
    '''
    
    print("x ->")
    # print(x)
    # 0          0.0
    # 1          0.0
    # print("type(x) - {}".format(type(x)))
    # type(x) - <class 'pandas.core.series.Series'>
    print("")
    
    print("y ->")
    # print(y)
    # 0        0.000000
    # 1        0.000000
    print("type(y) - {}".format(type(y)))
    # type(y) - <class 'pandas.core.series.Series'>
    print("")
    
    # first standardize both x and y - get the standard deviation of the values passed in the 
    # x arguments and the y argument 
    # simple - standard deviation 
    # ddof=0 - Bessel's correction turned off
    std_x = (x - x.mean()) / x.std(ddof=0) # Bessel's correction turned off
    
    print("std_x -> ")
    # print(std_x)
    """
    0       -0.639013
    1       -0.639013
    """
    
    # print("type(std_x) - {}".format(type(std_x)))
    # type(std_x) - <class 'pandas.core.series.Series'>
    print("")

    # first standardize both x and y
    # simple - standard deviation using Bessel's correction turned off
    std_y = (y - y.mean()) / y.std(ddof=0)  # Bessel's correction turned off
    print("std_y -> ")
    # print(std_y)
    """
    std_y ->
    0       -0.282530
    1       -0.282530
    """
    # print("type(std_y) - {}".format(type(std_y)))
    # type(std_y) - <class 'pandas.core.series.Series'>
    print("")
    
    # correlation = average of (  (x in standard units) times (y in standard units)  )
    
    # vectorized multiplication
    (std_x * std_y)
    # average of products 
    (std_x * std_y).mean()
    
    # correlation coefficient, Pearson's r 
    pearsonsRcorrelationCoefficient = (std_x * std_y).mean() 
    
    print("Pearson's R Correlation Coeficient")
    print("pearsonsRcorrelationCoefficient -> ")
    print(pearsonsRcorrelationCoefficient)
    # x - 0.03564851577223041

    # print("type(x) - {}".format(type(x)))
    # type(x) - <class 'float'>

    
    return None


entries = subway_df['ENTRIESn_hourly']
print("entries -> ")
# print(entries)
"""
entries - {} -> 
5         15.0
6         19.0
"""

# print(entries.describe())
"""
count    42649.000000
mean      1886.589955
std       2952.385585
min          0.000000
25%        274.000000
50%        905.000000
75%       2255.000000
max      32814.000000
Name: ENTRIESn_hourly, dtype: float64
"""

print("")
# <class 'pandas.core.series.Series'>
# print("type(entries) - {}".format(type(entries)))


cum_entries = subway_df['ENTRIESn']
print("cum_entries -> ")

# print(cum_entries)
"""
cum_entries - {} -> 
0        4388333
1        4388333
"""

# print(cum_entries.describe())
""""
cum_entries - {} -> 
count    4.264900e+04
mean     2.812486e+07
std      3.043607e+07
min      0.000000e+00
25%      1.039762e+07
50%      1.818389e+07
75%      3.263049e+07
max      2.357746e+08
Name: ENTRIESn, dtype: float64
"""


print("")
# <class 'pandas.core.series.Series'>
# print("type(cum_entries) - {}".format(type(cum_entries)))

"""
rain - {} -> 
0        0.000000
1        0.000000
"""
rain = subway_df['meanprecipi']
print("rain -> ")
# print(rain)
# print("type(rain) - {}".format(type(rain)))
# <class 'pandas.core.series.Series'>
print("")

"""
temp - {} -> 
0        55.980000
1        55.980000
"""
temp = subway_df['meantempi']
print("temp -> ")
# print(temp)
print("")
# type(temp) - <class 'pandas.core.series.Series'>
# print("type(temp) - {}".format(type(temp)))


# print correlation(entries, rain)
# print("correlation(entries, rain) - {}".format(correlation(entries, rain)))

correlation(entries, rain)
np.corrcoef(entries, rain)
print("np.corrcoef(entries, rain) -> ")
print(np.corrcoef(entries, rain))
print("11")

# correlation coeficient, Pearson's r - x - 0.03564851577223041
# precipitation and ridership go higher together - only 0.03 relationship NOT strong

# print correlation(entries, temp)
# print("correlation(entries, temp) - {}".format(correlation(entries, temp)))

# correlation(entries, temp)
# correlation coeficient, Pearson's r - x - -0.026693348321569912

# print correlation(rain, temp)
# print("correlation(rain, temp) - {}".format(correlation(rain, temp)))
# correlation(rain, temp)
# correlation coeficient, Pearson's r - x - -0.22903432340833663

# print correlation(entries, cum_entries)
# print("correlation(entries, cum_entries) - {}".format(correlation(entries, cum_entries)))
# correlation(entries, cum_entries)
# correlation coeficient, Pearson's r - x - 0.5858954707662182

x = 5
print("x - {}".format(x))
print("type(x) - {}".format(type(x)))


"""
github import pandas - csv file - Pearsons r - correlation coefficient
"""

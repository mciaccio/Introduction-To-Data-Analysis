'''
Created on Jan 13, 2017

@author: Menfi
'''

# github correlation coefficient Pearson's r, uncorrected standard deviation (ddof = 0), manually AND *** numPy - np.corrcoef(x,y)) ***

print("\nBegin\n")

import numpy as np
import pandas as pd

# filename = '/datasets/ud170/subway/nyc_subway_weather.csv'
filename = '/Users/Menfi/Documents/gitBaseDirectory/IntroToDataAnalysis/dataFiles/twoDimensional/nyc_subway_weather.csv'
# filename = '/Users/Menfi/Documents/gitBaseDirectory/IntroToDataAnalysis/dataFiles/twoDimensional/short'
# filename = '/Users/Menfi/Documents/gitBaseDirectory/IntroToDataAnalysis/dataFiles/twoDimensional/shorter'

subway_df = pd.read_csv(filename)

# Example - Pandas DataFrame head() method 
# print("type(subway_df) - {}".format(type(subway_df)))
#        type(subway_df) - <class 'pandas.core.frame.DataFrame'>
print("subway_df.head() -> ")
print(subway_df.head())
print("")

# Example - Pandas DataFrame describe() method 
print("subway_df.describe() -> ")
print(subway_df.describe())
print("")


def correlation(x, y):
    '''
    Fill in this function to compute the correlation between the two
    input variables. Each input is either a NumPy array or a Pandas
    Series.
    
    correlation = average of (x in standard units) times (y in standard units)
    
    Remember to pass the argument "ddof=0" to the Pandas std() function!
    '''
    
    print("x -> ")
    print(x)
    print("type(x) - {}".format(type(x)))
    #      type(x) - <class 'pandas.core.series.Series'>
    print("")

    xMean = x.mean()
    print("xMean -> ")
    print(xMean)
    # print("type(xMean) - {}".format(type(xMean)))
    #        type(xStandardDeviation) - <class 'float'>
    print("")
    
    xDifferenceFromMean = x - xMean 
    print("xDifferenceFromMean -> ")
    print(xDifferenceFromMean)
    print("type(xDifferenceFromMean) - {}".format(type(xDifferenceFromMean)))
    #      type(xDifferenceFromMean) - <class 'pandas.core.series.Series'>
    print("")
    
    xStandardDeviation = x.std(ddof = 0)
    print("xStandardDeviation -> ")
    print(xStandardDeviation)
    # print("type(xStandardDeviation) - {}".format(type(xStandardDeviation)))
    #        type(xStandardDeviation) - <class 'float'>
    print("")

    xStandardDeviationsAwayFromMean = (xDifferenceFromMean / xStandardDeviation)   
    print("xStandardDeviationsAwayFromMean -> ")
    print(xStandardDeviationsAwayFromMean)
    print("type(xStandardDeviationsAwayFromMean) - {}".format(type(xStandardDeviationsAwayFromMean)))
    #      type(xStandardDeviationsAwayFromMean) - <class 'pandas.core.series.Series'>
    print("")
    
    print("type(y) - {}".format(type(y)))
    yMean = y.mean()
    print("yMean -> ")
    print(yMean)
    # print("type(yMean) - {}".format(type(yMean)))
    #        type(yMean) - <class 'float'>

    yDifferenceFromMean = y - yMean 
    print("yDifferenceFromMean -> ")
    print(yDifferenceFromMean)
    # print("type(yDifferenceFromMean) - {}".format(type(yDifferenceFromMean)))
    #        type(yDifferenceFromMean) - <class 'pandas.core.series.Series'>      

    yStandardDeviation = y.std(ddof = 0)
    print("yStandardDeviation -> ")
    print(yStandardDeviation)
    # print("type(yStandardDeviation) - {}".format(type(yStandardDeviation)))
    #        type(yStandardDeviation) - <class 'float'>

    print("")

    yStandardDeviationsAwayFromMean = (yDifferenceFromMean / yStandardDeviation)       
    print("yStandardDeviationsAwayFromMean -> ")
    print(yStandardDeviationsAwayFromMean)
    # print("type(yStandardDeviationsAwayFromMean) - {}".format(type(yStandardDeviationsAwayFromMean)))
    #        type(yStandardDeviationsAwayFromMean) - <class 'pandas.core.series.Series'>

    productStandardDeviationsFromMean = (xStandardDeviationsAwayFromMean * yStandardDeviationsAwayFromMean) 
    # Example correlation coefficient, Pearson's r working example done manually   
    pearsonR = np.mean(productStandardDeviationsFromMean)
    print("pearsonR -> ")
    print(pearsonR)
    # print("type(pearsonR) - {}".format(type(pearsonR)))
    # type(pearsonR) - <class 'float'>
    print("")

    return None

entries = subway_df['ENTRIESn_hourly']
cum_entries = subway_df['ENTRIESn']
rain = subway_df['meanprecipi']
temp = subway_df['meantempi']

# print correlation(entries, rain)
# print("correlation(entries, rain) -> ")
# print(correlation(entries, rain)) # None
# print("")

# print correlation(entries, temp)
# print("correlation(entries, temp -> ")
# print(correlation(entries, temp))
# print("")

# print correlation(rain, temp)
# print("correlation(rain, temp) -> ")
# print(correlation(rain, temp))
# print("")

# print correlation(entries, cum_entries)
print("correlation(entries, cum_entries) -> ")
# Example - working example, correlation coefficient, Pearson's r, numPy *** np.corrcoef(x,y) *** *** NOT done manually *** best practices *** 
print(np.corrcoef(entries, cum_entries))
# [[ 1.          0.58589547]
# [ 0.58589547  1.        ]]
print(correlation(entries, cum_entries))
print("")

x = pd.Series([1, 2, 3, 4]) 
y = pd.Series([10, 11, 12, 13])
# correlation(x, y)

# Example - working example, correlation coefficient, Pearson's r, numPy *** np.corrcoef(x,y) ***
# print("type(x) - {}".format(type(x)))
#       type(x) - <class 'pandas.core.series.Series'>
# print("type(y) - {}".format(type(y)))
#        type(y) - <class 'pandas.core.series.Series'>
# print("np.corrcoef(x,y) -> ")
# print(np.corrcoef(x,y))
# print("type(np.corrcoef(x,y)) - {}".format(type(np.corrcoef(x,y))))
#      type(np.corrcoef(x,y)) - <class 'numpy.ndarray'>
print("")




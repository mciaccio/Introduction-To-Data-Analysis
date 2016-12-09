

# vectorized operations
#standardized values - standardizedValues = (values - values.mean()) / values.std()
import numpy as np

# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])

# Change this country name to change what country will be printed when you
# click "Test Run". Your function will be called to determine the standardized
# score for this country for each of the given 5 Gapminder variables in 2007.
# The possible country names are available in the Downloadables section.

country_name = 'United States'

def standardize_data(values):
    '''
    Fill in this function to return a standardized version of the given values,
    which will be in a NumPy array. Each value should be translated into the
    number of standard deviations that value is away from the mean of the data.
    (A positive number indicates a value higher than the mean, and a negative
    number indicates a value lower than the mean.)
    '''
    return None

print()
print("employment[0] - {}".format(employment[0]))

employmentArrayMean = employment.mean()
print("employmentArrayMean - {}".format(employmentArrayMean))
# type(employmentArrayMean) - <class 'numpy.float64'>
# print("type(employmentArrayMean) - {}\n".format(type(employmentArrayMean)))

employmentArrayStandardDeviation = employment.std()
print("employmentArrayStandardDeviation - {}\n".format(employmentArrayStandardDeviation))
# type(employmentArrayStandardDeviation) - <class 'numpy.float64'>
# print("type(employmentArrayStandardDeviation) - {}".format(type(employmentArrayStandardDeviation)))

# how far from the mean
meanArithmeticDifferenceArray = employment - employmentArrayMean
print("meanArithmeticDifferenceArray - {}".format(meanArithmeticDifferenceArray))
print("meanArithmeticDifferenceArray[0] - {}\n".format(meanArithmeticDifferenceArray[0]))
# type(standardDeviationArithmeticDifference) - <class 'numpy.ndarray'>
# print("type(standardDeviationArithmeticDifferenceArray) - {}".format(type(standardDeviationArithmeticDifferenceArray)))

# how many standard deviations
howManyStandardDeviationsArray = meanArithmeticDifferenceArray / employmentArrayStandardDeviation 
print("howManyStandardDeviationsArray - {}".format(howManyStandardDeviationsArray))
print("howManyStandardDeviationsArray[0] - {}\n".format(howManyStandardDeviationsArray[0]))
# type(howManyStandardDeviationsArray) - <class 'numpy.ndarray'>
# print("type(howManyStandardDeviationsArray) - {}".format(type(howManyStandardDeviationsArray)))

values = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
myMean = values.mean()
myStandardDeviation = values.std()
print("myStandardDeviation - {}".format(myStandardDeviation))
# type(myStandardDeviation) - <class 'numpy.float64'>
# print("type(myStandardDeviation) - {}".format(type(myStandardDeviation)))

meanArithmeticDifferenceArray = (values - myMean)
print("meanArithmeticDifferenceArray - {}".format(meanArithmeticDifferenceArray))
# type(standardDeviationArithmeticDifferenceArray) - <class 'numpy.ndarray'>
# print("type(standardDeviationArithmeticDifferenceArray) - {}\n".format(type(standardDeviationArithmeticDifferenceArray)))

howManyStandardDeviationsArray = meanArithmeticDifferenceArray / myStandardDeviation 
print("howManyStandardDeviationsArray - {}".format(howManyStandardDeviationsArray))
# type(howManyStandardDeviationsArray) - <class 'numpy.ndarray'>
# print("type(howManyStandardDeviationsArray) - {}".format(type(howManyStandardDeviationsArray)))














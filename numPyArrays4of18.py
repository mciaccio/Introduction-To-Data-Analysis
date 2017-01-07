'''
Created on Jan 6, 2017

@author: Menfi
'''

import numpy as np

print("")

# Example create a populated numPy array, first create a native Python list - Python list -> numPy Array
# 
# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# Example create a populated numPy array, first create a native Python list - Python list -> numPy Array,
# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])

# Change False to True for each block of code to see what it does

# Accessing elements
if False:
    # print("type(countries) - {}".format(type(countries)))
    # type(countries) - <class 'numpy.ndarray'>

    # Numpy Array, access, index, access first, zeroth element 
    # print countries[0]
    print("countries[0] - {}".format(countries[0]))
    
    # Numpy Array, access, index, access fourth, zero based indexing 
    # print countries[3]
    print("countries[3] - {}\n".format(countries[3]))


# Slicing
if False:
    # print("type(countries) - {}".format(type(countries)))
    #        type(countries) - <class 'numpy.ndarray'>
    
    # Example Numpy Array, slice, colon, bracket, access first three elements  
    # print countries[0:3]
    print("countries[0:3] - {}".format(countries[0:3]))

    # Example Numpy Array, slice, colon, bracket, access first three elements  
    # print countries[:3]
    print("countries[:3] - {}".format(countries[:3]))

    # Example Numpy Array, slice, colon, bracket, eighteenth element through the end   
    # print countries[17:]
    print("countries[17:] - {}".format(countries[17:]))

    # Example Numpy Array, slice, colon, bracket, access all elements   
    # print countries[:]
    print("countries[:] - {}".format(countries[:]))


# Element types
# Example numPy Array, dtype, dtypes, dot dtype, .dtype
if False:
    # print countries.dtype
    print("countries.dtype - {}".format(countries.dtype))

    # print employment.dtype
    print("employment.dtype - {}".format(employment.dtype))

    # print np.array([0, 1, 2, 3]).dtype
    print("np.array([0, 1, 2, 3]).dtype - {}".format(np.array([0, 1, 2, 3]).dtype))

    # print np.array([1.0, 1.5, 2.0, 2.5]).dtype
    print("np.array([1.0, 1.5, 2.0, 2.5]).dtype - {}".format(np.array([1.0, 1.5, 2.0, 2.5]).dtype))
    
    # print np.array([True, False, True]).dtype
    print("np.array([True, False, True]).dtype - {}".format(np.array([True, False, True]).dtype))
    
    # print np.array(['AL', 'AK', 'AZ', 'AR', 'CA']).dtype
    print("np.array(['AL', 'AK', 'AZ', 'AR', 'CA']).dtype - {}".format(np.array(['AL', 'AK', 'AZ', 'AR', 'CA']).dtype))

 
# Looping
if False:
    # Example numPy array, iterate, loop 
    for country in countries:
        # print 'Examining country {}'.format(country)
        print("Examining country - {}".format(country))

# Example numPy array, iterate, loop, *** index ***, range, could be used to access part of, partial, some elements 
    for i in range(len(countries)):
        country = countries[i]
        country_employment = employment[i]
        # print 'Country {} has employment {}'.format(country, country_employment)
        print("Country - {}, has employment - {}".format(country, country_employment))

# Numpy functions
if False:
    # print employment.mean()
    print("employment.mean - {}".format(employment.mean()))

    # print employment.std()
    print("employment.std() - {}".format(employment.std()))
    
    # print employment.max()
    print("employment.max() - {}".format(employment.max()))

    # print employment.sum()
    print("employment.sum() - {}".format(employment.sum()))

def max_employment(countries, employment):
    '''
    Fill in this function to return the name of the country
    with the highest employment in the given employment
    data, and the employment in that country.
    '''
        
    # print("type(employment) - {}".format(type(employment)))
    #        type(employment) - <class 'numpy.ndarray'>
    
    # print("sorted(employment) - {}".format(sorted(employment)))
    print("employment.argmax() - {}".format(employment.argmax()))
    print("countries[employment.argmax()] - {}\n".format(countries[employment.argmax()]))
    # print("type(employment.argmax()) - {}".format(type(employment.argmax())))
    #        type(employment.argmax()) - <class 'numpy.int64'>

    countries[employment.argmax()]
    
    # max_country = None # Replace this with your code
    max_country = countries[employment.argmax()]
    print("max_country - {}".format(max_country))

    # max_value = None   # Replace this with your code
    max_value = employment[employment.argmax()]
    print("max_value - {}".format(max_value))

    return (max_country, max_value)


max_employment(countries, employment)

    
    
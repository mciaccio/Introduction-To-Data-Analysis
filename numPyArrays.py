import numpy as np

# python list -> NumPy Array conversion
# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# python list -> NumPy Array conversion
# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])

# Afghanistan
print (countries[0])

# Angola
print (countries[3])

# ['Afghanistan', 'Albania', 'Algeria']
print (countries[0:3])

# ['Afghanistan', 'Albania', 'Algeria']
print (countries[:3])

#['Bhutan', 'Bolivia','Bosnia and Herzegovina']
print (countries[17:])

# ['Afghanistan' 'Albania' 'Algeria' 'Angola' 'Argentina' 'Armenia'
#  'Australia' 'Austria' 'Azerbaijan' 'Bahamas' 'Bahrain' 'Bangladesh'
#  'Barbados' 'Belarus' 'Belgium' 'Belize' 'Benin' 'Bhutan' 'Bolivia'
#  'Bosnia and Herzegovina']
print (countries[:])
print("")

# type(countries) - <class 'numpy.ndarray'>
print("type(countries) - {}\n".format(type(countries)))

# countries.dtype - <U22
print("countries.dtype - {}".format(countries.dtype))

# <U2
print (np.array(['AL', 'AK', 'AZ', 'AR', 'CA', '12345']).dtype)


# employment.dtype - float64
print("employment.dtype - {}\n".format(employment.dtype))


for country in countries:
    print("country - {}".format(country))
print("")

for i in range(len(countries)):
    country = countries[i]
    country_employment = employment[i]
    print("{} has employment\t\t{}".format(country, country_employment))
    
print("")
print("employment.mean() - {}".format(employment.mean()))
print("employment.std() - {}".format(employment.std()))
print("employment.max() - {}".format(employment.max()))
print("employment.sum() - {}\n".format(employment.sum()))

myMaxEmployment = employment.max()
for i in range(len(employment)):
    if employment[i] ==  myMaxEmployment:
        print("i - {}, employment[i] - {}".format(i, employment[i]))
        print("i - {}, countries[i] - {}".format(i, countries[i]))
        max_country = countries[i]
        
print("")
print("employment.argmax() - {}".format(employment.argmax()))
idxMax = employment.argmax()
print("countries[employment.argmax()] - {}\n".format(countries[employment.argmax()]))

max_value = employment.max()
print("max_value - {}".format(max_value))

max_country = countries[employment.argmax()]
print("max_country - {}\n".format(max_country))

def max_employment(countries, employment):
    '''
    Fill in this function to return the name of the country
    with the highest employment in the given employment
    data, and the employment in that country.
    '''
    # max_country = None      # Replace this with your code
    # max_value = None   # Replace this with your code
    
    # max_value = employment.max()
    max_value = employment.max()
    max_country = countries[employment.argmax()]

    for i in range(len(employment)):
        if employment[i] ==  myMaxEmployment:
            # print("i - {}, employment[i] - {}".format(i, employment[i]))
            # print("i - {}, countries[i] - {}".format(i, countries[i]))
            max_country = countries[i]
            
            max_country = countries[employment.argmax()]
            
    print("max_country - {}".format(max_country))
    print("max_value - {}".format(max_value))
 
    return (max_country, max_value)

 










# print countries.dtype


















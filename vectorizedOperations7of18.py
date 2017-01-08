'''
Created on Jan 07, 2017

@author: Menfi
'''

print("\nBegin\n")

import numpy as np

# Change False to True for each block of code to see what it does

# Arithmetic operations between 2 NumPy arrays
if True:
    a = np.array([1, 2, 3, 4])
    b = np.array([1, 2, 1, 2])
    
    # print a + b
    # print("a + b - {}".format(a + b))
    
    # print a - b
    # print("a - b - {}".format(a - b))
    
    # print a * b
    # print("a * b - {}".format(a * b))

    # print a / b
    # integers opertated on - float answer
    print("a / b - {}".format(a / b))
    #      a / b - [ 1.  1.  3.  2.] *** note decimal point(s) ***
    # print("type((a[0]) - {}".format(type((a[0]))))
    #        type((a[0]) - <class 'numpy.int64'> *** operands integer ***
    
    # print("type(a / b) - {}".format(type(a / b)))
    #        type(a / b) - <class 'numpy.ndarray'> *** answer numPy array***
    
    # print("type((a / b)[0]) - {}".format(type((a / b)[0])))
    #        type((a / b)[0]) - <class 'numpy.float64'> *** answer element float, operands integers answer float  ***

    # print a ** b
    # print("a ** b - {}".format(a ** b))


# Arithmetic operations between a NumPy array and a single number
if True:
    a = np.array([1, 2, 3, 4])
    b = 2
    
    # print a + b
    # print("a + b - {}".format(a + b))

    # print a - b
    # print("a - b - {}".format(a - b))

    # print a * b
    # print("a * b - {}".format(a * b))
    
    # print a / b
    # see above *** operands integers, answer numpyArray of floats, see decimal points
    print("a / b - {}\n".format(a / b))
    #      a / b - [ 0.5  1.   1.5  2. ]
    
    # print("type(a / b) - {}".format(type(a / b)))
    # type(a / b) - <class 'numpy.ndarray'>

    # print("type((a / b)[0]) - {}".format(type((a / b)[0])))
    #        type((a / b)[0]) - <class 'numpy.float64'> *** operands integers, answers float***

    # print a ** b
    # print("a ** b - {}".format(a ** b))


# Logical operations with NumPy arrays
if False:
    a = np.array([True, True, False, False])
    b = np.array([True, False, True, False])
    
    # print a & b
    # print("a & b - {}".format(a & b))

    # print a | b
    # print("a | b - {}".format(a | b))

    #print ~a
    # print("~a - {}".format(~a))
    
    # print a & True
    # print("a & True - {}".format(a & True))
    
    # print a & False
    # print("a & False - {}".format(a & False))
    
    # print a | True
    # print("a | True - {}".format(a | True))
    
    # print a | False
    # print("a | False - {}".format(a | False))
    
# Comparison operations between 2 NumPy Arrays
if True:
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([5, 4, 3, 2, 1])
    
    # print a > b
    # print("a > b - {}".format(a > b))
    
    # print a >= b
    # print("a >= b - {}".format(a >= b))
    
    # print a < b
    # print("a < b - {}".format(a < b))
    
    # print a <= b
    # print("a <= b - {}".format(a <= b))
    
    # print a == b
    # print("a == b - {}".format(a == b))
    
    # print a != b
    # print("a != b - {}".format(a != b))
    
# Comparison operations between a NumPy array and a single number
if True:
    a = np.array([1, 2, 3, 4])
    b = 2
    
    # print a > b
    # print("a > b - {}".format(a > b))

    # print a >= b
    # print("a >= b - {}".format(a >= b))
    
    # print a < b
    # print("a < b - {}".format(a < b))
    
    # print a <= b
    # print("a <= b - {}".format(a <= b))
    
    # print a == b
    # print("a == b - {}".format(a == b))
    
    # print a != b
    # print("a != b - {}".format(a != b))
    
# First 20 countries with school completion data
countries = np.array([
       'Algeria', 'Argentina', 'Armenia', 'Aruba', 'Austria','Azerbaijan',
       'Bahamas', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bolivia',
       'Botswana', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
       'Cambodia', 'Cameroon', 'Cape Verde'
])

# Female school completion rate in 2007 for those 20 countries
female_completion = np.array([
    97.35583,  104.62379,  103.02998,   95.14321,  103.69019,
    98.49185,  100.88828,   95.43974,   92.11484,   91.54804,
    95.98029,   98.22902,   96.12179,  119.28105,   97.84627,
    29.07386,   38.41644,   90.70509,   51.7478 ,   95.45072
])

# Male school completion rate in 2007 for those 20 countries
male_completion = np.array([
     95.47622,  100.66476,   99.7926 ,   91.48936,  103.22096,
     97.80458,  103.81398,   88.11736,   93.55611,   87.76347,
    102.45714,   98.73953,   92.22388,  115.3892 ,   98.70502,
     37.00692,   45.39401,   91.22084,   62.42028,   90.66958
])

def overall_completion_rate(female_completion, male_completion):
    '''
    Fill in this function to return a NumPy array containing the overall
    school completion rate for each country. The arguments are NumPy
    arrays giving the female and male completion of each country in
    the same order.
    '''
    # recommended using 2. not just 2 note dot, decimal point  
    print("((female_completion + male_completion) / 2) - {}".format(((female_completion + male_completion) / 2.)))
    # print("type((female_completion + male_completion) / 2)) - {}".format(type((female_completion + male_completion) / 2)))
    #        type((female_completion + male_completion) / 2)) - <class 'numpy.ndarray'>

    return None

overall_completion_rate(female_completion, male_completion)




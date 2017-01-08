'''
Created on Jan 7, 2017

@author: Menfi
'''

print("") 

import numpy as np

# Example create a populated numPy array, first create a native Python list - Python list -> numPy Array
myIntegerArray = np.array([1,2,3,4,5])

myBooloeanArray = np.array([False, False, True, True, True])
# print("type(myBooloeanArray) - {}".format(type(myBooloeanArray)))
#        type(myBooloeanArray) - <class 'numpy.ndarray'>

# Example accessing elements of a, any, nominal numPy array using a *** boolean *** bool *** numPy *** index *** array, boolean numPy array called an index array 
myIntegerArray[myBooloeanArray]
print("myIntegerArray[myBooloeanArray] - {}".format(myIntegerArray[myBooloeanArray]))


# Generating a boolean, bool numPy index array from a nominal numPy array. ***
print("myIntegerArray > 2 - {}\n".format(myIntegerArray > 2))
#      myIntegerArray > 2 - [False False  True  True  True]
# print("type(myIntegerArray > 2) - {}".format(type(myIntegerArray > 2)))
#        type(myIntegerArray > 2) - <class 'numpy.ndarray'>

# Generating a numPy array, criteria compliant, in this case greater than 2, from a nominal numPy array  
myIntegerArray[myIntegerArray > 2]
# print("myIntegerArray[myIntegerArray > 2] - {}".format(myIntegerArray[myIntegerArray > 2]))
#        myIntegerArray[myIntegerArray > 2] - [3 4 5]


# Change False to True for each block of code to see what it does
# Using index arrays
if False:
    a = np.array([1, 2, 3, 4])
    b = np.array([True, True, False, False]) # Example *** bool boolean index array ***
    
    # print a[b]
    print("a[b] - {}".format(a[b]))
    #      a[b] - [1 2] - bool boolean index array driven output 

    # print a[np.array([True, False, True, False])]
    print("a[np.array([True, False, True, False])] - {}".format(a[np.array([True, False, True, False])]))
    #      a[np.array([True, False, True, False])] - [1 3] - bool boolean index array driven output

# Creating the index array using vectorized operations
if True:
    a = np.array([1, 2, 3, 2, 1])
    b = (a >= 2)
    
    # print a[b] 
    # print("a[b] - {}".format(a[b]))
    #      a[b] - [2 3 2] - bool boolean index array driven output

    # print a[a >= 2]
    # print("a[a >= 2] - {}".format(a[a >= 2]))
    #      a[a >= 2] - [2 3 2] - bool boolean index array driven output
    
# Creating the index array using vectorized operations on another array
if True:
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([1, 2, 3, 2, 1])
    
    # print b == 2
    # print("b == 2 - {}".format(b == 2))
    #      b == 2 - [False  True False  True False] - bool boolean index array driven output
    
    #print a[b == 2]
    # print("a[b == 2] - {}".format(a[b == 2]))
    #      a[b == 2] - [2 4]  - bool boolean index array driven output

def mean_time_for_paid_students(time_spent, days_to_cancel):
    '''
    Fill in this function to calculate the mean time spent in the classroom
    for students who stayed enrolled at least (greater than or equal to) 7 days.
    Unlike in Lesson 1, you can assume that days_to_cancel will contain only
    integers (there are no students who have not canceled yet).
    
    The arguments are NumPy arrays. time_spent contains the amount of time spent
    in the classroom for each student, and days_to_cancel contains the number
    of days until each student cancel. The data is given in the same order
    in both arrays.
    '''
    return None

# Time spent in the classroom in the first week for 20 students
time_spent = np.array([
       12.89697233,    0.        ,   64.55043217,    0.        ,
       24.2315615 ,   39.991625  ,    0.        ,    0.        ,
      147.20683783,    0.        ,    0.        ,    0.        ,
       45.18261617,  157.60454283,  133.2434615 ,   52.85000767,
        0.        ,   54.9204785 ,   26.78142417,    0.
])

# Days to cancel for 20 students
days_to_cancel = np.array([
      4,   5,  37,   3,  12,   4,  35,  38,   5,  37,   3,   3,  68,
     38,  98,   2, 249,   2, 127,  35
])

myDaysToCancelBooleanIndexArray = days_to_cancel > 6
print("myDaysToCancelBooleanIndexArray - {}\n".format(myDaysToCancelBooleanIndexArray))

myTimeSpentEnrolledGreaterThan6 = time_spent[myDaysToCancelBooleanIndexArray]
print("myTimeSpentEnrolledGreaterThan6 - {}\n".format(myTimeSpentEnrolledGreaterThan6))
# print("type(myTimeSpentEnrolledGreaterThan6) - {}".format(type(myTimeSpentEnrolledGreaterThan6)))
#        type(myTimeSpentEnrolledGreaterThan6) - <class 'numpy.ndarray'>

myTimeSpentEnrolledGreaterThan6.mean()
print("myTimeSpentEnrolledGreaterThan6.mean() - {}".format(myTimeSpentEnrolledGreaterThan6.mean()))














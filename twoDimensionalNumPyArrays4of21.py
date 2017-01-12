'''
Created on Jan 12, 2017

@author: Menfi
'''
# github .argmax(), NumPy arrays    

print("\nBegin\n")

# NumPy - create single two dimensional array
# NumPy - Access elements a[1, 3], row then column, also both can be a slice, using colon notation 
# Pandas DataFrame  - Two Dimensional Data Structure  

import numpy as np

# Subway ridership for 5 stations on 10 different days
ridership = np.array([
    [   0,    0,    2,    5,    0],
    [1478, 3877, 3674, 2328, 2539],
    [1613, 4088, 3991, 6461, 2691],
    [1560, 3392, 3826, 4787, 2613],
    [1608, 4802, 3932, 4477, 2705],
    [1576, 3933, 3909, 4979, 2685],
    [  95,  229,  255,  496,  201],
    [   2,    0,    1,   27,    0],
    [1438, 3785, 3589, 4174, 2215],
    [1342, 4043, 4009, 4665, 3033]
])

# Change False to True for each block of code to see what it does

# Accessing elements
if False:
    print("ridership[1] - {}\n".format(ridership[1]))
    #      ridership[1] - [1478 3877 3674 2328 2539]
    
    # first row (zero based), third (zero based) column
    print("ridership[1, 3] - {}\n".format(ridership[1, 3]))
    #      ridership[1, 3] - 2328

    # print ridership[1:3, 3:5]
    # first row (zero based), up to do not include the third zero based() row 
    print("ridership[1:3] -> ")
    print(ridership[1:3])
    print("")
    
    # get first (zero based), through do not include the third row, get third (zero based), through not to include the 5th (zero based) column
    print("47ridership[1:3, 3:5] -> ")
    print(ridership[1:3, 3:5])
    print("")
    
    #print ridership[1, :]
    # get the whole first (zero based) row
    print("ridership[1, :] - {}".format(ridership[1, :]))
    
# Vectorized operations on rows or columns 12 January 3:01 AM
if False:
    # print ridership[0, :] + ridership[1, :]
    print("ridership[0, :] -> ")
    print(ridership[0, :])
    print("")
    
    print("ridership[1, :] -> ")
    print(ridership[1, :])
    print("")
    
    print("ridership[0, :] + ridership[1, :] -> ")
    print(ridership[0, :] + ridership[1, :])
    print("")
    
    # print ridership[:, 0] + ridership[:, 1]
    print("ridership[:, 0] -> ")
    print(ridership[:, 0])
    print("")
    
    print("ridership[:, 1] -> ")
    print(ridership[:, 1])
    print("")
    
    print("ridership[:, 0] + ridership[:, 1] -> ")
    print(ridership[:, 0] + ridership[:, 1])
    print("")
   
# Vectorized operations on entire arrays
if True:
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    # print a + b
    print(" a + b -> ")
    print( a + b)
    print("")
    
def mean_riders_for_max_station(ridership):
    '''
    Fill in this function to find the station with the maximum riders on the
    first day, then return the mean riders per day for that station. Also
    return the mean ridership overall for comparsion.
    
    Hint: NumPy's argmax() function might be useful:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html
    '''
    overall_mean = None # Replace this with your code
    mean_for_max = None # Replace this with your code
    
    return (overall_mean, mean_for_max)

# print("type(ridership) - {}".format(type(ridership)))
#      type(ridership) - <class 'numpy.ndarray'>

print(" -> ")
print(ridership[0])
print(ridership[0, :])
print("")
# print("type(ridership[0, :]) - {}".format(type(ridership[0, :])))
#        type(ridership[0, :]) - <class 'numpy.ndarray'>

# Example - argmax, .argmax() get the LOCATION of the highest numerical value 
# 0 top row - first day data for 5 stations - 5 columns 
firstDayMaxValueColumn = (ridership[0, :]).argmax()
print("firstDayMaxValueColumn - {}".format(firstDayMaxValueColumn))

# Use the top number location to get the top number 
firstDayMaxValue =  ridership[0, firstDayMaxValueColumn]
print("firstDayMaxValue - {}".format(firstDayMaxValue))

# column with the top number, from the top row
print("ridership[:, firstDayMaxValueColumn] -> ")
print(ridership[:, firstDayMaxValueColumn])
print("")

# get the mean of that column
print("ridership[:, firstDayMaxValueColumn].mean() -> ")
print(ridership[:, firstDayMaxValueColumn].mean())
print("")

# get NumPy Array mean 
print("ridership.mean() -> ")
print(ridership.mean())
print("")

print("")







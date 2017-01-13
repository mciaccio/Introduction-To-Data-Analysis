'''
Created on Jan 12, 2017

@author: Menfi
'''

import numpy as np

print("\nBegin\n")

# numPy Two Dimensional Array
# axis = 0, ridership.mean(axis = 0) - column - subway station 
# axis = 1 row - date 

# Change False to True for this block of code to see what it does

# NumPy axis argument
if True:
    a = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    
    print("type(a) - {}\n".format(type(a)))

    # Example - sum numPy array, no axis argument, all rows, all columns
    # print a.sum()
    print("a.sum() -> ")
    print(a.sum())
    print("")

    # Example - sum numPy array, axis = 0, column based sum 
    # print a.sum(axis=0)
    print("a.sum(axis=0) -> ")
    print(a.sum(axis=0))
    print("")
    
    # Example - sum numPy array, axis = 1, row based sum 
    # print a.sum(axis=1)
    print("a.sum(axis=1) -> ")
    print(a.sum(axis=1))
    print("")
    
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

def min_and_max_riders_per_day(ridership):
    '''
    Fill in this function. First, for each subway station, calculate the
    mean ridership per day. Then, out of all the subway stations, return the
    maximum and minimum of these values. That is, find the maximum
    mean-ridership-per-day and the minimum mean-ridership-per-day for any
    subway station.
    '''
    # rows - 5 subway stations (axis = 1)
    # columns - 10 calendar dates (axis = 0)
    
    # (1478+3877+3674+2328+2539) / 5 = 2729.2
    # (0+1478+1613+1560+1608+1576+95+2+1438+1342) / 10 = 1071.2 
    
    # Example numpy array, axis = 0 (column based)
    meanStationRidershipPerDayColumn = ridership.mean(axis = 0)
    # print("type(ridership) - {}".format(type(ridership)))
    #        type(ridership) - <class 'numpy.ndarray'>

    # print("type(meanStationRidershipPerDayColumn) - {}".format(type(meanStationRidershipPerDayColumn)))
    #        type(meanStationRidershipPerDayColumn) - <class 'numpy.ndarray'>
     
    print("meanStationRidershipPerDayColumn -> ")
    print(meanStationRidershipPerDayColumn)
    print("")
    
    # Example numpy array, axis = 0 (column based), maximum value
    # max_daily_ridership = None     # Replace this with your code
    max_daily_ridership = ridership.max(axis = 0)
    print("max_daily_ridership -> ")
    print(max_daily_ridership)
    
    # Example numPy array, maximum value
    max_daily_ridership = meanStationRidershipPerDayColumn.max()
    print("max_daily_ridership -> ")
    print(max_daily_ridership)
    print("")
    
    # Example numpy array, axis = 0 (column based), minimum value
    # min_daily_ridership = None     # Replace this with your code
    min_daily_ridership = ridership.min(axis = 0)
    print("min_daily_ridership -> ")
    print(min_daily_ridership)

    # Example numpy array, minimum value    
    min_daily_ridership = meanStationRidershipPerDayColumn.min()
    print("min_daily_ridership -> ")
    print(min_daily_ridership)
    print("")
    
    return (max_daily_ridership, min_daily_ridership)


min_and_max_riders_per_day(ridership)
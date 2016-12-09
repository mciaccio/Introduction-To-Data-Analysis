
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
if True:
    # print ridership[1, 3]
    print("")
    print("ridership[1, 3] 2nd row, zero based indexing")
    print("ridership[1, 3] fourth column, zero based indexing")
    print("ridership[1, 3] -> ")
    print(ridership[1, 3])
    print("")

    #print ridership[1:3, 3:5]
    print("ridership[1:3, 3:5] -> ")
    print(ridership[1:3, 3:5])
    print("")

    # print ridership[1, :]
    print(".....ridership[1, :] -> ")
    print(ridership[1, :])
    print("")

    # print ridership[1, :]
    # first row
    # print("ridership[: 1] -> ")
    # print(ridership[: 1])
    # print("")
    
    # print ridership[1, :]
    print("zeroth column, first day  -> ")
    print(ridership [:, 0] )
    # type(ridership [:, 0]) - <class 'numpy.ndarray'>
    # print("type(ridership [:, 0]) - {}".format(type(ridership [:, 0])))
    # get the index of the station with the maximum riders on the first day
    print("position, index of argmax() in first column - (ridership [:, 0]).argmax()  -> ")
    # position, index of max value
    print((ridership [:, 0]).argmax()) # 2
    # hard code index "2"  / test make sure 1613 
    print((ridership [2, 0])) #1613
    # use argmax() syntax max riders first day zeroth column, third row - # 1613 
    print((ridership [(ridership [:, 0]).argmax(), 0])) # 1613
    # row with first day max ridership
    # print(ridership [2, : ] )
    # row with first day max ridership
    # print(ridership [   (ridership [:, 0]).argmax()  , : ] )
    print("")
    
    # first day max ridership in third row 
    # print("max row 5 stations ridership [2, :] -> ")
    # print(ridership [2, :] )
    # print("(mean of max row ridership 5 stations [2, :]).mean() -> ")
    # print((ridership [2, :]).mean())
    # use argmax() syntax
    # print((ridership [   (ridership [:, 0]).argmax()   , :]).mean())
    # (1613  + 4088 + 3991 + 6461 + 2691) / 5 - 3768.8 - google search 
    # print("")
    
    print("Get the first column, first day data")
    print((ridership [:, 0:1 ]))
    # (1478 + 1613 + 1560  + 1608 + 1576 + 95 + 2 + 1438 + 1342) / 10 = 1071.2 - google search 
    print("first column, first day data - mean")
    print((ridership [:, 0:1 ]).mean())
    print("")
    
    print("ridership.mean() -> ")
    print(ridership.mean())
    print("")


# Vectorized operations on rows or columns
if True:
    # print ridership[0, :] + ridership[1, :]
    print("ridership[0, :] + ridership[1, :] ->")
    # arithmetic addition of first two rows
    print(ridership[0, :] + ridership[1, :])
    print("")

    # arithmetic addition of first two columns 
    # print ridership[:, 0] + ridership[:, 1]
    print("ridership[:, 0] + ridership[:, 1] -> ")
    print(ridership[:, 0] + ridership[:, 1])
    print("")
    
# Vectorized operations on entire arrays
if True:
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    # print a + b 
    print("a + b -> ")
    print(a + b)
    print("")

    
    
print("zeroth row, first day  -> ")
print(ridership [0, :] )
print("")

print("zeroth row, first day, index of max  -> ")
print(ridership [0, :].argmax())
print("")

print("first day max column  -> ")
print(ridership [:, 3] )
print(ridership [:, ridership [0, :].argmax()] )
print("")

print("mean riders per day for that station  -> ")
print(ridership [:, 3].mean())
print(ridership [:, ridership [0, :].argmax()].mean())
print((5 + 2328 + 6461 + 4787 + 4477 + 4979 + 496 + 27 + 4174 + 4665) / 10)
print("")


a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ])

print("a.sum() - {}".format(a.sum()))
print("a.sum(axis=0 - column) - {}".format(a.sum(axis=0)))
print("a.mean(axis=0 - column) - {}\n".format(a.mean(axis=0)))

print("a.sum(axis=1) - row - {}".format(a.sum(axis=1)))
print("a.mean(axis=1) - row - {}\n".format(a.mean(axis=1)))

print("ridership.mean(axis=0 - column) - {}\n".format(ridership.mean(axis=0)))

listOfStationMeans = ridership.mean(axis=0)
print("listOfStationMeans - {}".format(listOfStationMeans))
# type(listOfStationMeans) - <class 'numpy.ndarray'>
print("type(listOfStationMeans) - {}\n".format(type(listOfStationMeans)))

print("listOfStationMeans.min() - {}".format(listOfStationMeans.min()))
print("listOfStationMeans.max() - {}\n".format(listOfStationMeans.max()))


    

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
    
    


import numpy as np
print()

a = [1, 2, 3, 4, 5]
a_Array = np.array(a)
print("a - {}".format(a))
print("a_Array - {}\n".format(a_Array))

# index Array - identifies elements to keep
# boolean Array
b = [False, False, True, True, True]
b_Array = np.array(b)
print("b - {}".format(b))
print("b_Array - {}\n".format(b_Array))

# knock out the False keepers identified by b_Array 
a_Array[b_Array]
print("a_Array[b_Array] - {}\n".format(a_Array[b_Array]))

# vectorized operation - returns array of booleans 
a_Array > 2
# bools used to identify the keepers 
print("a_Array > 2 - {}".format(a_Array > 2))
print("a_Array[a_Array > 2] - {}\n".format(a_Array[a_Array > 2])) # preferred syntax 

# Using index arrays
a = np.array([1, 2, 3, 4])
b = np.array([True, True, False, False])

print("a[b] - {}".format(a[b]))
print ("a[np.array([True, False, True, False])] - {}\n".format(a[np.array([True, False, True, False])]))

# Creating the index array using vectorized operations
a = np.array([1, 2, 3, 2, 1])
b = (a >= 2)
print("a[b] - {}".format(a[b]))
print("a[a >= 2] - {}\n".format(a[a >= 2]))

# Creating the index array using vectorized operations on another array
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 3, 2, 1])
print("b == 2 - {}".format(b == 2))
print("a[b == 2] - {}\n".format(a[b == 2]))

a = np.array([1, 2, 3, 4])
print("a - {}".format(a))
b = a
print("b - {}\n".format(b))

# in-place vectorized addition
# b bumped with a, note +=
# a and b are pointers to the SAME Array same memory location 
# += updates in-place
a += np.array ([1, 1, 1, 1])

print("a - {}".format(a))
print("b - {}\n".format(b))
 
a = np.array([1, 2, 3, 4])
print("a - {}".format(a))
b = a
print("b - {}\n".format(b))

# not in-place vectorized addition - prefered 
# b not bumped, NEW Array created here the 'a' Array
# not in-place
a = a + np.array ([1, 1, 1, 1])

print("a - {}".format(a))
print("b - {}\n".format(b))

a = np.array([1, 2, 3, 4, 5])
# a - [1 2 3 4 5]
print("a - {}".format(a))
# slice - view of original Array
# slice - <class 'slice'>
print("slice - {}".format(slice))

slice = a[:3]
# slice - view of original Array
# slice - [1 2 3]
print("slice - {}".format(slice))

# a - [1 2 3 4 5]
print("a - {}".format(a))

# modify the slice, the view of the original Array - original Array modified as well
slice[0] = 100
# slice - view of original Array
# slice - [100   2   3]
print("slice - {}".format(slice))
#a - [100   2   3   4   5]
print("a - {}".format(a))
 
  
 
 

    
 


    
 




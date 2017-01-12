'''
Created on Jan 11, 2017

@author: Menfi
'''
# github dropna dropna() method, fillna method, Panda Series add method (fill_value argument), Panda Series apply() method

import pandas as pd

print("\nBegin\n")

# Change False to True for each block of code to see what it does

# Addition when indexes are the same
if True:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
    # print s1 + s2
    print("s1 + s2 -> ")
    print(s1 + s2)
    print("")

# Indexes have same elements in a different order
if True:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['b', 'd', 'a', 'c'])
    # print s1 + s2
    print("s1 + s2 -> ")
    print(s1 + s2)
    print("")

# Indexes overlap, but do not have exactly the same elements
if True:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
    # print s1 + s2
    print("s1 + s2 -> ")
    print(s1 + s2)
    print("")
    
# Example add two Panda Series, sum has NaN Values 
# Example add two Panda Series, sum has NaN Values, use dropna() method to remove or drop NaN, Not a Number 
# Indexes overlap, but do not have exactly the same elements
if True:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
    
    seriesSumWithNaNValues = (s1 + s2) 

    print("seriesSumWithNaNValues -> ")
    print(seriesSumWithNaNValues)
    print("")

# Example add two Panda Series, sum has NaN Values, use dropna() method to remove or drop NaN, Not a Number 
    print("seriesSumWithNaNValues.dropna() -> ")
    print(seriesSumWithNaNValues.dropna())
    print("")
    # print("type() - {}".format(type(seriesSumWithNaNValues.dropna)))
    #        type() - <class 'method'>

# Example add two Panda Series, sum has NaN Values, use fillna(0) method to replace NaN with zero 0 
    print("seriesSumWithNaNValues.fillna(0) -> ")
    print(seriesSumWithNaNValues.fillna(0))
    print("")

# Example add two Panda Series, sum has NaN Values, use Panda Series add method, fill_value argument, to fill in "blanks" with the zero 0 *** BEFORE ADDITION *** 
    print("s1.add(s2, fill_value = 0) -> ")
    print(s1.add(s2, fill_value = 0))
    print("")
    
# Indexes do not overlap
if True:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['e', 'f', 'g', 'h'])
    # print s1 + s2
    print("s1 + s2 -> ")
    print(s1 + s2)
    print("")    
    
def addThree(x):
    return x + 3
    
# Example - problem definition, Panda Series builtin, built in, function does not exist, native Panda Series Vectorized Operation not found - use Panda Series apply() method    
# Example - native Python list -> Panda Series, call Panda Series apply() method on Panda Series
myPythonList = [1, 2, 3, 4, 5]
myPandaSeries = pd.Series(myPythonList)
myPandaSeries.apply(addThree)
print("myPandaSeries.apply(addThree) -> ")
print(myPandaSeries.apply(addThree))
# print("type(myPandaSeries.apply) - {}".format(type(myPandaSeries.apply)))
#        type(myPandaSeries.apply) - <class 'method'>
print("")
    
names = pd.Series([
    'Andre Agassi',
    'Barry Bonds',
    'Christopher Columbus',
    'Daniel Defoe',
    'Emilio Estevez',
    'Fred Flintstone',
    'Greta Garbo',
    'Humbert Humbert',
    'Ivan Ilych',
    'James Joyce',
    'Keira Knightley',
    'Lois Lane',
    'Mike Myers',
    'Nick Nolte',
    'Ozzy Osbourne',
    'Pablo Picasso',
    'Quirinus Quirrell',
    'Rachael Ray',
    'Susan Sarandon',
    'Tina Turner',
    'Ugueth Urbina',
    'Vince Vaughn',
    'Woodrow Wilson',
    'Yoji Yamada',
    'Zinedine Zidane'
])

def myReverseFunction(firstLast):
    # print("firstLast - {}".format(firstLast))
    mySplitString = firstLast.split()
    myReturnString = mySplitString[1] + ', '+ mySplitString[0]
    print("myReturnString - {}".format(myReturnString))

def reverse_names(names):
    '''
    Fill in this function to return a new series where each name
    in the input series has been transformed from the format
    "Firstname Lastname" to "Lastname, FirstName".
    
    Try to use the Pandas apply() function rather than a loop.
    '''
    
    # Example - problem definition, Panda Series builtin, built in, function does not exist, native Panda Series Vectorized Operation not found - use Panda Series apply() method
    names.apply(myReverseFunction)
    
    return None

reverse_names(names)
    
myString = 'Tina Turner'
print("myString - {}".format(myString))
mySplitString = myString.split()
print("mySplitString - {}".format(mySplitString))
# print("type(mySplitString) - {}".format(type(mySplitString)))
#        type(mySplitString) - <class 'list'>

myReturnString = mySplitString[1] + ', '+ mySplitString[0]
print("myReturnString - {}".format(myReturnString))








    
    
    
      
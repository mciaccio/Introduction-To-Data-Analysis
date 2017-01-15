'''
Created on Jan 15, 2017

@author: Menfi
'''

# github apply() Python function to Pandas DataFrame Series, return 1 value 

print("\nBegin\n")
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'a': [4, 5, 3, 1, 2],
    'b': [20, 10, 40, 50, 30],
    'c': [25, 20, 5, 15, 10]
})

# Change False to True for this block of code to see what it does

# DataFrame apply() - use case 2
if True:   
    pass
    # call, or apply() numPy built in function *** mean *** on PandaSeries of Panda DataFrame  
    # print df.apply(np.mean)
    # print("type(df) - {}".format(type(df)))
    #        type(df) - <class 'pandas.core.frame.DataFrame'>
    # print("type(np.mean) - {}".format(type(np.mean)))
    #        type(np.mean) - <class 'function'>
    
    # print("df.apply(np.mean) -> ")
    # print(df.apply(np.mean))
    # print("type(df.apply(np.mean)) - {}".format(type(df.apply(np.mean))))
    #        type(df.apply(np.mean)) - <class 'pandas.core.series.Series'>
    # print("")
    
    
    # Same here call or apply built in numPy max function on Panda Series of Panda DataFrame  
    # print df.apply(np.max)
    # print("df.apply(np.max) -> ")
    # print(df.apply(np.max))
    # print("type(df.apply(np.max)) - {}".format(type(df.apply(np.max))))
    #        type(df.apply(np.max)) - <class 'pandas.core.series.Series'>

    # print("")
    
def mySecondLargest(pandasSeries):
    # print("pandasSeries-> ")
    # print(pandasSeries)
    # print("type(pandasSeries) - {}".format(type(pandasSeries)))
    #      type(pandasSeries) - <class 'pandas.core.series.Series'>
    # print("")
    
    print("50 -> ")
    print(pandasSeries.sort_values(ascending = 0))
    print("")
    
    tempPandasSeries = pandasSeries.sort_values(ascending = 0)
    # print("type(tempPandasSeries) - {}".format(type(tempPandasSeries)))
    #      type(tempPandasSeries) - <class 'pandas.core.series.Series'>
    
    # second highest value 
    myValue = tempPandasSeries.iloc[1] 
    print("myValue -> ")
    print(myValue)
    print("")

    myValue1 = tempPandasSeries[1] 
    print("myValue1 -> ")
    print(myValue1)
    print("")
    
    return myValue1

def second_largest(df):
    '''
    Fill in this function to return the second-largest value of each 
    column of the input DataFrame.
    '''
    print("type(df) - {}".format(type(df)))
    #      type(df) - <class 'pandas.core.frame.DataFrame'>
    
    df.apply(mySecondLargest)

    return None

second_largest(df)



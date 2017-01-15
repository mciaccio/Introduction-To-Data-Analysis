'''
Created on Jan 15, 2017

@author: Menfi
'''

# github - Examples adding Pandas Series to Pandas DataFrame, *** axis ***

print("\nBegin\n")

import pandas as pd

# Adding using +
# success, works - integers of Pandas Series added to *** columns *** of Pandas DataFrame
if True:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    # print df
    # print '' # Create a blank line between outputs
    # print df + s
    
    # print("df -> ")
    # print(df)
    # print("")
    
    # print("df + s -> ")
    print(df + s)
    print("...34")
    
# Adding with axis='index'
# success, works, same as above - integers of Pandas Series added to *** rows *** of Pandas DataFrame, *** axis='index' ***
if True:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    # print df
    # print '' # Create a blank line between outputs
    # print df.add(s, axis='index')
    # The functions sub(), mul(), and div() work similarly to add()

    # print("df -> ")
    # print(df)
    # print("")
    
    # print("df.add(s, axis='index') -> ")
    print(df.add(s, axis='index'))
    print("axis='index'")    

# Adding with axis='columns'
# success, works, same as above - integers of Pandas Series added to *** columns *** of Pandas DataFrame *** axis='columns' *** 
if True:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    # print df
    # print '' # Create a blank line between outputs
    # print df.add(s, axis='columns')
    # The functions sub(), mul(), and div() work similarly to add()
    
    # print("df -> ")
    # print(df)
    # print("")
    
    # print("df.add(s, axis='columns') -> ")
    print(df.add(s, axis='columns'))
    print("axis='columns'\n")    
    
grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

def standardize(df):
    '''
    Fill in this function to standardize each column of the given
    DataFrame. To standardize a variable, convert each value to the
    number of standard deviations it is above or below the mean.
    
    This time, try to use vectorized operations instead of apply().
    You should get the same results as you did before.
    '''
    
    print("101")
    
    # print("df -> ")
    # print(df)
    # print("")
    
    # Pandas Standard Deviation - Default - Sample - ddof = 1
    # Pandas Standard Deviation - Population (all values known) ddof = 0  
    # 14.986994, 14.492757
    myStandardDeviation = df.std(ddof = 0)
    # print("myStandardDeviation -> ")
    # print(myStandardDeviation)
    # print("")

    # 77.7
    # 57.4
    myDFMean = df.mean()
    # print("myDFMean -> ")
    print(myDFMean)
    # print("")
    
    myMeanDifference = df - myDFMean
    # print("myMeanDifference -> ")
    # print(myMeanDifference) # AOK checks out
    # print("")
    
    myStandardized = myMeanDifference / myStandardDeviation
    # print("myStandardized -> ")
    # print(myStandardized) # AOK checks out
    # print("")

    # return None
    return myStandardized

def standardize_rows(df):
    '''
    Optional: Fill in this function to standardize each row of the given
    DataFrame. Again, try not to use apply().
    
    This one is more challenging than standardizing each column!
    '''
    print("142")
    
    print("standardize_rows - df -> ")
    print(df)
    print("")
    
    # 9.5, 9
    # Got the Standard Deviation of the rows, NOT columns 
    myStandardDeviation = df.std(ddof = 0, axis = 'columns')
    print("standardize_rows - myStandardDeviation -> ")
    print(myStandardDeviation) # AOK checks out
    print("")
    
    # Got the Mean of the rows, NOT columns, use axis = 'columns' - instructor verified!! 
    myDFMean = df.mean(axis = 'columns')
    
    # print("157type(myDFMean) - {}".format(type(myDFMean)))
    # type(myDFMean) - <class 'pandas.core.series.Series'>

    print("standardize_rows - myDFMean -> ")
    print(myDFMean) # AOK checks out
    print("")
    
    myMeanDifference = df.sub(myDFMean, axis = 'index') # index or row index per instructor 
    print("standardize_rows - myMeanDifference -> ")
    print(myMeanDifference) # AOK checks out
    # print("")
    
    # myStandardized = myMeanDifference / myStandardDeviation
    # myStandardized = myMeanDifference.div(myStandardDeviation, axis = 'index') # works AOK checks out row centric NOT columns instructor used index!!
    myStandardized = myMeanDifference.div(myStandardDeviation, axis = 'rows')  # works AOK checks out row centric NOT columns
    # myStandardized = myMeanDifference.div(myStandardDeviation, axis = 'columns')  # does NOT work
    print("standardize_rows - myStandardized -> ")
    print(myStandardized)
    print("")

    return None


standardize(grades_df)
standardize_rows(grades_df)





import pandas as pd

# Adding using +
# DataFrame + Series = DataFrame
# value of Series at index 0 added to column values of DataFrame at index 0
# same for indexes 2, 3, 4
if False:
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
    
    print("")
    print("df -> ")
    print(df)
    # print("type(df) - {}".format(type(df)))
    # type(df) - <class 'pandas.core.frame.DataFrame'>
    print("")
    
    print("s -> ")
    print(s)
    # print("type(s) - {}".format(type(s)))
    # type(s) - <class 'pandas.core.series.Series'>

    print("")
    
    print("Add a Series to a DataFrame")
    # Series index 0 value, added to DataFrame column index 0 
    # same result as axis = 'columns', axis = 1
    print("df + s -> ")
    print(df + s)
    # print("type(df + s) - {}".format(type(df + s)))
    # type(df + s) - <class 'pandas.core.frame.DataFrame'>
    print("")
    
    
# Adding with axis='index'
if False:
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
    
    print("")
    print("df -> ")
    print(df)
    # print("type(df) - {}".format(type(df)))
    # type(df) - <class 'pandas.core.frame.DataFrame'>
    print("")
    
    print("s -> ")
    print(s)
    # print("type(s) - {}".format(type(s)))
    # type(s) - <class 'pandas.core.series.Series'>

    print("")
    print("Add a Series to a DataFrame axis='index'")
    # add a Series to a DataFrame
    # using the add method of the DataFrame class - axis = 'index' argument
    # value at index 0 of the Series, added to ROW index 0 of the DataFrame
    # axis = 'index' same effect as axis = 0
    print("df + s -> ")
    print(df.add(s, axis='index'))
    # print("type(df + s) - {}".format(type(df + s)))
    # type(df + s) - <class 'pandas.core.frame.DataFrame'>
    
    print("")
    print("Add a Series to a DataFrame axis=0")
    # add a Series to a DataFrame
    # using the add method of the DataFrame class - axis = 0 argument
    # index 0 value of the Series, added to ROW index 0 of the DataFrame
    # axis = 0 - effected the ROW
    #axis = 'index' same effect as axis = 0
    print(df.add(s, axis=0))
    print("")
    
    print("Add a Series to a DataFrame axis=1")
    # add a Series to a DataFrame
    # using the add method of the DataFrame class - axis = 1 argument
    # index 0 value of the Series, added to column 0 of the DataFrame
    # axis = 1 - effected the COLUMN
    print(df.add(s, axis=1))
    print("") 
    
    print("Add a Series to a DataFrame axis='columns'")
    # add a Series to a DataFrame
    # using the add method of the DataFrame class - axis = columns argument
    # index 0 value of the Series, added to column 0 of the DataFrame
    # axis = 'columns' - effected the COLUMN
    # axis = 'columns' same as axis = 1
    print(df.add(s, axis='columns'))
    print("")
    
    # subtract, multiply, divide work similarly to add()
    # The functions sub(), mul(), and div() work similarly to add()

    
    
# Adding with axis='columns' - See above
if False:
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
    
grades_dfORIG = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James'] 
)

grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89],
          'exam2': [24, 63, 56, 56, 67]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio'] 
)




def standardize(df):
    '''
    Fill in this function to standardize each column of the given
    DataFrame. To standardize a variable, convert each value to the
    number of standard deviations it is above or below the mean.
    
    This time, try to use vectorized operations instead of apply().
    You should get the same results as you did before.
    '''
    # Standardize each column of the DataFrame 
    # Standardize exam grades 
    # Use vectorized operations Not the apply method.
    
    print("")
    print("DataFrame - grades_df")
    print(df)
    
    print("")
    print("First get the mean of each column of exam grades in the DataFrame")
    print("df.mean() returns a pandas Series")
    print("dataFrameMeanPandasSeries = df.mean()")
    dataFrameMeanPandasSeries = df.mean() 
    print("dataFrameMean -> ")
    print(dataFrameMeanPandasSeries)
    # print("type(dataFrameMeanPandasSeries) - {}".format(type(dataFrameMeanPandasSeries)))
    # type(dataFrameMeanPandasSeries) - <class 'pandas.core.series.Series'>

    print("")
    print("First get the mean of each column of exam grades in the DataFrame")
    print("df.mean() returns a pandas Series")
    print("dataFrameMeanPandasSeries = df.mean(axis=0) <--- note: axis = 0, same as axis = 'rows', axis = 'index'  ")
    dataFrameMeanPandasSeries = df.mean(axis=0) 
    print("dataFrameMean -> ")
    print(dataFrameMeanPandasSeries)
 
    print("")
    print("First get the mean of each column of exam grades in the DataFrame")
    print("df.mean() returns a pandas Series")
    print("dataFrameMeanPandasSeries = df.mean(axis='rows') <--- note: axis = 'rows', same as axis = 0, axis = 'index'")
    dataFrameMeanPandasSeries = df.mean(axis='rows') 
    print("dataFrameMean -> ")
    print(dataFrameMeanPandasSeries)
    print("")
    
    print("First get the mean of each column of exam grades in the DataFrame")
    print("df.mean() returns a pandas Series")
    print("dataFrameMeanPandasSeries = df.mean(axis='index') <--- note: axis = 'index', same as axis = 0, axis = 'rows'")
    dataFrameMeanPandasSeries = df.mean(axis='index') 
    print("dataFrameMean -> ")
    print(dataFrameMeanPandasSeries)
    print("")
    
    print("Next step in standardization subtract the mean from the value")
    
    df_grades_DataFrameMeanSubtracted = df - dataFrameMeanPandasSeries 
    
    print("df - dataFrameMeanPandasSeries")
    print(df - dataFrameMeanPandasSeries)
    print("")

    print("df.sub(dataFrameMeanPandasSeries)")
    print(df.sub(dataFrameMeanPandasSeries))
    print("")
    
    print("df.sub(dataFrameMeanPandasSeries, axis = 1), note axis = 1, same as axis = 'columns'")
    print(df.sub(dataFrameMeanPandasSeries, axis = 1))
    print("")

    print("df.sub(dataFrameMeanPandasSeries, axis = 'columns'), note axis = 'columns', same as axis = '1'")
    print(df.sub(dataFrameMeanPandasSeries, axis = 'columns'))
    print("")
    
    print("Next get the standard deviation of the DataFrame (grades_df)")
    grades_dfStandardDeviation = df.std(ddof=1)
    print("grades_dfStandardDeviation -> ")
    print(grades_dfStandardDeviation)
    print("")
    
    print("df_gradesDataFrameMeanSubtracted -> ")
    print(df_grades_DataFrameMeanSubtracted)
    print("")
    
    standardized_grades_df = df_grades_DataFrameMeanSubtracted / grades_dfStandardDeviation
    
    print("standardized_grades_df -> ")
    print(standardized_grades_df)
    print("")
    
    return None

def standardize_rows(df):
    '''
    Optional: Fill in this function to standardize each row of the given
    DataFrame. Again, try not to use apply().
    
    This one is more challenging than standardizing each column!
    '''

    print("")    
    print("df (grades_df) -> ")
    print(df)
    print("")
      
    dataFrameMean = df.mean(axis='columns')
     
    print("")    
    print("dataFrameMean -> ")
    print(dataFrameMean)
    # print("type(dataFrameRowMeans) - {}".format(type(dataFrameRowMeans)))
    # type(dataFrameRowMeans) - <class 'pandas.core.series.Series'>
    print("")
    
    dataFrameMeanSubtracted = df.sub(dataFrameMean, axis ='rows') # both 'rows' and 'index' worked, instructor used 'index'
    dataFrameMeanSubtracted = df.sub(dataFrameMean, axis ='index') # - instructor used 'index' 
    print("dataFrameMeanSubtracted -> ")
    print(dataFrameMeanSubtracted)
    print("")
    
    dataFrameStandardDeviation = df.std(axis = 'columns', ddof=1)
      
    print("dataFrameStandardDeviation -> ")
    print(dataFrameStandardDeviation)
    # print("type(dataFrameStandardDeviation) - {}".format(type(dataFrameStandardDeviation)))
    # type(dataFrameStandardDeviation) - <class 'pandas.core.series.Series'>
    print("")
    
    # answer = dataFrameMeanSubtracted.div(dataFrameStandardDeviation, axis = 'rows') # both work instructor used 'index'
    standardizedDataFrameValues = dataFrameMeanSubtracted.div(dataFrameStandardDeviation, axis = 'index') # both work instructor used 'index' 
       
    print("standardizedDataFrameValues -> ")
    print(standardizedDataFrameValues)
    print("")   
    
    return None

# standardize(grades_df)
standardize_rows(grades_df)


print("")
x = 5
print("x -> ")
print(x)
print("")
print("type(x) - {}".format(type(x)))
print("")

print("x - {}".format(x))
print("type(x) - {}".format(type(x)))
print("")





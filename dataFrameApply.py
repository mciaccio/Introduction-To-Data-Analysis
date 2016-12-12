

"""
standard deviation calculation lecture notes
numpy's numpy.std() - default is population standard deviation - "ddof = 0" - all scores known population NOT sample - Bessel's correction OFF 
panda's panda.std() - default is sample     standard deviation - "ddof = 1"  Bessel's correction ON
here we are using  DataFrame apply() function - we want to act on EACH COLUMN
not using DataFrame applymap() function - operates on all columns
github "pandas - DataFrame - Series - index name - loc, iloc - apply() work on each column"
"""

import pandas as pd

grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

# Change False to True for this block of code to see what it does

# DataFrame apply()
if False:
    def convert_grades_curve(exam_grades):
        # Pandas has a bult-in function that will perform this calculation
        # This will give the bottom 0% to 10% of students the grade 'F',
        # 10% to 20% the grade 'D', and so on. You can read more about
        # the qcut() function here:
        # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.qcut.html
        return pd.qcut(exam_grades,
                       [0, 0.1, 0.2, 0.5, 0.8, 1],
                       labels=['F', 'D', 'C', 'B', 'A'])
        
    # qcut() operates on a list, array, or Series. This is the
    # result of running the function on a single column of the
    # DataFrame.
    # print convert_grades_curve(grades_df['exam1'])
    print("")
    print("convert_grades_curve(grades_df['exam1'] -> ")
    print(convert_grades_curve(grades_df['exam1']))
    print("")

    # qcut() does not work on DataFrames, but we can use apply()
    # to call the function on each column separately
    # print grades_df.apply(convert_grades_curve)
    print("grades_df.apply(convert_grades_curve) -> ")
    print(grades_df.apply(convert_grades_curve))

    
def standardize(df):
    '''
    Fill in this function to standardize each column (*** each column think apply() NOT applymap()***)
    of the given DataFrame. To standardize a variable, convert each value to the
    number of standard deviations it is above or below the mean.
    '''
    
    # print("type(df) - {}".format(type(df)))
    # type(df) - <class 'pandas.core.frame.DataFrame'>
    
    print("")
    print("df -> ")
    print(df)
    print("")
    
    print("df.mean() -> ")
    print(df.mean())
    print("")
    
    print("df.std() -> ")
    print(df.std())
    print("")
    
    print("df.index -> ")
    print(df.index)
    print("")
    
    # accessing panda DataFrame, Series, loc, index name 
    print("df.loc['Barry'], df.loc['Barry'][0], df.loc['Barry'][1]")
    print(df.loc['Barry'])
    #print("type(df.loc['Barry']) - {}".format(type(df.loc['Barry'])))
    #type(df.loc['Barry']) - <class 'pandas.core.series.Series'>
    print(df.loc['Barry'][0])
    print(df.loc['Barry'][1])
    print("")
    
    # accessing panda DataFrame, Series, iloc, index number  
    print("df.iloc[0] -> ")
    print(df.iloc[0])
    print("")

    
    """
    standard deviation calculation lecture notes
    numpy's numpy.std() - default is population standard deviation - "ddof = 0" - all scores known population NOT sample - Bessel's correction OFF 
    panda's panda.std() - default is sample     standard deviation - "ddof = 1"  Bessel's correction ON
    here we are using  DataFrame apply() function - we want to act on EACH COLUMN
    not using DataFrame applymap() function - operates on all columns
    """

    # pandas - default ddof=1 sample not population - here we have the entire population so - ddof=0 
    standardizedDataFrame = (df - df.mean()) / df.std(ddof=0)
    print("standardizedDataFrame -> ")
    print(standardizedDataFrame)
    print("")
    
        
    return None

def standardize1(df):
    '''
    Fill in this function to standardize each column (*** each column think apply() NOT applymap()***)
    of the given DataFrame. To standardize a variable, convert each value to the
    number of standard deviations it is above or below the mean.
    '''
    # print("type(df) - {}".format(type(df)))
    # type(df) - <class 'pandas.core.frame.DataFrame'>
    
    """
    standard deviation calculation lecture notes
    numpy's numpy.std() - default is population standard deviation - "ddof = 0" - all scores known population NOT sample - Bessel's correction OFF 
    panda's panda.std() - default is sample     standard deviation - "ddof = 1"  Bessel's correction ON
    here we are using  DataFrame apply() function - we want to act on EACH COLUMN
    not using DataFrame applymap() function - operates on all columns
    """

    # pandas - default ddof=1 sample not population - here we have the entire population so - ddof=0 
    standardizedDataFrame = (df - df.mean()) / df.std(ddof=0)
    print("standardizedDataFrame -> ")
    print(standardizedDataFrame)
    print("")
    
        
    return None

# standardize(grades_df)
print("11111111111111111grades_df.apply(standardize1) -> ")
print(grades_df.apply(standardize1))
print("222222222222222")

grades_df.apply(standardize1)
print("33333333333333grades_df.apply(standardize1) -> ")
# print(grades_df.apply(standardize1))
print("444444444444")
    

print("")
x = 5
print("x - {}".format(x))
print("type(x) - {}".format(type(x)))
print("")

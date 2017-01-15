'''
Created on Jan 14, 2017

@author: Menfi
'''
print("\nBegin\n")

import pandas as pd 

# Example - DataFrame apply Series of DataFrame to Python function

# Example - create, instantiate, populate Pandas DataFrame, column names, index argument, Panda DataFrame made up of Panda Series, DataFrame apply Series of DataFrame to Python function
grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

# Change False to True for this block of code to see what it does

# DataFrame apply()
if True:
    def convert_grades_curve(exam_grades):
        
        # A 20%, B 30%, C 30 % d 10% F 10%
        #     F         D           C        C         C         B         B         B          A         A
        #    43(Andre) 65(Humbert) 70(Fred) 75(Dan)   78(Chris) 81(Barry) 87(James) 89(Emilio) 91(Greta) 98(Ivan)
        #     F         D           C        C         C         B         B         B          A         A
        #    24(Andre) 46(Humbert) 51(Fred) 56(Chris) 56(Dan)   60(James) 63(Barry) 67(Emilio) 72(Ivan)  79(Greta) 
        # Andre Barry

        
        # Pandas has a bult-in function that will perform this calculation
        # This will give the bottom 0% to 10% of students the grade 'F',
        # 10% to 20% the grade 'D', and so on. You can read more about
        # the qcut() function here:
        # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.qcut.html
        
        # print("type(exam_grades) - {}".format(type(exam_grades)))
        #        type(exam_grades) - <class 'pandas.core.series.Series'>
        
        # print("type(pd.qcut) - {}".format(type(pd.qcut)))
        #        type(pd.qcut) - <class 'function'>

        # qcut - built in Pandas function works on Pandas Series, NOT Pandas DataFrame, maps percentages (raw scores) to labels (letter grades)
        return pd.qcut(exam_grades,
                       [0, 0.1, 0.2, 0.5, 0.8, 1],
                       labels=['F', 'D', 'C', 'B', 'A'])
        
    # qcut() operates on a list, array, or Series. This is the
    # result of running the function on a single column of the
    # DataFrame.
    
    # print convert_grades_curve(grades_df['exam1'])
    # First run it on the exam1 column, Pandas series
    # print("convert_grades_curve(grades_df['exam1']) -> ")
    # print(convert_grades_curve(grades_df['exam1']))
    # print("type(convert_grades_curve(grades_df['exam1'])) - {}".format(type(convert_grades_curve(grades_df['exam1']))))
    # type(convert_grades_curve(grades_df['exam1'])) - <class 'pandas.core.series.Series'>
    # print("")
    
    # Next run it on the exam2 column, Pandas series
    # print("convert_grades_curve(grades_df['exam2']) -> ")
    # print(convert_grades_curve(grades_df['exam2']))
    # print("")
    
    # At this point we know the convert_grades_curve Python function / Panda qcut function WORKS on Pandas Series 
    
    # qcut() does not work on DataFrames, but we can use apply()
    # to call the function on each column separately
    
    # print("type(grades_df.apply) - {}".format(type(grades_df.apply)))
    # type(grades_df.apply) - <class 'method'>
    
    # The apply method passes the Panda Series that makeup the Pandas DataFrame to the Python convert_grades_curve function, the DataFrame is NOT passed
    # print grades_df.apply(convert_grades_curve)
    # print("grades_df.apply(convert_grades_curve) -> ")
    # print(grades_df.apply(convert_grades_curve))
    # print("type(grades_df.apply(convert_grades_curve)) - {}".format(type(grades_df.apply(convert_grades_curve))))
    #        type(grades_df.apply(convert_grades_curve)) - <class 'pandas.core.frame.DataFrame'>

    # print("")

def standardizeTheSeries(mySeries):
    print("mySeries -> ")
    print(mySeries)
    # print("type(mySeries) - {}".format(type(mySeries)))
    #        type(mySeries) - <class 'pandas.core.series.Series'>

    print("")
    
    mySeriesMean = mySeries.mean()
    print("mySeriesMean -> ")
    print(mySeriesMean)
    print("")
    
    mySeriesDifferenceFromMean = mySeries - mySeriesMean
    print("mySeriesDifferenceFromMean -> ")
    print(mySeriesDifferenceFromMean)
    print("")
    
    mySeriesStandardDeviation = mySeries.std(ddof = 0) 
    print("mySeriesStandardDeviation -> ")
    print(mySeriesStandardDeviation)
    # print("type(mySeriesStandardDeviation) - {}".format(type(mySeriesStandardDeviation)))
    #        type(mySeriesStandardDeviation) - <class 'float'>
    print("")
    
    standardizedSeries = mySeriesDifferenceFromMean / mySeriesStandardDeviation
    print("standardizedSeries -> ")
    print(standardizedSeries)
    # print("type(standardizedSeries) - {}".format(type(standardizedSeries)))
    #        type(standardizedSeries) - <class 'pandas.core.series.Series'>
    print("")


def standardize(df):
    '''
    Fill in this function to standardize each column of the given
    DataFrame. To standardize a variable, convert each value to the
    number of standard deviations it is above or below the mean.
    '''
    df.apply(standardizeTheSeries)
    return None

standardize(grades_df)
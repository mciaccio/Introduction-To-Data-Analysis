
"""
github - "pandas - applymap()"
lecture notes -
DataFrame out of the box builtin functions do not provide needed functionality.
apply, applymap - custom function to DataFrame to get a new DataFrame 
"""

import pandas as pd

# Change False to True for this block of code to see what it does

# DataFrame applymap()
if True:
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [10, 20, 30],
        'c': [5, 10, 15]
    })
    
    def add_one(x):
        return x + 1
    
    def getLetterGrade(x):
        #print("x - {}".format(x))
        #print("type(x) - {}".format(type(x)))
        if x > 89:
            return 'A'
        elif x > 79:
            return 'B'
        elif x > 69:
            return 'C'
        elif x > 59:
            return 'D'
        else:
            return 'F'
               
    """
    df - original input DataFrame to be manipulated
    applymap - out of box DataFrame function
    add_one - custom function called - run on df - original input DataFrame 
    """
    # print df.applymap(add_one)
    print("")
    print("df.applymap(add_one) -> ")
    print(df.applymap(add_one))
    print("")
    
    print("original DataFrame unchanged")
    print("df -> ")
    print(df)
    print("")

grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

def convert_grades(grades):
    '''
    Fill in this function to convert the given DataFrame of numerical
    grades to letter grades. Return a new DataFrame with the converted
    grade.
    
    The conversion rule is:
        90-100 -> A
        80-89  -> B
        70-79  -> C
        60-69  -> D
        0-59   -> F
    '''
    
    print("grades -> ")
    print(grades)
    print("")
    # print("type(grades) - {}".format(type(grades)))
    # type(grades) - <class 'pandas.core.frame.DataFrame'>
    
    print("grades['exam1'] -> ")
    print(grades['exam1'])
    print("")
    
    """
    applymap() documentation, lecture notes, example
    no need to drill down into the individual elements of the input DataFrame
    simply apply the custom function - getLetterGrade - to the input or original DataFrame
    original DataFrame remains untouched
    """
    myDataFrame = grades.applymap(getLetterGrade)
    print("myDataFrame -> ")
    print(myDataFrame)
    print("")
#     print("type(myDataFrame) - {}".format(type(myDataFrame)))
#     type(myDataFrame) - <class 'pandas.core.frame.DataFrame'>
    
    return None

convert_grades(grades_df)



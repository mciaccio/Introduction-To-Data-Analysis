'''
Created on Jan 14, 2017

@author: Menfi
'''

# github DataFrame applymap()

print("\nBegin\n")

import pandas as pd

# Change False to True for this block of code to see what it does

# DataFrame applymap()
if False:
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [10, 20, 30],
        'c': [5, 10, 15]
    })
    
    def add_one(x):
        return x + 1
        
    # print df.applymap(add_one)
    print("df.applymap(add_one) -> ")
    print(df.applymap(add_one))
    print("")
    
grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)
    
def convert_grades0(grades):
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
    return grades + 1
    # return None
    
def convert_grades(grades):
    if grades > 89:
        return 'A'
    elif grades > 79:
        return 'B'
    elif  grades > 69:
        return 'C'
    elif grades > 59:
        return 'D'
    else:
        return 'F' 

letterGrades0 = convert_grades0(grades_df)
print("letterGrades0 -> ")
print(letterGrades0)
print("")

letterGrades = grades_df.applymap(convert_grades0)
print("letterGrades -> ")
print(letterGrades)
print("")

letterGrades = grades_df.applymap(convert_grades)
print("letterGrades -> ")
print(letterGrades)
print("")



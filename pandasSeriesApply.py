
import pandas as pd

# apply .apply a function to a pd panda series 

# Change False to True to see what the following block of code does

# Example pandas apply() usage (although this could have been done
# without apply() using vectorized operations)
if True:
    s = pd.Series([1, 2, 3, 4, 5])
    
    def add_one(x):
        return x + 1
    
    print ("s.apply(add_one) ->")
    print (s.apply(add_one))
    
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

def lastFirst(firstLast):
    print('\t\tBegin lastFirst')
    print("\t\t\tfirstLast - {}\n".format(firstLast))
    
    firstLastSplit = firstLast.split()
    
    # firstLastSplit - ['Tina', 'Turner']
    print("\t\t\tfirstLastSplit - {}\n".format(firstLastSplit))
    # type(firstLastSplit) - <class 'list'>
    # print("type(firstLastSplit) - {}".format(type(firstLastSplit)))
    
    print("\t\t\tfirstLastSplit[0] - {}".format(firstLastSplit[0]))
    # type(firstLastSplit[1]) - <class 'str'>
    # print("\t\t\ttype(firstLastSplit[0]) - {}\n".format(type(firstLastSplit[0])))

    print("\t\t\tfirstLastSplit[1] - {}\n".format(firstLastSplit[1]))
    # type(firstLastSplit[1]) - <class 'str'>
    # print("\t\t\ttype(firstLastSplit[1]) - {}\n".format(type(firstLastSplit[1])))
    
    lastFirst = firstLastSplit[1] + ', ' + firstLastSplit[0]

    print('\t\tEnd lastFirst')
    return lastFirst


def reverse_names(names):
    '''
    Fill in this function to return a new series where each name
    in the input series has been transformed from the format
    "Firstname Lastname" to "Lastname, FirstName".
    
    Try to use the Pandas apply() function rather than a loop.
    '''
    print('\tBegin reverse_names')
    firstLast = 'Tina Turner'
    fixedName = lastFirst(firstLast)
    
    print("\tfixedName - {}".format(fixedName))
    
    # names.apply(lastFirst)

    print('\tEnd reverse_names')

    return names.apply(lastFirst)

fixedNames = reverse_names(names)
print("fixedNames - {}".format(fixedNames))


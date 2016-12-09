

# math arithmetic NumPy arrays
import numpy as np


a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 1, 2])
print("a - {}".format(a))
print("b - {}\n".format(b))

print("a + b - {}".format(a + b))
print("a - b - {}\n".format(a - b))

print("a * b - {}".format(a * b))
print("a / b - {}\n".format(a / b))

print("a ** b - {}\n".format(a ** b))


a = np.array([1, 2, 3, 4])
b = 2
print("a - {}".format(a))
print("b - {}\n".format(b))

print("a + b - {}".format(a + b))
print("\t\ta - b - {}\n".format(a - b))

print("a * b - {}".format(a * b))
print("a / b - {}\n".format(a / b))

print("a ** b - {}\n".format(a ** b))

a = np.array([True, True, False, False])
b = np.array([True, False, True, False])

print("~a - {}".format(~a))
print("a & b - {}".format(a & b))
print("a & True - {}".format(a & True))
print("a & False - {}".format(a & False))
print("a | True - {}".format(a | True))
print("a | False - {}\n".format(a | False))

a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])
print("a > b - {}".format(a > b))
print("a >= b - {}".format(a >= b))
print("a < b - {}".format(a < b))
print("a <= b - {}".format(a <= b))
print("a == b - {}".format(a == b))
print("a != b - {}\n".format(a != b))

a = np.array([1, 2, 3, 4])
b = 2
print("a > b - {}".format(a > b))
print("a >= b - {}".format(a >= b))
print("a < b - {}".format(a < b))
print("a <= b - {}".format(a <= b))
print("a == b - {}".format(a == b))
print("a != b - {}".format(a != b))

# First 20 countries with school completion data
countries = np.array([
       'Algeria', 'Argentina', 'Armenia', 'Aruba', 'Austria','Azerbaijan',
       'Bahamas', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bolivia',
       'Botswana', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
       'Cambodia', 'Cameroon', 'Cape Verde'
])

# Female school completion rate in 2007 for those 20 countries
female_completion = np.array([
    97.35583,  104.62379,  103.02998,   95.14321,  103.69019,
    98.49185,  100.88828,   95.43974,   92.11484,   91.54804,
    95.98029,   98.22902,   96.12179,  119.28105,   97.84627,
    29.07386,   38.41644,   90.70509,   51.7478 ,   95.45072
])

# Male school completion rate in 2007 for those 20 countries
male_completion = np.array([
     95.47622,  100.66476,   99.7926 ,   91.48936,  103.22096,
     97.80458,  103.81398,   88.11736,   93.55611,   87.76347,
    102.45714,   98.73953,   92.22388,  115.3892 ,   98.70502,
     37.00692,   45.39401,   91.22084,   62.42028,   90.66958
])

overall_school_completion_rate_list = []

for i in range(len(female_completion)):
    # print("i - {}".format(i))
    print("i - {}, female_completion[i] - {}, male_completion[i] - {}".format(i, female_completion[i], male_completion[i]))
    print("female_completion[i] - {}, male_completion[i] - {}".format( female_completion[i], male_completion[i] ))
    print("{}".format( ((female_completion[i] + male_completion[i]) / 2.) ))
    overall_school_completion_rate_list.append(((female_completion[i] + male_completion[i]) / 2.))
    
print("")
print("len(overall_school_completion_rate_list) - {}".format(len(overall_school_completion_rate_list)))
overall_school_completion_rate = np.array(overall_school_completion_rate_list)
print("len(overall_school_completion_rate) - {}".format(len(overall_school_completion_rate)))


total_array = female_completion + male_completion
print("len(total_array) - {}".format(len(total_array)))

answerArray = total_array / 2
answerArray1 = female_completion + male_completion / 2
print("len(answerArray) - {}".format(len(answerArray)))
print("len(answerArray1) - {}".format(len(answerArray1)))


         
 

    



 
    






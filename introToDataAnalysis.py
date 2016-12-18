"""
 plot show multiple charts histograms hist ....
"""
 
import os
import unicodecsv 
from datetime import datetime as dt
from collections import defaultdict
import pprint
import numpy
# import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import seaborn as sns

# from statsmodels.sandbox.regression.kernridgeregress_class import plt_closeall
# from bokeh.charts.attributes import color

enrollmentAccountKeys=set()
engagementAccountKeys=set()
submissionAccountKeys=set()

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')
    
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)
 
 
DATADIR = '/Users/Menfi/Documents/gitBaseDirectory/IntroToDataAnalysis/dataFiles'

ENROLLMENT_FN = 'enrollments.csv'
ENROLLMENT_DF = os.path.join(DATADIR,ENROLLMENT_FN)

ENGAGEMENT_FN = 'daily_engagement.csv'
ENGAGEMENT_DF = os.path.join(DATADIR, ENGAGEMENT_FN)

SUBMISSION_FN = 'project_submissions.csv'
SUBMISSION_DF = os.path.join(DATADIR, SUBMISSION_FN)

# ENROLLMENT_DF = 'enrollments.csv'
with open (ENROLLMENT_DF, 'rb') as f:
    enrollmentReader = unicodecsv.DictReader(f)
    enrollments = list(enrollmentReader)
print ("")

for enrollment in enrollments[:1]:
    print("enrollment before cleanup - {}".format(enrollment))    
    
# enrollment.csv data clean up
for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])    
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])
    
for enrollment in enrollments[:1]:
    print("enrollment after cleanup - {}".format(enrollment))    
   
for enrollment in enrollments:
    enrollmentAccountKeys.add(enrollment['account_key'])

# enrollment list length 1640 total - 1302 unique students enrolled
# 1302 unique student enrolled records differs from 1237 unique engagement student records
# a student can enroll, cancel than re-enroll
# hence total enrollment records > unique enrollments records      
print("len(enrollments) - {}".format(len(enrollments)))
print("len(enrollmentAccountKeys) - {}".format(len(enrollmentAccountKeys)))
print("")

# ENGAGEMENT_DF = 'daily_engagement.csv'
with open (ENGAGEMENT_DF, 'rb') as f:
    engagementReader = unicodecsv.DictReader(f)
    daily_engagement = list(engagementReader)

for engagement in daily_engagement[:1]:
    print("engagement before cleanup - {}".format(engagement))

# daily_engagement.csv data clean up
for engagement_record in daily_engagement:
    engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
    engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
    engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
    engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
    engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])
    
    tempAccountKey = engagement_record['acct']
    del engagement_record['acct']
    engagement_record['account_key'] = tempAccountKey
    
for engagement_record in daily_engagement[:1]:
    print("engagement_record after cleanup - {}".format(engagement_record))

for engagement_record in daily_engagement:
    engagementAccountKeys.add(engagement_record['account_key'])
     
# 136240 total daily_engagement records (multiple entries for each student)
# 1237 unique engagement students
# 1237 unique engagement student records differs from 1302 unique student enrolled records 
print("len(daily_engagement) - {}".format(len(daily_engagement)))
print("len(engagementAccountKeys) - {}".format(len(engagementAccountKeys)))
print ("")

            
# SUBMISSION_DF = 'project_submissions.csv'
with open (SUBMISSION_DF, 'rb') as f:
    submissionReader = unicodecsv.DictReader(f)
    project_submissions = list(submissionReader)

for submission in project_submissions[:1]:
    print("submission before cleanup - {}".format(submission))

for submission in project_submissions:
    submission['completion_date'] = parse_date(submission['completion_date'])
    submission['creation_date'] = parse_date(submission['creation_date'])
    
for submission in project_submissions[:1]:
    print("submission after cleanup - {}".format(submission))

for submission in project_submissions:
    submissionAccountKeys.update([submission['account_key']])
    
# 3642 project submissions (total) from 743 unique students
print("len(project_submissions) - {}".format(len(project_submissions)))
print("len(submissionAccountKeys) - {}".format(len(submissionAccountKeys)))
print("")


# More unique students in enrollment (1302) than engagement table (1227) 
# difference = 65, 3 udacity students 57
# enrollment[‘join_date’] = enrollment[‘cancel_date’]
# AND
# enrollment[‘days_to_cancel’] = 0 zero 
# hence no enrollment record

count = 0
count1 = 0
count2 = 0
udacity_test_accounts = set()
non_udacity_enrollments = []
non_udacity_engagement = []
non_udacity_submissions = []

for enrollment in enrollments:
    if enrollment['account_key'] not in engagementAccountKeys: # 71 total
        # print("enrollment['account_key'] - {}".format(enrollment['account_key']))
        # print("enrollment['join_date'] - {}".format(enrollment['join_date']))
        # print("enrollment['cancel_date'] - {}".format(enrollment['cancel_date']))
        # print("type(enrollment['cancel_date']) - {}".format(type(enrollment['cancel_date'])))
        enrollment['cancel_date']
        enrollment['join_date']
        count +=1
        
        if (enrollment['cancel_date'] == enrollment['join_date']) and enrollment['days_to_cancel'] == 0: # 67 records here 
            if enrollment['is_udacity']:
                pass
                #print("145enrollment - {}".format(enrollment)) # 3 records herr
            else:
                count1 += 1
        else:
            pass
            # print("enrollment - {}".format(enrollment)) # 3 records here
            
        if (not enrollment['is_udacity']) and (enrollment['cancel_date'] == enrollment['join_date']) and (enrollment['days_to_cancel'] == 0): # 67
            # print("enrollment['is_udacity'] - {}".format(enrollment['is_udacity']))
            count2 += 1
            # print("count2 - {}".format(count2))
            
    if enrollment['is_udacity']:
        # print("161 enrollment - {}".format(enrollment))
        udacity_test_accounts.add(enrollment['account_key'])

print("count - {}".format(count))
print("count1 - {}".format(count1))
print("count2 - {}\n".format(count2))

print("len(udacity_test_accounts) - {}\n".format(len(udacity_test_accounts)))

for enrollment in enrollments:
    if enrollment['account_key'] not in udacity_test_accounts:
        non_udacity_enrollments.append(enrollment)  

for engagement_record in daily_engagement:
    if engagement_record['account_key'] not in udacity_test_accounts:
        non_udacity_engagement.append(enrollment)  
        
for submission in project_submissions:
    if submission['account_key'] not in udacity_test_accounts:
        non_udacity_submissions.append(submission)  
        
print("len(non_udacity_enrollments) - {}".format(len(non_udacity_enrollments)))
print("len(non_udacity_engagement) - {}".format(len(non_udacity_engagement)))
print("len(non_udacity_submissions) - {}\n".format(len(non_udacity_submissions)))

paid_students = {}
       
for enrollment in non_udacity_enrollments: # answer 
    if not enrollment['is_canceled'] or enrollment['days_to_cancel'] > 7:
        if enrollment['account_key'] not in paid_students:
            paid_students[enrollment['account_key']] = enrollment['join_date'] 
        else:
            if enrollment['join_date']  > paid_students[enrollment['account_key']]:
                paid_students[enrollment['account_key']] = enrollment['join_date']
print("len(paid_students) is {}".format(len(paid_students)))

paid_enrollments = []
paid_engagement = []
paid_submission = []

for enrollment in non_udacity_enrollments:
    if enrollment['account_key'] in paid_students:
        paid_enrollments.append(enrollment)
print("len(paid_enrollments) - {}".format(len(paid_enrollments)))

for engagement in non_udacity_engagement:
    if engagement['account_key'] in paid_students:
        paid_engagement.append(engagement)
print("len(paid_engagement) - {}".format(len(paid_engagement)))        

for submission in non_udacity_submissions:
    if submission['account_key'] in paid_students:
        paid_submission.append(submission)
print("paid_submission[0]- {}".format(paid_submission[0]))        
print("len(paid_submission)- {}".format(len(paid_submission)))        

paid_engagement_in_first_week = []

for engagement_record in daily_engagement:
    if engagement_record['account_key'] in paid_students:
        time_delta = engagement_record['utc_date'] - paid_students[engagement_record['account_key']]
        if time_delta.days < 7 and time_delta.days >= 0:
            paid_engagement_in_first_week.append(engagement_record)
print("len(paid_engagement_in_first_week) - {}\n".format(len(paid_engagement_in_first_week)))

# summary record processing 
engagement_by_account = defaultdict(list)
for engagement_record in paid_engagement_in_first_week:
    engagement_by_account[engagement_record['account_key']].append(engagement_record)
pprint.pprint(engagement_by_account['10'])
# print("type(engagement_by_account['10']) - {}\n".format(type(engagement_by_account['10']))) # list
print("len(engagement_by_account) - {}\n".format(len(engagement_by_account))) # 995

total_minutes_by_account = {}

for account_key, engagement_for_student in engagement_by_account.items():
    total_minutes = 0
    for engagement_record in engagement_for_student:
        total_minutes += engagement_record['total_minutes_visited']
    total_minutes_by_account[account_key] = total_minutes 
    
total_minutes = total_minutes_by_account.values()

# print("total_minutes - {}".format(total_minutes))
print("type(total_minutes) - {}".format(type(total_minutes)))

print("numpy.mean(list(total_minutes)) - {}".format(numpy.mean(list(total_minutes))))
print("numpy.std(list(total_minutes)) - {}".format(numpy.std(list(total_minutes))))
print("numpy.min(list(total_minutes)) - {}".format(numpy.min(list(total_minutes))))
print("numpy.max(list(total_minutes)) - {}\n".format(numpy.max(list(total_minutes))))

for key, value in total_minutes_by_account.items():
    if value > 9000:
        print("key - {}".format(key))
        print("value - {}".format(value))
        
#engagement_by_account = defaultdict(list)
print("len(engagement_by_account) is {}".format(len(engagement_by_account))) # 

lessons_completed_by_account = {}

for account_key, engagement_for_student in engagement_by_account.items():
    lessons_completed = 0
    for engagement_record in engagement_for_student:
        lessons_completed += engagement_record['lessons_completed']
    lessons_completed_by_account[account_key] = lessons_completed
    
total_lessons = lessons_completed_by_account.values()

print("len(total_lessons) is {}".format(len(total_lessons)))
print("type(total_lessons) is {}".format(type(total_lessons)))
print("numpy.mean(list(total_lessons)) - {}".format(numpy.mean(list(total_lessons))))
print("numpy.std(list(total_lessons)) - {}".format(numpy.std(list(total_lessons))))
print("numpy.min(list(total_lessons)) - {}".format(numpy.min(list(total_lessons))))
print("numpy.max(list(total_lessons)) - {}\n".format(numpy.max(list(total_lessons))))

days_visited_by_account = {}

for account_key, engagement_for_student in engagement_by_account.items():
    days_visited = 0
    for engagement_record in engagement_for_student:
        if engagement_record['num_courses_visited'] > 0:
            days_visited += 1
    days_visited_by_account[account_key] = days_visited
    
total_days_visited = days_visited_by_account.values()

print("len(total_days_visited) is {}".format(len(total_days_visited)))
print("numpy.mean(list(total_days_visited)) - {}".format(numpy.mean(list(total_days_visited))))
print("numpy.std(list(total_days_visited)) - {}".format(numpy.std(list(total_days_visited))))
print("numpy.min(list(total_days_visited)) - {}".format(numpy.min(list(total_days_visited))))
print("numpy.max(list(total_days_visited)) - {}\n".format(numpy.max(list(total_days_visited))))


# project_submissions - ['assigned_rating']
# DISTINCTION PASSED

# project_submissions - ['lesson_key']
# subway_project_lesson_keys = ['746169184']
# subway_project_lesson_keys = ['3176718735']
subway_project_lesson_keys = ['746169184', '3176718735']
assigned_rating_keys = ['PASSED', 'DISTINCTION']

passing_accounts = []

passing_engagement = []
non_passing_engagement = []

passCounter = 0
failCounter = 0

#   dict           list
for submission in project_submissions:
    sub_account_key = submission['account_key'] 
    assigned_rating = submission['assigned_rating']
    lesson_key = submission['lesson_key'] 

    if lesson_key in subway_project_lesson_keys and assigned_rating in assigned_rating_keys:
        passing_accounts.append(sub_account_key) 
        
print("len(passing_accounts) is {}".format(len(passing_accounts)))

for engage_account_key in engagement_by_account:
    if engage_account_key in passing_accounts:
        passing_engagement.extend(engagement_by_account[engage_account_key])
    else:
        non_passing_engagement.extend(engagement_by_account[engage_account_key]) 
        
print("len(passing_engagement) is {}".format(len(passing_engagement)))
print("len(non_passing_engagement) is {}\n".format(len(non_passing_engagement)))

passing_engagement = []
non_passing_engagement = []

for peifw in paid_engagement_in_first_week[:2]:
    print("peifw - {}".format(peifw))
print()

for engagement in paid_engagement_in_first_week:
    if engagement['account_key'] in passing_accounts:
        passing_engagement.append(engagement)
    else:
        non_passing_engagement.append(engagement) 
        
print("len(passing_engagement) is {}".format(len(passing_engagement)))
print("len(non_passing_engagement) is {}\n".format(len(non_passing_engagement)))

total_minutes_visited_list = []
total_minutes_visited = 0
lessons_completed_list = []
num_courses_visited_list = []
for passing in passing_engagement:
    # print("passing\t\t - {}".format(passing))
    total_minutes_visited_list.append(passing['total_minutes_visited'])
    lessons_completed_list.append(passing['lessons_completed'])
    num_courses_visited_list.append(passing['num_courses_visited'])
# print("len(total_minutes_visited_list) is {}".format(len(total_minutes_visited_list)))
print("numpy.mean(total_minutes_visited_list) - {}".format(numpy.mean(total_minutes_visited_list)))
print("numpy.mean(lessons_completed_list) - {}".format(numpy.mean(lessons_completed_list)))
print("numpy.mean(num_courses_visited_list) - {}\n".format(numpy.mean(num_courses_visited_list)))

total_minutes_visited_list.clear()
lessons_completed_list.clear()
num_courses_visited_list.clear()
for non_passing in non_passing_engagement:
    #print("non_passing\t - {}".format(non_passing))
    total_minutes_visited_list.append(non_passing['total_minutes_visited'])
    lessons_completed_list.append(non_passing['lessons_completed'])
    num_courses_visited_list.append(non_passing['num_courses_visited'])
# print("len(total_minutes_visited_list) is {}".format(len(total_minutes_visited_list)))
print("numpy.mean(total_minutes_visited_list) - {}".format(numpy.mean(total_minutes_visited_list)))
print("numpy.mean(lessons_completed_list) - {}".format(numpy.mean(lessons_completed_list)))
print("numpy.mean(num_courses_visited_list) - {}\n".format(numpy.mean(num_courses_visited_list)))

histogramList = []
titlesList = ['Total Minutes Class Instruction - Passing', 'Total Minutes Class Instruction - Non Passing' ]
xaxes = ['Passing', 'Non Passing']
colorList = ['red', 'blue']
# xaxes = ['Passing', 'Non Passing']
total_minutes_visited_dictionary = defaultdict(float)
for passing in passing_engagement:
    myKey = passing['account_key'] 
    myMin = passing['total_minutes_visited']
    total_minutes_visited_dictionary[myKey] = total_minutes_visited_dictionary[myKey] + myMin 
    
print("len(total_minutes_visited_dictionary) is {}".format(len(total_minutes_visited_dictionary)))
myTotalMinValues = total_minutes_visited_dictionary.values()
myMean = numpy.mean(list(myTotalMinValues))
print("myTotalMinValues - {}".format(myTotalMinValues))
print("numpy.min(list(myTotalMinValues)) - {}".format(numpy.min(list(myTotalMinValues))))
print("numpy.max(list(myTotalMinValues)) - {}".format(numpy.max(list(myTotalMinValues))))
print("numpy.mean(list(myTotalMinValues)) - {}\n".format(numpy.mean(list(myTotalMinValues))))
# plt.xlabel("Average Minutes Studying (Passing Students) " + str(numpy.around(numpy.mean(list(myTotalMinValues)), decimals = 2)))
# plt.ylabel("Occurrences")
# xxx = list(myTotalMinValues)
histogramList.append(list(myTotalMinValues))
#plt.hist(list(myTotalMinValues),bins=50,color=['crimson'])
# plt.show()

total_minutes_visited_dictionary.clear()
for non_passing in non_passing_engagement:
    myKey = non_passing['account_key'] 
    myMin = non_passing['total_minutes_visited']
    total_minutes_visited_dictionary[myKey] = total_minutes_visited_dictionary[myKey] + myMin 
    
print("len(total_minutes_visited_dictionary) is {}".format(len(total_minutes_visited_dictionary)))
myTotalMinValues = total_minutes_visited_dictionary.values()
print("myTotalMinValues - {}".format(myTotalMinValues))
print("numpy.mean(list(myTotalMinValues)) - {}\n".format(numpy.mean(list(myTotalMinValues))))
# plt.xlabel("Average Minutes Studying (Non Passing Students) " + str(numpy.around(numpy.mean(list(myTotalMinValues)), decimals = 2)))
# plt.ylabel("Occurrences")
histogramList.append(list(myTotalMinValues))
# plt.hist(list(myTotalMinValues),bins=50,color=['crimson'])
# plt.show()

# a - Axes(0.125,0.536364;0.775x0.363636)
# type(a) - <class 'matplotlib.axes._subplots.AxesSubplot'>
figure, axes = plt.subplots(2, 1)

print("figure - {}".format(figure))
# type(figure) - <class 'matplotlib.figure.Figure'>
# print("type(figure) - {}\n".format(type(figure)))

print("axes - {}\n".format(axes))
# type(axes) - <class 'numpy.ndarray'>
# print("type(axes) - {}\n".format(type(axes)))

a = axes.ravel()
print("a - {}".format(a))
# type(a) - <class 'numpy.ndarray'>
# print("type(a) - {}".format(type(a)))

# ddd = list(myTotalMinValues) 

for idx, ax in enumerate(a):
    print("idx - {}".format(idx))
    
    ax.set_title(titlesList[idx])
    ax.hist(histogramList[idx],bins=50, color=colorList[idx], label = 'lllllllllllllllllllllllllllllllllllllllllll')
    # ax.set_xlabel(xaxes[idx])
    ax.set_ylabel('Occurrences')
     
plt.show()
# plt.close('all')

lessons_completed_dictionary = defaultdict(int)
for passing in passing_engagement:
    myKey = passing['account_key'] 
    myLessonCompleted = passing['lessons_completed']
    lessons_completed_dictionary[myKey] = lessons_completed_dictionary[myKey] + myLessonCompleted
print("len(lessons_completed_dictionary) is {}".format(len(lessons_completed_dictionary)))
myLessonsCompletedValues = lessons_completed_dictionary.values()
print("myLessonsCompletedValues - {}".format(myLessonsCompletedValues))
print("numpy.mean(list(myLessonsCompletedValues)) - {}\n".format(numpy.mean(list(myLessonsCompletedValues))))
plt.xlabel("Lessons Completed (Passing Students) Mean " + str(numpy.around(numpy.mean(list(myLessonsCompletedValues)), decimals = 2)))
plt.ylabel("Occurrences")
plt.hist(list(myLessonsCompletedValues),bins=50,color=['crimson'])
plt.show()

lessons_completed_dictionary.clear()
for non_passing in non_passing_engagement:
    myKey = non_passing['account_key'] 
    myLessonCompleted = non_passing['lessons_completed']
    lessons_completed_dictionary[myKey] = lessons_completed_dictionary[myKey] + myLessonCompleted 
print("len(lessons_completed_dictionary) is {}".format(len(lessons_completed_dictionary)))
mylessonCompletedValues = lessons_completed_dictionary.values()
print("mylessonCompletedValues - {}".format(mylessonCompletedValues))
print("numpy.mean(list(mylessonCompletedValues)) - {}\n".format(numpy.mean(list(mylessonCompletedValues))))
plt.xlabel("Lessons Completed (Non Passing Students) Mean " + str(numpy.around(numpy.mean(list(myLessonsCompletedValues)), decimals = 2)))
plt.ylabel("Occurrences")
plt.hist(list(myLessonsCompletedValues),bins=50,color=['crimson'])
plt.show()

days_visited_dictionary = defaultdict(int)
myDaysVisited = 0
for passing in passing_engagement:
    myKey = passing['account_key']
    
    if passing['num_courses_visited'] > 0:
        myDaysVisited += 1
        
    days_visited_dictionary[myKey] = days_visited_dictionary[myKey] + myDaysVisited
    myDaysVisited = 0
print("len(days_visited_dictionary) is {}".format(len(days_visited_dictionary)))
myDaysVisitedValues = days_visited_dictionary.values()
# print("myDaysVisitedValues - {}".format(myDaysVisitedValues))
print("numpy.mean(list(myDaysVisitedValues)) - {}\n".format(numpy.mean(list(myDaysVisitedValues))))
plt.xlabel("Days Visited (Passing Students) Mean " + str(numpy.around(numpy.mean(list(myDaysVisitedValues)), decimals = 2)))
plt.ylabel("Occurrences")
# plt.hist(list(myTotalMinValues),bins=50,color=['blue'])
plt.hist(list(myDaysVisitedValues),color=['blue'])
plt.show()

days_visited_dictionary.clear()
for non_passing in non_passing_engagement:
    myKey = non_passing['account_key'] 
    
    if non_passing['num_courses_visited'] > 0:
        myDaysVisited += 1
        
    days_visited_dictionary[myKey] = days_visited_dictionary[myKey] + myDaysVisited
    myDaysVisited = 0
print("len(days_visited_dictionary) is {}".format(len(days_visited_dictionary)))
myDaysVisitedValues = days_visited_dictionary.values()
print("myDaysVisitedValues - {}".format(myDaysVisitedValues))
print("numpy.mean(list(myDaysVisitedValues)) - {}\n".format(numpy.mean(list(myDaysVisitedValues))))
plt.xlabel("Days Visited (Non Passing Students) Mean " + str(numpy.around(numpy.mean(list(myDaysVisitedValues)), decimals = 2)))
plt.ylabel("Occurrences")
# plt.hist(list(myTotalMinValues),bins=50,color=['Green'])
plt.hist(list(myDaysVisitedValues),color=['Green'])
plt.show()

print("The End")
 
#for github comments 
# engagement_by_account = defaultdict(list)
# extend list, extends unwraps the list
# instead of adding one list it extends all n entries in the list
# subplots
 

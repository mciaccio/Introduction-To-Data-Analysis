'''
Created on Dec 26, 2016

@author: Menfi
'''
# github " Default Dictionary, defaultdict, value Default Dictionary key points to is a *** list ***"

import os
import csv
from datetime import datetime as dt
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

DATADIR = '/Users/Menfi/Documents/gitBaseDirectory/IntroToDataAnalysis/dataFiles'

ENROLLMENT_FN = 'enrollments.csv'
ENROLLMENT_DF = os.path.join(DATADIR, ENROLLMENT_FN)

ENGAGEMENT_FN = 'daily_engagement.csv'
ENGAGEMENT_DF = os.path.join(DATADIR, ENGAGEMENT_FN)

PROJECTSUBMISSIONS_FN = 'project_submissions.csv'
PROJECTSUBMISSIONS_DF = os.path.join(DATADIR,PROJECTSUBMISSIONS_FN)

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

print("")

# Example empty Python Dictionary, create Python Dictionary 
paid_students = {}
# print("type(paid_students) - {}".format(type(paid_students)))
#        type(paid_students) - <class 'dict'>

# Example read from disk file -> Python Dictionary -> list
with open(ENROLLMENT_DF, 'r') as f:
    reader = csv.DictReader(f)
    enrollments = list(reader)  
# print("len(enrollments) - {}".format(len(enrollments)))
#        len(enrollments) - 1640

# Example data clean up  - enrollments.csv
for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])
# print("len(enrollments) - {}".format(len(enrollments)))
#        len(enrollments) - 1640

# Example declare instantiate empty set
# iterate through the list, populating the enrollmentSet with account_key values 
enrollmentSet = set()
for enrollment in enrollments: 
    enrollmentSet.add(enrollment['account_key'])
enrollment_num_unique_students = len(enrollmentSet)
# print("enrollmentSet - {}".format(enrollmentSet))
#      enrollmentSet - {'1292', '381', '330', '1002', '1079', '955'... 
# print("len(enrollmentSet) - {}".format(len(enrollmentSet)))
#        len(enrollmentSet) - 1302

# find the 6 is_udacity = True account_key values
udacity_test_accounts = set()
for enrollment in enrollments: 
    if enrollment['is_udacity']:
        udacity_test_accounts.add(enrollment['account_key'])
# print("udacity_test_accounts - {}".format(udacity_test_accounts))
# udacity_test_accounts - {'1069', '1304', '1101', '312', '818', '448'}
# print("len(udacity_test_accounts) - {}".format(len(udacity_test_accounts)))
# len(udacity_test_accounts) - 6

# populate list of non_udacity_enrollments 
non_udacity_enrollments = []
for enrollment in enrollments:
    if enrollment['account_key'] in udacity_test_accounts:
        pass
    else:
        non_udacity_enrollments.append(enrollment)
# print("len(non_udacity_enrollments) - {}\n".format(len(non_udacity_enrollments)))
#        len(non_udacity_enrollments) - 1622
# Example access a list slice, bracket semi colon semicolon, note append to the right makes 1 very long line  
# print("non_udacity_enrollments[1:9] - {}".format(non_udacity_enrollments[1:9]))

# populate paid_students Dictionary - also update Dictionary value for a key that is already in the Python Dictionary 
# enrollments.csv - join_date
# join_date is the enrollment date
# key      - enrollment['account_key']
# value    - enrollment['join_date'] - *** most recent ***
for enrollment in non_udacity_enrollments:
    if enrollment['is_canceled'] == False or enrollment['days_to_cancel'] > 7: 
        if (enrollment['account_key'] not in paid_students) or (enrollment['join_date'] > paid_students[enrollment['account_key']]): # associate account_key - MOST recent enrollmentDate
            paid_students[enrollment['account_key']] = enrollment['join_date']
# print("paid_students - {}".format(paid_students))
#      paid_students - {'955': datetime.datetime(2015, 5, 11, 0, 0), '168': datetime.datetime(2015, 4, 8, 0, 0 
#      paid_students     enrollment['account_key']                        : enrollment['join_date']
# print("len(paid_students) - {}".format(len(paid_students)))
#        len(paid_students) - 995

# Example best practices print, iterate, enumerate, loop, through only part of a Python Dictionary,  print only n (few) Python Dictionary entries  
for index, key in enumerate(paid_students):
    if index < 3:
        print("enrollment - paid_students - key - {}\tpaid_students[key] - {} ".format(key, paid_students[key]))
print("")

paidStudentsSet = set()
# Example, best practices. access the Dictionary key
for key in paid_students:
    paidStudentsSet.add(key)
# print("paidStudentsSet - {}".format(paidStudentsSet))
#      paidStudentsSet - {'523', '495', '377', '1182', '91',  
# print("len(paidStudentsSet) - {}".format(len(paidStudentsSet)))
# len(paidStudentsSet) - 995
        
# Example read from disk file -> Python Dictionary -> list
with open(ENGAGEMENT_DF, 'r') as f:
    reader = csv.DictReader(f)
    daily_engagement = list(reader)
# print("daily_engagement[0] - {}".format(daily_engagement[0]))
#      daily_engagement[0] - {'num_courses_visited': '1.0', 'acct': '0', 'lessons_completed': '0.0', 'utc_date': '2015-01-09', 'total_minutes_visited': '11.6793745', 'projects_completed': '0.0'}

# Example data clean up - daily_engagement.csv  
for engagment_record in daily_engagement:
    engagment_record['lessons_completed'] = int(float(engagment_record['lessons_completed']))
    engagment_record['num_courses_visited'] = int(float(engagment_record['num_courses_visited']))
    engagment_record['projects_completed'] = int(float(engagment_record['projects_completed']))
    engagment_record['total_minutes_visited'] = float(engagment_record['total_minutes_visited'])
    engagment_record['utc_date'] = parse_date(engagment_record['utc_date'])
    tempKey = engagment_record['acct']
    del  engagment_record['acct']
    engagment_record['account_key'] = tempKey 
    if engagment_record['num_courses_visited'] > 0:
        engagment_record['has_visited'] = 1
    else:
        engagment_record['has_visited'] = 0
        
# print("daily_engagement[0] - {}".format(daily_engagement[0]))
#      daily_engagement[0] - {'num_courses_visited': 1, 'utc_date': datetime.datetime(2015, 1, 9, 0, 0), 'lessons_completed': 0, 'account_key': '0', 'projects_completed': 0, 'total_minutes_visited': 11.6793745}
engagement_num_rows = len(daily_engagement)
# print("engagement_num_rows - {}\n".format(engagement_num_rows))
#      engagement_num_rows - 136240

non_udacity_engagement = []
for engagment_record in daily_engagement:
    if engagment_record['account_key'] in udacity_test_accounts:
        pass
    else:
        non_udacity_engagement.append(engagment_record)
# print("len(non_udacity_engagement) - {}".format(len(non_udacity_engagement)))
#        len(non_udacity_engagement) - 135656

paid_engagement_in_first_week = []

# non_udacity_engagement - list
# criteria is_udacity = False AND paid_students account_key
for index, validEngagement in enumerate(non_udacity_engagement):
    if validEngagement['account_key'] in paidStudentsSet:
        myKey = validEngagement['account_key']
        myJoinDate = paid_students[myKey]
        # print("myJoinDate - {}".format(myJoinDate))
        # print("validEngagement['utc_date'] - {}".format(validEngagement['utc_date']))
        # print("validEngagement['account_key'] - {}".format(validEngagement['account_key']))
        # print("index {}".format(index))
        # daily_engagement.csv - utc_date enrollments.csv - join_date 
        # join_date
        time_delta = (validEngagement['utc_date'] - myJoinDate)
        
        # fixed bug 
        # *** add *** and time_delta.days > 0
        # insure validEngagement['utc_date'] AFTER myJoinDate
        # handles use case where student has multiple enrollments.csv join_dates 
        # if most recent enrollments.csv join_date is recent or "large"
        # then the above subtraction will generate a negative number which is indeed less than 7 but use case invalid, incorrect
        # checking for > 0 fixes the bug
        # this insures working with engagement records associated with the MOST RECENT enrollment
        if time_delta.days < 7 and time_delta.days >= 0:
            paid_engagement_in_first_week.append(validEngagement)
            
print("len(paid_engagement_in_first_week) - {}\n".format(len(paid_engagement_in_first_week)))
#        len(paid_engagement_in_first_week) - 21508


# print("len(paid_students) - {}".format(len(paid_students)))
#        len(paid_students) - 995

paid_enrollments = []
print("len(non_udacity_enrollments) - {}".format(len(non_udacity_enrollments)))
#        len(non_udacity_enrollments) - 1622
for enrollment in non_udacity_enrollments:
    if enrollment['account_key'] in paid_students:
        paid_enrollments.append(enrollment)
print("len(paid_enrollments) - {}\n".format(len(paid_enrollments)))
#        len(paid_enrollments) - 1293

print("len(non_udacity_engagement) - {}".format(len(non_udacity_engagement)))
#      len(non_udacity_engagement) - 135656
paid_engagement = []
for engagement in non_udacity_engagement:
    if engagement['account_key'] in paid_students:
        paid_engagement.append(engagement)
print("len(paid_engagement) - {}\n".format(len(paid_engagement)))
#        len(paid_engagement) - 134549

print("len( paid_engagement_in_first_week) - {}".format(len( paid_engagement_in_first_week)))
del paid_engagement_in_first_week[:]
print("len( paid_engagement_in_first_week) - {}\n".format(len( paid_engagement_in_first_week)))

# print("type(paid_engagement) - {}".format(type(paid_engagement)))
# type(paid_engagement) - <class 'list'>

for engagement in paid_engagement:
    pass
    # print("203engagement[0] - {}".format(engagement[0]))
    # print("type(engagement) - {}".format(type(engagement)))
    # print("type(engagement) - {}".format(type(engagement)))

    myKey = engagement['account_key']
    myJoinDate = paid_students[myKey]
    time_delta = (engagement['utc_date'] - myJoinDate)
    # bug fix
    # add time_delta.days >= 0 
    # insures working with engagement records associated with the MOST RECENT enrollment
    # Not an OLD enrollment
    if time_delta.days < 7 and time_delta.days >= 0:
        paid_engagement_in_first_week.append(engagement)
print("len( paid_engagement_in_first_week) - {}\n".format(len( paid_engagement_in_first_week)))

with open(PROJECTSUBMISSIONS_DF, 'r') as f:
    reader = csv.DictReader(f)
    project_submissions = list(reader)   
# print("len(project_submissions) - {}\n".format(len(project_submissions)))
#        len(project_submissions) - 3642

for submission in project_submissions:
    submission['completion_date'] = parse_date(submission['completion_date'])
    submission['creation_date'] = parse_date(submission['creation_date'])
# print("len(project_submissions) - {}\n".format(len(project_submissions)))
#        len(project_submissions) - 3642

non_udacity_submissions = []
for submission in project_submissions:
    if submission['account_key'] in udacity_test_accounts:
        pass
    else:
        non_udacity_submissions.append(submission)
# print("len(non_udacity_submissions) - {}\n".format(len(non_udacity_submissions)))
#        len(non_udacity_submissions) - 3634

print("len(non_udacity_submissions) - {}".format(len(non_udacity_submissions)))
paid_submissions = []
for submission in non_udacity_submissions:
    if submission['account_key'] in paid_students:
        paid_submissions.append(submission)
print("len(paid_submissions) - {}\n".format(len(paid_submissions)))
#        len(paid_submissions) - 3618


# Begin Exploring Student Engagement 17 of 32

# instantiate, declare an empty defaultdict - default dictionary, the value associated with the Dictionary key will be a list
# the key will be account_key
# the list, the value of the key, is a list of engagement records FOR THAT STUDENT (account_key), which are Python Dictionaries, 
engagement_by_account = defaultdict(list)

# iterate loop through the paid_engagement_in_first_week *** list ***
# get the defaultdict Dictionary key - the account_key column
for engagement_record in paid_engagement_in_first_week:
    # print("engagement_record - {}".format(engagement_record))
    #        engagement_record - {'utc_date': datetime.datetime(2015, 2, 20, 0, 0), 'projects_completed': 0, 'num_courses_visited': 0, 'account_key': '69', 'lessons_completed': 0, 'total_minutes_visited': 0.0}
    # print("type(engagement_record) - {}\n".format(type(engagement_record)))
    #        type(engagement_record) - <class 'dict'>
    account_key = engagement_record['account_key']
    # populate the defaultdict, engagement_by_account
    # associate the current engagement_record, (Python Dictionary), with the defaultdict key, the corresponding account_key
    # defaultdict key VALUE is a *** list *** of engagement_record(s) with the corresponding account_key, engagement records FOR THAT STUDENT
    # the value of defaultdict is a list of engagement records corresponding to the account_key
    # append the engagement record to the defaultdict *** list *** 
    engagement_by_account[account_key].append(engagement_record)

# print("type(engagement_by_account) - {}".format(type(engagement_by_account)))
#        type(engagement_by_account) - <class 'collections.defaultdict'>
# print("engagement_by_account - {}".format(engagement_by_account))
# print("len(engagement_by_account) - {}".format(len(engagement_by_account)))
#        len(engagement_by_account) - 995

# Example best practices print, iterate, enumerate, loop, through only part of a Python Dictionary,  print only n (few) Python Dictionary entries, key and value, debug technique
for index, key in enumerate(engagement_by_account):
    if index < 3:
        print("key - {}".format(key))
        # print("type(key) - {}\n".format(type(key)))
        #        type(key) - <class 'str'>
        print("engagement_by_account[key] *** list ***- {}".format(engagement_by_account[key]))
        # print("type(engagement_by_account[key]) - {}".format(type(engagement_by_account[key])))
        #        type(engagement_by_account[key]) - <class 'list'>
        print("len(engagement_by_account[key]) - {}".format(len(engagement_by_account[key])))
print("")

# Example, best practices, instantiate, declare empty Python Dictionary
total_minutes_by_account = {}

# my method, see instructor method below
# Example best practices, get, print the defaultdict key and value, default Python Dictionary
'''
for account_key, engagement_for_student in engagement_by_account.items():
    # print("outeraccount_key - {}".format(account_key))
    #        account_key - 474
    # print("type(account_key) - {}".format(type(account_key)))
    # type(account_key) - <class 'str'>
    # print("engagement_for_student - {}".format(engagement_for_student)) # list, VALUE of key
    # print("type(engagement_for_student) - {}\n".format(type(engagement_for_student)))
    #        type(engagement_for_student) - <class 'list'>
    # print("len(engagement_for_student) - {}\n".format(len(engagement_for_student)))
    #        len(engagement_for_student) - 76
    
    # print("engagement_for_student['total_minutes_visited'] - {}".format(engagement_for_student['total_minutes_visited']))
    # print("engagement_for_student - {}".format(engagement_for_student[])) # list, VALUE of key
    
    # iterate, loop, through the list of engagement records that are the value of the engagement_by_account defaultdict 
    for engagementDictionary in engagement_for_student:
        # print("engagementDictionary - {}".format(engagementDictionary))
        # print("type(engagementDictionary) - {}\n".format(type(engagementDictionary)))
        #        type(engagementDictionary) - <class 'dict'>
        #
        # total_minutes_by_account is a Python Dictionary 
        # instructor method differs from this part
        
        # if the key is already in the total_minutes_by_account Python Dictionary - add, summ
        try:
            total_minutes_by_account[account_key] = total_minutes_by_account[account_key] + engagementDictionary['total_minutes_visited']
        # else create the total_minutes_by_account Python Dictionary entry
        except KeyError:
            total_minutes_by_account[account_key] = engagementDictionary['total_minutes_visited']
        
'''    
    
# instructors method
# iterate, loop through the defaultdict, engagement_by_account, get the key and the value
# get the key - udacity student - account_key
# get the *** list *** of engagement records associated with *** THAT *** student 
for account_key, engagement_for_students in engagement_by_account.items():
    # print("account_key - {}".format(account_key))
    #        account_key - 188
    
    total_minutes = 0
    
    # iterate through the list of that student's engagement records
    # only purpose here is to sum engagement_record['total_minutes_visited']
    for engagement_record in engagement_for_students:
        # print("engagement_record - {}".format(engagement_record))
        total_minutes += engagement_record['total_minutes_visited']
    # now populate the total_minutes_by_account Python Dictionary, account_key, the value is the grand total, the sum of the individual engagement_record['total_minutes_visited']
    total_minutes_by_account[account_key] = total_minutes       
         
# Example best practices print, iterate, enumerate, loop, through only part of a Python Dictionary,  print only n (few) Python Dictionary entries  
for index, key in enumerate(total_minutes_by_account):
    if index < 3:
        print("key - {}\ttotal_minutes_by_account[key] - {} ".format(key, total_minutes_by_account[key]))
        # print("key - {}\ttotal_minutes_by_account[key] - {} ".format(key, total_minutes_by_account[key]))
print("")

# Example, best practices, get the values of a Python Dictionary, just the values, not the key(s), keys
# get the total values for each student
# get just the values from the Python Dictionary
total_minutes = total_minutes_by_account.values()
print("total_minutes -> ")
print(total_minutes)
# print("type(total_minutes) - {}".format(type(total_minutes)))
# type(total_minutes) - <class 'dict_values'>

# now get the statistics associated with those values 
np.mean(list(total_minutes))
print("np.mean(list(total_minutes)) - {}".format(np.mean(list(total_minutes))))
print("np.std(list(total_minutes)) - {}".format(np.std(list(total_minutes))))
print("np.min(list(total_minutes)) - {}".format(np.min(list(total_minutes))))
print("np.max(list(total_minutes)) - {}\n".format(np.max(list(total_minutes))))
# np.max(list(total_minutes)) - 10568.100867332541, > 10,000 minutes 
# 60 * 24 * 7 = 10,080 minutes in a week, 10568.100867332541 -> greater than the number of minutes in a week, somenthing *** WRONG ***

# Begin look for bad data
student_with_max_minutes = None
max_minutes = 0

# Find the student with too many minutes, minutes total > total minutes in 1 week
# Example -iterate, loop, through a Python Dictionary, get key, keys, value, values, pythonDictionary.items(), dot items  
for student, total_minutes in total_minutes_by_account.items():
    if total_minutes > max_minutes:
        max_minutes = total_minutes
        student_with_max_minutes = student
print("student_with_max_minutes - {}".format(student_with_max_minutes))
print("max_minutes - {}\n".format(max_minutes))

# Example iterate, loop through a Python list
# more than 7 records found, should only be seven - *** first_week ***
# Time interval > 1 week, 1st record - January 7 -           -        last record - April 26, should only be 1 week - *** first_week ***
# 'utc_date': datetime.datetime(2015, 1, 7, 0, 0)  -  'utc_date': datetime.datetime(2015, 4, 26, 0, 0), 
# bug fix above *** add ***  and time_delta.days >= 0
for engagement_record in paid_engagement_in_first_week:
    if engagement_record['account_key'] == student_with_max_minutes:
        print("engagement_record - {}".format(engagement_record))
print("")

# Example, best practices, instantiate, declare empty Python Dictionary
total_lessons_completed_by_account = {}

# instructors method
# iterate, loop through the defaultdict, engagement_by_account, get the key and the value
# Example - defaultdict, iterate, loop through get the key AND the key associated value
# get the key - udacity student - account_key, default - dot items()
# get the *** list *** of engagement records associated with *** THAT *** student, default - dot items() 
for account_key, engagement_for_students in engagement_by_account.items():
    # print("account_key - {}".format(account_key))
    #        account_key - 188
    
    lessons_completed = 0
    
    # iterate through the list of that student's engagement records
    # only purpose here is to sum engagement_record['lessons_completed']
    for engagement_record in engagement_for_students:
        # print("engagement_record - {}".format(engagement_record))
        lessons_completed += engagement_record['lessons_completed']
    # now populate the total_lessons_completed_by_account, Python Dictionary, account_key, the value is the grand total, the sum of the individual engagement_record['lessons_completed']
    total_lessons_completed_by_account[account_key] = lessons_completed   
    
total_lessons = total_lessons_completed_by_account.values()

# np.mean(list(total_lessons))
print("np.mean(list(total_lessons)) - {}".format(np.mean(list(total_lessons))))
print("np.std(list(total_lessons)) - {}".format(np.std(list(total_lessons))))
print("np.min(list(total_lessons)) - {}".format(np.min(list(total_lessons))))
print("np.max(list(total_lessons)) - {}".format(np.max(list(total_lessons))))
print("")
       
# Example best practices print, iterate, enumerate, loop, through only part of a Python Dictionary,  print only n (few) Python Dictionary entries  
for index, key in enumerate(total_minutes_by_account):
    if index < 3:
        print("key - {}\ttotal_minutes_by_account[key] - {} ".format(key, total_minutes_by_account[key]))
        # print("key - {}\ttotal_minutes_by_account[key] - {} ".format(key, total_minutes_by_account[key]))
print("")

total_visits_in_first_week = {}

# engagement_by_account = defaultdict(list)
# break out the defaultdict(list)
# the dictionary key is the account_key, the one value associated with that key is a *** list *** of records
for account_key, engagement_for_students in engagement_by_account.items():
    # print("account_key - {}".format(account_key))
    #        account_key - 188
    
    visits_for_account = 0
    
    # iterate through the list of that student's engagement records
    # only purpose here is to sum engagement_record['has_visited']
    for engagement_record in engagement_for_students:
        # print("engagement_record - {}".format(engagement_record))
        visits_for_account += engagement_record['has_visited']
    # now populate the total_lessons_completed_by_account, Python Dictionary, account_key, the value is the grand total, the sum of the individual engagement_record['lessons_completed']
    total_visits_in_first_week[account_key] = visits_for_account   
    
# Example get the values
total_visits = total_visits_in_first_week.values()
# print("type(total_visits) - {}".format(type(total_visits)))
#        type(total_visits) - <class 'dict_values'>
print("np.mean(list(total_visits)) - {}".format(np.mean(list(total_visits))))
print("np.min(list(total_visits)) - {}".format(np.min(list(total_visits))))
print("np.max(list(total_visits)) - {}".format(np.max(list(total_visits))))
print("np.std(list(total_visits)) - {}\n".format(np.std(list(total_visits))))
 
print("paid_submissions[0] - {}\n".format(paid_submissions[0]))

# Splitting out Passing Students 21/32 
subway_project_lesson_keys = ['746169184', '3176718735']  
passing_engagement = []
non_passing_engagement = []

# Example initialize an empty Python set  
pass_subway_project = set()

# First populate a *** set *** of the project_submissions.csv records, account_keys meeting the criteria
# Example *** set *** - many to one conversion
# Example *** set *** - for many records in file - 1 entry in set  
for mySubmission in paid_submissions:
    if (mySubmission['assigned_rating'] == 'PASSED') or (mySubmission['assigned_rating'] == 'DISTINCTION'):
        if mySubmission['lesson_key'] in subway_project_lesson_keys:
            pass_subway_project.add(mySubmission['account_key'])

# Next iterate through the list of engagement records
# populate lists driven by set population
for engagement_record in paid_engagement_in_first_week:
    if engagement_record['account_key'] in pass_subway_project:
        passing_engagement.append(engagement_record)
    else:
        non_passing_engagement.append(engagement_record)

print("passing_engagement[0]) - {}".format(passing_engagement[0]))
print("len(pass_subway_project) - {}".format(len(pass_subway_project)))
print("len(passing_engagement) - {}".format(len(passing_engagement)))
print("len(non_passing_engagement) - {}".format(len(non_passing_engagement)))
print("")

passedLessonsCompleted = {}
failedLessonsCompleted = {}

for account_key, engagement_for_students in engagement_by_account.items():
    tally = 0
    if account_key in pass_subway_project:
        for myEngagementRecord in engagement_for_students:
            # print("myEngagementRecord - {}".format(myEngagementRecord))
            tally += myEngagementRecord['lessons_completed']
        passedLessonsCompleted[account_key] = tally
    else:
        for myEngagementRecord in engagement_for_students:
            tally += myEngagementRecord['lessons_completed']
        failedLessonsCompleted[account_key] = tally
        
passedValues = passedLessonsCompleted.values()
failedValues = failedLessonsCompleted.values()

# print("passedValues - {}".format(passedValues))
print("np.mean(list(passedValues)) - {}".format(np.mean(list(passedValues))))
# print("failedValues - {}".format(failedValues))
print("np.mean(list(failedValues)) - {}".format(np.mean(list(failedValues))))

plt.hist(list(passedValues))
plt.show()

 
print("Finished")

  

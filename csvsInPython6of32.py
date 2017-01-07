'''
Created on Dec 24, 2016

@author: Menfi
'''

import os
# import unicodecsv
import csv 
from datetime import datetime as dt

print("")

DATADIR = '/Users/Menfi/Documents/gitBaseDirectory/IntroToDataAnalysis/dataFiles'

ENROLLMENT_FN = 'enrollments.csv'
ENROLLMENT_DF = os.path.join(DATADIR,ENROLLMENT_FN)

ENGAGEMENT_FN = 'daily_engagement.csv'
ENGAGEMENT_DF = os.path.join(DATADIR,ENGAGEMENT_FN)

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

enrollments = []

'''
Example - read csv, file populate Python Dictionary, column headings Dictionary key
'''

f = open (ENROLLMENT_DF, 'r')
reader = csv.DictReader(f)

# print("type(reader) - {}".format(type(reader)))
#        type(reader) - <class 'csv.DictReader'>

for row in reader:
    enrollments.append(row)
f.close

'''
Example 1 - iterate through a Python list, 3 times, print index, print value 
Example 1 - access list square bracket, colon 
'''
for index, value in enumerate(enrollments[:2]):
    # print("index - {}".format(index))
    # print("value - {}".format(value))
    print("")
    
# print("enrollments[0] - {}".format(enrollments[0]))
# enrollments[0] - {'is_canceled': 'True', 'account_key': '448', 'join_date': '2014-11-10', 'status': 'canceled', 'days_to_cancel': '65', 'is_udacity': 'True', 'cancel_date': '2015-01-14'}

# print("type(enrollments) - {}".format(type(enrollments)))
#      type(enrollments) - <class 'list'>

# print("type(enrollments[0]) - {}".format(type(enrollments[0])))
#      type(enrollments[0]) - <class 'dict'>

'''
Example 2 -  read csv file, populate Python Dictionary, column headings Dictionary key, with, cleaner example - note with
'''
with open(ENROLLMENT_DF, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        enrollments.append(row)
'''
print("enrollments[0] - {}".format(enrollments[0]))
       enrollments[0] - {'is_canceled': 'True', 'account_key': '448', 'is_udacity': 'True', 'days_to_cancel': '65', 'join_date': '2014-11-10', 'cancel_date': '2015-01-14', 'status': 'canceled'}
'''
for index, value in enumerate(enrollments[:2]):
    # print("index - {}".format(index))
    # print("value - {}".format(value))
    print("")

'''
Example 3 - cleanest, simplest example - read csv file, populate Python Dictionary, column headings Dictionary key, with, clean population of Python list from Python Dictionary, enrollments1 = [] NOT NEEDED
Example 3 - from csv file to Python Dictionary to list
'''
with open(ENROLLMENT_DF, 'r') as f:
    reader = csv.DictReader(f)
    # enrollments1 = [] NOT NEEDED
    # enrollments1 = list(reader) # Works comment out, only going through the csv file ONCE
    enrollments = list(reader) # Needed for course work

print("enrollments[0] - {}".format(enrollments[0]))
#        enrollments[0] - {'is_canceled': 'True', 'account_key': '448', 'is_udacity': 'True', 'days_to_cancel': '65', 'join_date': '2014-11-10', 'cancel_date': '2015-01-14', 'status': 'canceled'}

# access a list, enumerate list, index and value, using square bracket colon notation 
for index, value in enumerate(enrollments[:1]):
    # print("index - {}".format(index))
    # print("value - {}".format(value))
    # print("")
    pass
    
# access Python Dictionary value by key     
for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])
print("enrollments[0] - {}".format(enrollments[0]))

enrollment_num_rows = len(enrollments)
print("enrollment_num_rows - {}".format(enrollment_num_rows))

# Example declare empty Python set, add to a Python set, use keyword set  
# Example populate Python set, add to Python set with *** add ***
enrollmentSet = set()
for enrollment in enrollments: 
    enrollmentSet.add(enrollment['account_key'])
enrollment_num_unique_students = len(enrollmentSet) 
# enrollments = 1640, unique enrollments = 1302
# A student can enroll, then cancel, the re-enroll
# total enrollments greater than unique enrollments
# 1640 - 1302 = 338
print("enrollment_num_unique_students - {}\n".format(enrollment_num_unique_students))

udacity_test_accounts = set()
for enrollment in enrollments: 
    if enrollment['is_udacity']:
        udacity_test_accounts.add(enrollment['account_key'])
print("udacity_test_accounts - {}".format(udacity_test_accounts))
print("len(udacity_test_accounts) - {}".format(len(udacity_test_accounts)))

udacity_test_accounts = set()
for enrollment in enrollments: 
    if enrollment['is_udacity']:
        udacity_test_accounts.add(enrollment['account_key'])
print("udacity_test_accounts - {}".format(udacity_test_accounts))
print("len(udacity_test_accounts) - {}".format(len(udacity_test_accounts)))

non_udacity_enrollments = []
for enrollment in enrollments:
    if enrollment['account_key'] in udacity_test_accounts:
        pass
    else:
        non_udacity_enrollments.append(enrollment)
print("len(non_udacity_enrollments) - {}\n".format(len(non_udacity_enrollments)))
    
'''
Example daily_engagement.csv - cleanest, simplest example - read csv file, populate Python Dictionary, column headings Dictionary key, with, clean population of Python list from Python Dictionary     
'''
with open(ENGAGEMENT_DF, 'r') as f:
    reader = csv.DictReader(f)
    # daily_engagement = [] NOT NEEDED
    daily_engagement = list(reader)
print("daily_engagement[0] - {}".format(daily_engagement[0]))
#        daily_engagement[0] - {'num_courses_visited': '1.0', 'acct': '0', 'lessons_completed': '0.0', 'utc_date': '2015-01-09', 'total_minutes_visited': '11.6793745', 'projects_completed': '0.0'}

for engagment_record in daily_engagement:
    engagment_record['lessons_completed'] = int(float(engagment_record['lessons_completed']))
    engagment_record['num_courses_visited'] = int(float(engagment_record['num_courses_visited']))
    engagment_record['projects_completed'] = int(float(engagment_record['projects_completed']))
    engagment_record['total_minutes_visited'] = float(engagment_record['total_minutes_visited'])
    engagment_record['utc_date'] = parse_date(engagment_record['utc_date'])
    tempKey = engagment_record['acct']
    del  engagment_record['acct']
    engagment_record['account_key'] = tempKey 
print("daily_engagement[0] - {}".format(daily_engagement[0]))
engagement_num_rows = len(daily_engagement)
print("engagement_num_rows - {}".format(engagement_num_rows))

# Example declare empty Python set, add to a Python set, use keyword set, create empty set
# Example populate Python set, add to Python set with *** add ***
engagementSet = set()
for engagment_record in daily_engagement:
    engagementSet.add(engagment_record['account_key'])
engagement_num_unique_students = len(engagementSet)
print("engagement_num_unique_students - {}".format(engagement_num_unique_students))

non_udacity_engagement = []
for engagment_record in daily_engagement:
    if engagment_record['account_key'] in udacity_test_accounts:
        pass
    else:
        non_udacity_engagement.append(engagment_record)
print("len(non_udacity_engagement) - {}\n".format(len(non_udacity_engagement)))

'''
Example daily_engagement.csv - cleanest, simplest example - read csv file, populate Python Dictionary, column headings Dictionary key, with, clean population of Python list from Python Dictionary     
'''
with open(PROJECTSUBMISSIONS_DF, 'r') as f:
    reader = csv.DictReader(f)
    # project_submissions = [] NOT NEEDED
    project_submissions = list(reader)    
print("project_submissions[0] - {}".format(project_submissions[0]))
#      project_submissions[0] - {'completion_date': '2015-01-16', 'lesson_key': '3176718735', 'processing_state': 'EVALUATED', 'creation_date': '2015-01-14', 'assigned_rating': 'UNGRADED', 'account_key': '256'}

for submission in project_submissions:
    submission['completion_date'] = parse_date(submission['completion_date'])
    submission['creation_date'] = parse_date(submission['creation_date'])
print("project_submissions[0] - {}".format(project_submissions[0])) 
#      project_submissions[0] - {'completion_date': datetime.datetime(2015, 1, 16, 0, 0), 'lesson_key': '3176718735', 'processing_state': 'EVALUATED', 'creation_date': datetime.datetime(2015, 1, 14, 0, 0), 'assigned_rating': 'UNGRADED', 'account_key': '256'}
submission_num_rows = len(project_submissions)
print("submission_num_rows - {}".format(submission_num_rows))

submissionSet = set()
for submission in project_submissions:
    submissionSet.add(submission['account_key'])
submission_num_unique_students = len(submissionSet)
print("submission_num_unique_students - {}".format(submission_num_unique_students))

non_udacity_submissions = []
for submission in project_submissions:
    if submission['account_key'] in udacity_test_accounts:
        pass
    else:
        non_udacity_submissions.append(submission)
print("len(non_udacity_submissions) - {}\n".format(len(non_udacity_submissions)))
# 3642 total project submissions from 743 unique students

'''
'''

# look for enrollment data with no corresponding engagement data
# total daily engagements - 136240 - multiple entries for each student
# total daily engagements (unique) - 1237 - multiple entries for each student
# unique enrollments ids - 1302
# unique engagements ids - 1237
# 1302 - 1237 = 65 unique enrolled students, missing from the unique engagements total
# enrollments.csv - is_udacity = True = 18
# 65 - 18 = 47 
#
# print("daily_engagement[0]['account_key'] - {}".format(daily_engagement[0]['account_key']))
# daily_engagement[0]['account_key'] - 0 - part of the course
# 

isUdacityCount = 0
zeroDaysToCancel = 0

enrolledAccountNoEngagementsHowMany = enrollment_num_unique_students - engagement_num_unique_students
print("enrolledAccountNoEngagementsHowMany - {}".format(enrolledAccountNoEngagementsHowMany))

enrolledAccountNoEngagementsSet = enrollmentSet - engagementSet
print("enrolledAccountNoEngagementsSet - {}".format(enrolledAccountNoEngagementsSet))
print("")

for enrollment in enrollments:
    if enrollment['is_udacity']:
        isUdacityCount += 1 
    elif (enrollment['join_date'] == enrollment['cancel_date']) and (enrollment['days_to_cancel'] == 0):
        zeroDaysToCancel +=1
print("isUdacityCount - {}".format(isUdacityCount))
print("zeroDaysToCancel - {}".format(zeroDaysToCancel))
 
zeroDaysStudent = 0
for enrollment in enrollments: 
    if enrollment['account_key'] in engagementSet:
        pass
    elif (enrollment['is_udacity'] == False) and (enrollment['join_date'] == enrollment['cancel_date']) and  (enrollment['days_to_cancel'] == 0):
        zeroDaysStudent += 1    
print("zeroDaysStudent - {}\n".format(zeroDaysStudent)) 

enrolledAtLeatOneDay = 0
for enrollment in enrollments: 
    if enrollment['account_key'] in engagementSet:
        pass
    elif (enrollment['join_date'] != enrollment['cancel_date']):
        print("enrollment - {}".format(enrollment))
        enrolledAtLeatOneDay += 1    
print("enrolledAtLeatOneDay - {}\n".format(enrolledAtLeatOneDay)) 

print("")
x = 5
print(" - {}".format(x))
print("type(x) - {}".format(type(x)))
print("")

print(" -> ")
print()
print("")

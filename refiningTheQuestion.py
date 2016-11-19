
import os
import unicodecsv 
from datetime import datetime as dt
from collections import defaultdict
import numpy
import pprint


paid_students = {}
paid_engagement_in_first_week = []
# avgMinDictionary = {}
avgMinDictionary = defaultdict(list)
engagement_by_account = defaultdict(list)


DATADIR = '/Users/Menfi/Documents/gitBaseDirectory/IntroToDataAnalysis/dataFiles'
DATAFILE = 'enrollments.csv'
DATAFILE = os.path.join(DATADIR, DATAFILE)

ENGAGEMENT_FN = 'daily_engagement.csv'
ENGAGEMENT_DF = os.path.join(DATADIR, ENGAGEMENT_FN)


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

# DATAFILE = 'enrollments.csv'
with open (DATAFILE, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)
print ("")

# enrollment.csv data clean up
for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])    
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])
    
for enrollment in enrollments[:2]:
    pass
    
    # enrollment - {'is_canceled': True, 'join_date': datetime.datetime(2014, 11, 5, 0, 0), 'status': 'canceled', 'account_key': '448', 'is_udacity': True, 'cancel_date': datetime.datetime(2014, 11, 10, 0, 0), 'days_to_cancel': 5}
    # print("enrollment - {}\n".format(enrollment))
    # <class 'dict'>
    # print("type(enrollment) - {}\n".format(type(enrollment)))

# populate the paid_students Dictionary from the enrollments.csv file 
# account_key : enrollment['join_date']
# {'1244': datetime.datetime(2015, 5, 17, 0, 0), '25
for enrollment in enrollments:
    if not enrollment['is_udacity']:
        if (enrollment['days_to_cancel'] == None):
            if enrollment['account_key'] not in paid_students or enrollment['join_date'] > paid_students[enrollment['account_key']]:
                paid_students[enrollment['account_key']] = enrollment['join_date'] 
        elif int(enrollment['days_to_cancel']) > 7 :
            if enrollment['account_key'] not in paid_students:
                paid_students[enrollment['account_key']] = enrollment['join_date'] 
                #print("paid_students[enrollment['account_key']] - {}\n".format(paid_students[enrollment['account_key']]))
            elif enrollment['join_date'] > paid_students[enrollment['account_key']]:
                paid_students[enrollment['account_key']] = enrollment['join_date']
                # print("paid_students[enrollment['account_key']] - {}\n".format(paid_students[enrollment['account_key']]))
       
# paid_students - account_key : enrollment['join_date']
# '337': datetime.datetime(2015, 2, 10, 0, 0)
# print("paid_students is {}".format(paid_students))
print("len(paid_students) is {}\n".format(len(paid_students))) # 995

for key, value in paid_students.items():
    pass
    # print("key - {}, value - {}".format(key, value))
    
#
#
#

# daily_engagement.csv
with open (ENGAGEMENT_DF, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    daily_engagement = list(reader)

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
    
# {'projects_completed': 0, 'lessons_completed': 0, 'account_key': '0', 'num_courses_visited': 1, 'utc_date': datetime.datetime(2015, 1, 9, 0, 0), 'total_minutes_visited': 11.6793745}
# {'projects_completed': 0, 'lessons_completed': 0, 'account_key': '0', 'num_courses_visited': 2, 'utc_date': datetime.datetime(2015, 1, 10, 0, 0), 'total_minutes_visited': 37.2848873333}
for engagement in daily_engagement[:2]:
    pass
    # print("engagement - {}".format(engagement))

# len(daily_engagement) - 136240
print("len(daily_engagement) - {}\n".format(len(daily_engagement)))

# populate the paid_engagement_in_first_week
for engagement_record in daily_engagement:
    #print("{} - {}".format(i, daily_engagement[i]))    
    # print("{} - daily_engagement['account_key'] - {}".format(i, daily_engagement[i]['account_key']))    
    # print("{} - daily_engagement['utc_date'] - {}".format(i, daily_engagement[i]['utc_date']))
    if engagement_record['account_key'] in paid_students:
        #print("daily_engagement[i]['account_key'] - {}".format(daily_engagement[i]['account_key']))
        # print("paid_students - {}".format(paid_students))
        # print("paid_students - {}".format(paid_students[daily_engagement[i]['account_key']]))
        enrollmentsJoinDate = paid_students[engagement_record['account_key']]
        # print("enrollmentsJoinDate - {}".format(enrollmentsJoinDate))
        
        engagementRecordUTCDate = engagement_record['utc_date']
        # print("engagementRecordUTCDate - {}".format(engagementRecordUTCDate))
        
        lengthOfTime = engagementRecordUTCDate - enrollmentsJoinDate
        days = lengthOfTime.days
        # print("days - {}\n".format(days))
        # print("type(days) - {}".format(type(days))) # int
        
        # if days < 7:
        if days < 7 and days >= 0: # fix
            paid_engagement_in_first_week.append(engagement_record)
            
# list 
# print("type(paid_engagement_in_first_week) - {}".format(type(paid_engagement_in_first_week)))


# {'lessons_completed': 0, 'utc_date': datetime.datetime(2015, 1, 9, 0, 0), 'num_courses_visited': 1, 'account_key': '0', 'projects_completed': 0, 'total_minutes_visited': 11.6793745}
# {'lessons_completed': 0, 'utc_date': datetime.datetime(2015, 1, 10, 0, 0), 'num_courses_visited': 2, 'account_key': '0', 'projects_completed': 0, 'total_minutes_visited': 37.2848873333}
for paid_engagement in paid_engagement_in_first_week[:2]:
    pass
    # print("paid_engagement - {}".format(paid_engagement))

# len(paid_engagement_in_first_week) - 6919
# print("len(paid_engagement_in_first_week) - {}\n".format(len(paid_engagement_in_first_week)))
 
# engagement_by_account = defaultdict(list)
# append minutes to Dictionary value - ** list ** 
for engagement_record in paid_engagement_in_first_week:
    account_key = engagement_record['account_key']
    engagement_by_account[account_key].append(engagement_record) # instructor engagement_by_account = defaultdict(list)
    avgMinDictionary[engagement_record['account_key']].append(engagement_record['total_minutes_visited']) # MGC avgMinDictionary = defaultdict(list)
    
for key, value in engagement_by_account.items():
    pass
    # print("key - {}, value - {}".format(key, value))
  
#   
#             {'0': [{'account_key': '0',
#                     'lessons_completed': 0,
#                     'num_courses_visited': 1,
#                     'projects_completed': 0,
#                     'total_minutes_visited': 11.6793745,
#                     'utc_date': datetime.datetime(2015, 1, 9, 0, 0)},
#                    
#                    {'account_key': '0',
#                     'lessons_completed': 0,
#                     'num_courses_visited': 2,
#                     'projects_completed': 0,
#                     'total_minutes_visited': 37.2848873333,
#                     'utc_date': datetime.datetime(2015, 1, 10, 0, 0)},


total_minutes_by_account = {}
total_lessons_by_account = {}
total_daysVisited_by_account = {}

for account_key, engagement_for_student in engagement_by_account.items():
    # the key
    # account_key - 596
    # print("account_key - {}".format(account_key))
    
    # the list of engagement records 
    # engagement_for_student - [{'utc_date': datetime.datetime(2015, 5, 12, 0, 0), 'num_courses_visited': 1, 'total_minutes_visited': 2.48917566667, 'account_key': '596', 'projects_completed': 0, 'lessons_completed': 0}, {'utc_date': datetime.datetime(2015, 5, 13, 0, 0), 'num_courses_visited': 2, 'total_minutes_visited': 59.4449115, 'account_key': '596', 'projects_completed': 0, 'lessons_completed': 1}, {'utc_date': datetime.datetime(2015, 5, 14, 0, 0), 'num_courses_visited': 1, 'total_minutes_visited': 92.780323, 'account_key': '596', 'projects_completed': 0, 'lessons_completed': 1}, {'utc_date': datetime.datetime(2015, 5, 15, 0, 0), 'num_courses_visited': 1, 'total_minutes_visited': 34.3024258333, 'account_key': '596', 'projects_completed': 0, 'lessons_completed': 0}, {'utc_date': datetime.datetime(2015, 5, 16, 0, 0), 'num_courses_visited': 1, 'total_minutes_visited': 37.2178128333, 'account_key': '596', 'projects_completed': 0, 'lessons_completed': 1}, {'utc_date': datetime.datetime(2015, 5, 17, 0, 0), 'num_courses_visited': 0, 'total_minutes_visited': 0.0, 'account_key': '596', 'projects_completed': 0, 'lessons_completed': 0}, {'utc_date': datetime.datetime(2015, 5, 18, 0, 0), 'num_courses_visited': 1, 'total_minutes_visited': 84.837714, 'account_key': '596', 'projects_completed': 0, 'lessons_completed': 1}]
    # print("engagement_for_student - {}\n".format(engagement_for_student))
    # list
    # print("type(engagement_for_student) - {}\n".format(type(engagement_for_student)))
    total_minutes = 0
    total_lessonsForAnAccount = 0
    total_lessons = 0 
    
    daysVisited = 0
    daysVisitedAll = 0
    
    # loop through the list of engagement records 
    for engagement_record in engagement_for_student:
        # print("201 account_key - {}, engagement_record['num_courses_visited'] - {}".format(account_key, engagement_record['num_courses_visited']))
        if  engagement_record['num_courses_visited'] > 0:
            daysVisited += 1

        # engagement_record['total_minutes_visited'] - 197.3559125
        # print("engagement_record['total_minutes_visited'] - {}".format(engagement_record['total_minutes_visited']))
        
        # engagement_record['lessons_completed'] - 0
        #print("engagement_record['lessons_completed'] - {}\n".format(engagement_record['lessons_completed']))
        
        total_minutes += engagement_record['total_minutes_visited']
        total_lessonsForAnAccount += engagement_record['lessons_completed']

    total_minutes_by_account[account_key] = total_minutes
    total_lessons_by_account[account_key] = total_lessonsForAnAccount
    
    # print("account_key - {}, daysVisited - {}".format(account_key, daysVisited))
    # if daysVisited > 0:
    total_daysVisited_by_account[account_key] = daysVisited
    # print("account_key - {}, total_daysVisited_by_account[account_key] - {}\n".format(account_key, total_daysVisited_by_account[account_key]))
    
    
total_minutes = total_minutes_by_account.values()
# print("total_minutes - {}".format(total_minutes))
# print("total_minutes_by_account - {}\n".format(total_minutes_by_account))

# print("total_lessonsForAnAccount - {}".format(total_lessonsForAnAccount))
total_lessons = total_minutes_by_account.values()
# print("total_lessons - {}\n".format(total_lessons))

daysVisitedList = []

for i in total_daysVisited_by_account:
    daysVisitedList.append(total_daysVisited_by_account[i])

print("numpy.mean(daysVisitedList) - {}".format(numpy.mean(daysVisitedList)))
print("numpy.std(daysVisitedList) - {}".format(numpy.std(daysVisitedList)))
print("numpy.min(daysVisitedList) - {}".format(numpy.min(daysVisitedList)))
print("numpy.max(daysVisitedList) - {}\n".format(numpy.max(daysVisitedList)))

total_minutes = []
for i in total_minutes_by_account:
    
    if total_minutes_by_account[i] > 10568: # find the bad data 
        print("{} - {}".format(i, total_minutes_by_account[i]))
    # print("{} - {}".format(i, total_minutes_by_account[i]))
    total_minutes.append(total_minutes_by_account[i])
    
total_lessons = []
for i in total_lessons_by_account:
    
    if total_minutes_by_account[i] > 10568: # find the bad data
        pass 
        # print("{} - {}".format(i, total_minutes_by_account[i]))
    # print("{} - {}".format(i, total_minutes_by_account[i]))
    total_lessons.append(total_lessons_by_account[i])


# numpy.min(total_minutes) - 0.0
print("numpy.min(total_minutes) - {}".format(numpy.min(total_minutes)))

# 7 * 24 * 60 = 10,080 maximum minutes too large 
# numpy.max(total_minutes) - 10568.100867332541
# numpy.max(total_minutes) - 3564.7332644989997 - after the fix 
print("numpy.max(total_minutes) - {}".format(numpy.max(total_minutes)))

# numpy.mean(total_minutes) - 647.5901738262693
# video says - 647.59017382626985
# numpy.mean(total_minutes) - 306.70832675342825 - after the fix 
print("numpy.mean(total_minutes) - {}".format(numpy.mean(total_minutes)))

# numpy.std(total_minutes) - 1129.2712104188108
# numpy.std(total_minutes) - 412.99693340852957 - after the fix
print("numpy.std(total_minutes) - {}\n".format(numpy.std(total_minutes)))
    
# print("engagement_by_account - {}".format(engagement_by_account))
# pprint.pprint(engagement_by_account)
    

# append average to Dictionary value - ** list **    
for key in avgMinDictionary.keys():
    # print("key - {}".format(key))
    # print("avgMinDictionary[key] - {}".format(avgMinDictionary[key]))
    tempDictionary = {'average' : numpy.average(avgMinDictionary[key])}
    # print("type(avgMinDictionary[key]) - {}\n".format(type(avgMinDictionary[key])))
    avgMinDictionary[key].append(tempDictionary)
    
# '179': [7.74253766667, 53.0285923333, 262.488002, 195.501943333, 184.320763667, 200.753508667, 9.84054133333, {'average': 130.52512700004283}]
print("avgMinDictionary - {}".format(avgMinDictionary))
print("len(avgMinDictionary) - {}\n".format(len(avgMinDictionary)))
    
# pprint.pprint(avgMinDictionary)

print("numpy.min(total_lessons) - {}".format(numpy.min(total_lessons)))
print("numpy.max(total_lessons) - {}".format(numpy.max(total_lessons)))
print("numpy.mean(total_lessons) - {}".format(numpy.mean(total_lessons)))
print("numpy.std(total_lessons) - {}".format(numpy.std(total_lessons)))

print("")


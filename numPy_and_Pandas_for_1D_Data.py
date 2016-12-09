
import os
import unicodecsv 
from datetime import datetime as dt
import time
import pandas as pd

DATADIR = '/Users/Menfi/Documents/gitBaseDirectory/IntroToDataAnalysis/dataFiles'

ENGAGEMENT_FN = 'daily_engagement.csv'
ENGAGEMENT_DF = os.path.join(DATADIR, ENGAGEMENT_FN)

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')

print("")
begin = time.time()
with open (ENGAGEMENT_DF, 'rb') as f:
    engagementReader = unicodecsv.DictReader(f)
    daily_engagement = list(engagementReader)
end = time.time()

print("read - end - begin - {}".format(end - begin))
print("len(daily_engagement) - {}\n".format(len(daily_engagement)))
    
for engagementRecord in daily_engagement[:2]:
    print("engagementRecord before cleanup - {}".format(engagementRecord))    

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

print("")
for engagementRecord in daily_engagement[:2]:
    print("engagementRecord after cleanup - {}".format(engagementRecord))    


print("")
print("type(engagementRecord) - {}".format(type(engagementRecord)))
print("type(daily_engagement) - {}\n".format(type(daily_engagement)))


unique_engagement_students = set()
begin = time.time()
for engagementRecord in daily_engagement:
    unique_engagement_students.add(engagementRecord['account_key']) 
end = time.time()
print("unique - end - begin - {}".format(end - begin))

# len(unique_engagement_students) - 1237 - agrees with video  
print("len(unique_engagement_students) - {}\n".format(len(unique_engagement_students)))

begin = time.time()
daily_engagement = pd.read_csv(ENGAGEMENT_DF)
end = time.time()


print("panda - len(daily_engagement) - {}".format(len(daily_engagement)))
print("panda - read - end - begin - {}\n".format(end - begin))

# type(daily_engagement) - <class 'pandas.core.frame.DataFrame'>
print("type(daily_engagement) - {}".format(type(daily_engagement)))

begin = time.time()
daily_engagement['acct'].unique()
end = time.time()
print("panda - unique - end - begin - {}\n".format(end - begin))

# for i in range(0, len(daily_engagement)):
for i in range(0, 3):
    print (daily_engagement.iloc[i])
    print ("daily_engagement.iloc[i]['acct'] - {}".format(daily_engagement.iloc[i]['acct']))
    print ("daily_engagement.iloc[i]['total_minutes_visited'] - {}".format(daily_engagement.iloc[i]['total_minutes_visited']))
    print()




 
 









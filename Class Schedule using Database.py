import pandas as pd
# Input Code for Determining Selected Day:
day = input("\nWhich Day's Schedule Are You Looking For?  ")
if day == ('monday' or 'tuesday' or 'wednesday' or 'thursday' or 'friday' or 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday'):
    print("\nHere is the schedule for selected day")
else:
    print("\nPlease select a valid day")
# Database Definitions for each day
Monday = {                                                
    'Class':['CP1850','CR1130','CP1420','CP1555'],                      #Class
    'Time':['8:30-10:30','10:30-11:30','12:30-2:30','2:30-4:30'],       #Time
    'Classroom':['K205','K205','K205', 'K205']}                         #Classroom
dm = pd.DataFrame(Monday)
Tuesday = {                                                
    'Class':['CP1555','MA1900','CP1461','CP1420'],   
    'Time':['8:30-10:30','12:30-1:30','1:30-3:30','3:30-4:30'],
    'Classroom':['K205','D207','K205','K205']}
dt = pd.DataFrame(Tuesday)
Wednesday = {                                                
    'Class':['CP1850','CM1400','MA1900'],    
    'Time':['8:30-10:30','10:30-12:30','2:30-4:30'],
    'Classroom':['K205','F210','K106']}
dw = pd.DataFrame(Wednesday)
Thursday = {                                                
    'Class':['CP1850','CP1461','MA1900'],   
    'Time':['8:30-10:30','10:30-12:30','1:30-3:30'],
    'Classroom':['K205','K205','K106']}
dth = pd.DataFrame(Thursday)
Friday = {                                                
    'Class':['CP1850','CP1400'],    
    'Time':['8:30-10:30','11:30-12:30'],
    'Classroom':['K205','A305']}
df = pd.DataFrame(Friday)
#If input statements for each day
if day == "Monday":
    print(dm)
elif day == "Tuesday":
    print(dt)
elif day == "Wednesday":
    print(dw)
elif day == "Thursday":
    print(dth)
elif day == "Friday":
    print(df)
elif day == "monday":
    print(dm)
elif day == "tuesday":
    print(dt)
elif day == "wednesday":
    print(dw)
elif day == "thursday":
    print(dth)
elif day == "friday":
    print(df)
import pandas as pd
Monday = {
    'Class': ['CP1850', 'CR1130', 'CP1420', 'CP1555'],  # Class
    'Time': ['8:30-10:30', '10:30-11:30', '12:30-2:30', '2:30-4:30'],  # Time
    'Classroom': ['K205', 'K205', 'K205', 'K205']}  # Classroom
dm = pd.DataFrame(Monday)
Tuesday = {
    'Class': ['CP1555', 'MA1900', 'CP1461', 'CP1420'],
    'Time': ['8:30-10:30', '12:30-1:30', '1:30-3:30', '3:30-4:30'],
    'Classroom': ['K205', 'D207', 'K205', 'K205']}
dt = pd.DataFrame(Tuesday)
Wednesday = {
    'Class': ['CP1850', 'CM1400', 'MA1900'],
    'Time': ['8:30-10:30', '10:30-12:30', '2:30-4:30'],
    'Classroom': ['K205', 'F210', 'K106']}
dw = pd.DataFrame(Wednesday)
Thursday = {
    'Class': ['CP1850', 'CP1461', 'MA1900'],
    'Time': ['8:30-10:30', '10:30-12:30', '1:30-3:30'],
    'Classroom': ['K205', 'K205', 'K106']}
dth = pd.DataFrame(Thursday)
Friday = {
    'Class': ['CP1850', 'CP1400'],
    'Time': ['8:30-10:30', '11:30-12:30'],
    'Classroom': ['K205', 'A305']}
df = pd.DataFrame(Friday)
program_running = True
while program_running:
    day = str(input("\nWhich Day's Schedule Are You Looking For? "))
    if day == 'monday' or 'Monday':
        print("Here's Monday's Schedule:")
        print(dm)
    elif day == 'tuesday' or 'Tuesday':
        print("Here's Tuesday's Schedule:")
        print(dt)
    elif day == 'wednesday' or 'Wednesday':
        print("Here's Wednesday's Schedule:")
        print(dw)
    elif day == 'Thursday' or "thursday":
        print("Here's Thursday's Schedule:")
        print(dth)
    elif day == 'Friday' or "friday":
        print("Here's Friday's Schedule:")
        print(df)
        print("Have a good weekend!")
    else:
        print("Not a Valid Day. Please Try Again.")
program_running = False
print("Have a great day!")



    
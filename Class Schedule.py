day = input("\nWhich Day's Schedule Are You Looking For?  ")
if(day != "monday" or "tuesday" or "wednesday" or "thursday" or "friday" or "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday"):
    print("\nPlease select a valid day")
else:
    print("\nHere is the schedule for selected day")

Monday = """\n8:30-10:30\t10:30-11:30\t12:30-2:30\t2:30-4:30
K205\t\tK205\t\tK205\t\tK205
CP1850\t\tCR1130\t\tCP1420\t\tCP1555"""
Tuesday = """\n8:30-10:30\t12:30-1:30\t1:30-3:30\t3:30-4:30
K205\t\tD207\t\tK205\t\tK205
CP1555\t\tMA1900\t\tCP1461\t\tCP1420"""
Wednesday = """\n8:30-10:30\t10:30-12:30\t1:30-3:30
K205\t\tF210\t\tL216
CP1850\t\tCM1400\t\tMA1900"""
Thursday = """\n8:30-10:30\t10:30-12:30\t1:30-3:30
K205\t\tK205\t\tK106
CP1850\t\tCP1461\t\tMA1900"""
Friday = """\n8:30-10:30\t11:30-12:30
K205\t\tA305
CP1850\t\tCM1400"""


if day == "Monday":
    print(Monday)
elif day == "Tuesday":
    print(Tuesday)
elif day == "Wednesday":
    print(Wednesday)
elif day == "Thursday":
    print(Thursday)
elif day == "Friday":
    print(Friday)
elif day == "monday":
    print(Monday)
elif day == "tuesday":
    print(Tuesday)
elif day == "wednesday":
    print(Wednesday)
elif day == "thursday":
    print(Thursday)
elif day == "friday":
    print(Friday)


print("\n Thanks for using scheduler checker!")

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:25:48 2023

@author: Mitchell.Harvie
"""

print("The Test Scores Program")
print("\nEnter 3 Test Scores")
print(22*"=")
test_1= float(input("Enter test Score:"))
test_2= float(input("Enter test Score:"))
test_3= float(input("Enter test Score:"))

print(22*"=")
total_score=int((test_1)+(test_2)+(test_3))
print("Total Score: \t{}".format((total_score)))
average_score=int(((test_1)+(test_2)+(test_3))/3)
print("Average Score: \t{}".format((average_score)))

if average_score >= 90 and average_score <= 100:
    avg_grade = "A"
elif average_score >= 80 and average_score <= 89 :
    avg_grade = "B"
elif average_score >= 60 and average_score <= 79 :
    avg_grade = "C"
elif average_score >= 40 and average_score <= 59 :
    avg_grade = "D"
else:
    avg_grade = "F"
    
print("Average Grade: \t{}".format((avg_grade)))
print("\nBye!")
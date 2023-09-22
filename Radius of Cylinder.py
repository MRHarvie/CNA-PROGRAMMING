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
total_score=((test_1)+(test_2)+(test_3))
print("Total Score: \t{:.0f}".format((total_score)))
average_score=(((test_1)+(test_2)+(test_3))/3)
print("Average Score: \t{:.0f}".format((average_score)))
print("\nBye!")
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 09:46:44 2023

@author: harv3
"""

def get_day(month):
    if month == 2:
        max_days = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_days = 30
    else:
        max_days = 31
    while True:
        day = int(input(f"Day (1 - {max_days}):  "))
        if day >= 1 and day <= max_days:
            return day
        else:
            print("Day Must Be Between 1 and {max_days}/  /n")

def get_month():
    while True:
        month = int(input("Month (1-12):   "))
        if month >= 1 and month <= 12:
            return month
        else:
            print("Month should be between 1-12.")
def get_year():
    while True:
            year = input("Year (1900-3000):    ")
            if year >= 1900 and year <= 3000:
                return year
            else:
                print("Please select a valid year (1900-3000). \n")

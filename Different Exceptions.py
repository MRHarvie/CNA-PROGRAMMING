# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:56:07 2023

@author: harv3
"""

file_name = input("Enter filename:")
movies = []
try:
    with open(file_name) as file_handle:
        movies = file_handle.realines()
except FileNotFoundError:
    print(f"Could not find the file named {file_name}")
except OSError:
    print("File is found. Error reading the file.")
except Exception:
    print("Unexpected Error Occured.")
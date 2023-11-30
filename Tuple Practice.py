# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 09:17:47 2023

@author: harv3
"""
import random

tuple_data = (0,5,10,15,20,25,30,35,40,45,50)
avg = (sum(tuple_data))/len(tuple_data)

sorted_data = sorted(tuple_data)
n = len(sorted_data)
if n % 2 == 0:
    median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
else:
    median = sorted_data[n // 2]
mini = min(tuple_data)
maxi = max(tuple_data)
dups = len(tuple_data) - len(set(tuple_data))

print("Tuple data:", tuple_data)
print("Median:", median)
print("Minimum:", mini)
print("Maximum:", maxi)
print("Duplicates:", dups)

rand_data = tuple(random.randint(0, 50) for i in range(10))
sorted_randdata = sorted(rand_data)
nn = len(rand_data)
if nn % 2 == 0:
    median_r = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
else:
    median_r = sorted_data[n // 2]
mini_rand = min(rand_data)
max_rand = max(rand_data)
dups_rand = len(rand_data) - len(set(rand_data))

print("Tuple:", sorted_randdata)
print("Median:", median_r)
print("Minimum:", mini_rand)
print("Maximum:", max_rand)
print("Duplicates:", dups_rand)
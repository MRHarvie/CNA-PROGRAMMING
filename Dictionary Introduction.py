# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:48:29 2023

@author: harv3
"""
#creating dict
countries = {'CA':"Canada",
             "US":"Unites States of America",
             "MX":"Mexico"}

movie = {"name":"Robocop",
         "year":1987,
         "price": 9.99}
# Retreiving obj from dict
country = countries['CA']
#updating values for an existing key
countries['CA'] = "Cameroon"
#properties
country_code = "IN"
if country_code in countries:
    country = countries[country_code]
    print(country)
else:
    print("No Such Country")
    
country = countries.get("US")
country = countries.get("IN", "Unknown")

#Delete a key value pair
del countries["CA"]
del country, country_code
#Remove a country and return the value
country = countries.pop("CA")
movie.clear() #Delete everything in dict

#Accessing Keys From List
countries.keys()
#Print keys and accosiated variables
for code in countries.keys():
    print(f"{code}\t\t{countries[code]}")

for code2 in countries:
    print(f"{code2}\t\t{countries[code2]}")
#accessing values only
countries.values()
for country in countries.values():
    print(country)
#Accessing both
countries.items()

for country_code, country in countries.items():
    print(f"{country_code}\t\t{country}")
    
#converting keys to a lit
list(countries.keys())
list(countries.values())
list(countries.items())

#converting from a list
countries = [["GB", "Britain"],
              ["NL", 'Netherlands'],
              ["DE", "Denmark"]]
dict(countries)

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:26:34 2023

@author: harv3
"""

characters = {"Arun":{"Class":"Knight", "Weapon":"Lance", "City":"Rivendale", "HP Potions" : 5, "MP Potions":10},
              "Yennefer":{"Class":"Wizard", "Weapon": "Dagger", "City":"Mount Pearl", "HP Potions": 10, "MP Potions": 2, "Unique Skill":"Dark Magic"}}

weapon = characters['Arun']['Weapon']
characters['Arun']["Unique Skill"] = ["Rolling Bash"]
characters["Arun"].pop("Unique Skill")
characters["Yennefer"].get("HP Potions")
characters["Yennefer"].get('armor', "cloth")
characters["Arun"]["Regular Skills"] = ["Bash", "Taunt", "Stab"]
characters["Arun"]["Regular Skills"][0]
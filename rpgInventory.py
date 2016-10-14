# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:59:55 2016

@author: julia_001
"""

inventory = ["sword", "armor", "shield", "Healing Potion", "5 gp"]
for x in inventory:
    print(x)

print(len(inventory))

if "sword" in inventory:
    print("Good")
    
#start = int(raw_input("Please input start"))
#end = int(raw_input("Please input end"))
#step = int(raw_input("Please input step"))
#print(inventory[start:end:step])

chest = ["gold","silver"]
inventory += chest
print(inventory)

inventory[0] = "crossbow"
print(inventory)

inventory[2:4] = ["magic dust"]
print(inventory)

del(inventory[3])
print(inventory)

del(inventory[0:2])
print(inventory)
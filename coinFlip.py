# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 11:38:25 2016

@author: julia_001
"""

import random

count = 0
count = input("How many coins would you like to flip.")

heads = 0
tails = 0

while count > 0:
    rand_num = random.randint(0, 1)
    if rand_num == 0:
        heads += 1
    elif rand_num == 1:
        tails += 1
    else:
        print("ERROR")
    
    count -= 1

print("You have flipped {} heads, and {} tails.").format(heads, tails)
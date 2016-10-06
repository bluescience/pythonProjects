# -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 14:49:01 2016

@author: julia_001
"""

import random

rand_num = random.randint(1, 1000)
count = 5
print("Try to guess a number between 1 and 1000 that is randomly generated.")
    

while (count > 0):
    print("You have ", count, "tries left: ")
    guess = input("What is the number you choose? ")
    #print(rand_num, guess)
    if guess == rand_num:
        print("YOU GUESSED THE RIGHT NUMBER! YOU WIN!")
        quit()
    elif guess < rand_num:
        print("The number you guessed is inferior to my number")
    elif guess > rand_num:
        print("The number you guessed is superior to my number")
    else:
        print("You broke it, how did you do it")
        quit()        
    count -= 1 
    
print("The correct number is ", rand_num)
    
        
        
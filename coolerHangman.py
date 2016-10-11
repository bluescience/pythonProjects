# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 12:08:05 2016

@author: julia_001
"""
import random
count = 5
words = ("DOG", "CAT", "HORSE", "PYTHON", "KNIGHT", "EMACS")
compChoice = random.choice(words)
print(compChoice)
compLen = len(compChoice) 
print("The number I am thinking of has {} letters").format(compLen)
print("You {} chances to guess a letter in the word I am thinking of. After those 5 tries, you will need to guess the entire word.").format(count)
while count > 0:
    userLetter = input("You have {} tries to guess letters left. Please input a letter.").format(count)  
    if userLetter in compChoice:
        
    count -=1

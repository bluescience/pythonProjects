# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 12:08:05 2016

@author: julia_001
"""
import random
count = 5
words = ("DOG", "CAT", "HORSE", "PYTHON", "KNIGHT", "EMACS")

compChoice = random.choice(words)
#print(compChoice)
compLen = len(compChoice) 
userLetter = ""
finalChoice = ""

print("The number I am thinking of has {} letters.").format(compLen)
print("You {} chances to guess a letter in the word I am thinking of. After those 5 tries, you will need to guess the entire word.").format(count)

while count > 0:
    print("You have {} tries to guess letters left.").format(count) 
    userLetter = raw_input("Please input a letter: ")  
    
#    print("test")    
    
    if userLetter.upper() in compChoice:
        print("The letter you have typed in IS in my word.")
    else:
        print("The letter you have typed in is NOT in my word.")
    count -=1

finalChoice = raw_input("Please input the entire word you think I have chosen for you: ")

if finalChoice.upper() == compChoice:
    print("YOU WIN!!!")
else:
    print("Sadly, you lose...")

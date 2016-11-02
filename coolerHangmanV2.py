# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:30:37 2016

@author: julia_001
"""
def hangmanStage(stage):

    if stage == 0:
        print(" _____")
        print(" |   |")
        print(" | ")
        print(" | ")
        print(" | ")
        print("_|_")

    if stage == 1:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" | ")
        print(" | ")
        print("_|_")

    if stage == 2:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |   |")
        print(" | ")
        print("_|_")

    if stage == 3:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |  /|")
        print(" | ")
        print("_|_")

    if stage == 4:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |  /|\\")
        print(" | ")
        print("_|_")

    if stage == 5:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |  /|\\")
        print(" |  /")
        print("_|_")

    if stage == 6:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |  /|\\")
        print(" |  / \\")
        print("_|_")

mainMenuChoice = "YES"

while mainMenuChoice != "NO":
    stageCount = 0
    userGuessList = []
    confirmedLetters = []
    mainMenuChoice = raw_input("Would you like to start a game of hangman? ").upper()

    if mainMenuChoice != "NO" or mainMenuChoice != "N":
        wordToGuess = raw_input("Please input the word you would like your partner to guess. Only letters are allowed to be inputed: ").upper()

        while wordToGuess.isalpha() == False:
            wordToGuess = raw_input("Please input the word you would like your partner to guess. Only letters are allowed to be inputed: ").upper()
        
        secretWord = list(wordToGuess)
        secretWordlen = len(secretWord)    
        secretCheck = secretWord        
                
        while stageCount < 6 and len(secretWord) != 0:
            hangmanStage(stageCount)                
            

            userGuess = raw_input("Please input the letter you would like to see if it is your partner's word. DO NOT INPUT REPEATS. ").upper()
           
            while userGuess in userGuessList or userGuess in confirmedLetters:
                userGuess = raw_input("Please input the letter you would like to see if it is your partner's word. DO NOT INPUT REPEATS. ").upper()
            
            if userGuess in secretWord:
                while userGuess in secretCheck:
                    confirmedLetters.append(userGuess)
                    del(secretCheck[secretCheck.index(userGuess)])
                
            else:
                userGuessList.append(userGuess)
                stageCount +=1
            '''
            secretCount = 0
            guessCount = 0        
            while range(0, len(confirmedLetters) != range(secretWord.index(confirmedLetters[0], )):
                if confirmedLetters[guessCount] != secretWord[secretCount]:
                    confirmedLetters.append(confirmedLetters[guessCount])
                    del(confirmedLetters[guessCount])
                    guessCount+=1
                else:
                    secretCount +=1
            '''
            print("The word you have discovered thus far is {}.").format(confirmedLetters)
            print("The letters you have guessed thus far are {}.").format(userGuessList)
            
            print(len(secretWord))
            print(secretWord)
            print(secretCheck)
            print(len(confirmedLetters))
                
                    
        if len(secretWord) == 0:
            print("You win!")
            
        else:
            hangmanStage(6)
            print("You lose...")
                            
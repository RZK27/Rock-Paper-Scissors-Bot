import imp
from random import randint
from os import system

wins = 0
losses = 0

userData = ""

def patternFound(pattern):

    temp = userData
    
    tally = [0, 0, 0]
    while(True):
        if temp.index(pattern) == len(temp) - len(pattern):
            break
        tally[int(temp[temp.index(pattern) + 1])] += temp.index(pattern) + len(pattern)
        temp = temp[temp.index(pattern) + 1:]


    if tally[0] >= tally[1] and tally[0] >= tally[2]:
        return 1
    if tally[1] >= tally[0] and tally[1] >= tally[2]:
        return 2
    if tally[2] >= tally[1] and tally[2] >= tally[0]:
        return 0

def searchPattern(userData, depth):

    if depth == 0:

        return randint(0, 2)
    if len(userData) - depth == userData.index(userData[-depth:]):

        return searchPattern(userData, depth - 1)
    else:
        avg = 0.0
        for i in range(depth):
            avg += patternFound(userData[-depth + i:])
        avg /= depth
        return round(avg)


while(True):

    #The bot's move is predetermined
    botMove = searchPattern(userData, len(userData))

    print ("Wins: " + str(wins))
    print ("Losses: " + str(losses))

    userInput = ""
    while (not(userInput == "rock" or userInput == "paper" or userInput == "scissors" or userInput == "exit" or userInput == "r" or userInput == "p" or userInput == "s" or userInput == "e")):
        userInput = input("Rock, Paper, Scissors, or Exit? ").lower()
    
    if userInput == "exit" or userInput == "e":
        break
    elif userInput == "rock" or userInput == "r":
        userData += "0"
    elif userInput == "paper" or userInput == "p":
        userData += "1"
    elif userInput == "scissors" or userInput == "s":
        userData += "2"


    if botMove == 0:
        botMoveText = "Rock"
    if botMove == 1:
        botMoveText = "Paper"
    if botMove == 2:
        botMoveText = "Scissors"
    
    print("The Bot played " + botMoveText)

    if int(userData[-1]) - botMove == -2:
        print("You won!")
        wins += 1
    elif int(userData[-1]) - botMove == -1:
        print("You lost!")
        losses += 1
    elif int(userData[-1]) - botMove == 0:
        print("You tied!")
    elif int(userData[-1]) - botMove == 1:
        print("You won!")
        wins += 1
    elif int(userData[-1]) - botMove == 2:
        print("You lost!")
        losses += 1



    input("Press enter to continue: ")
    system("cls")
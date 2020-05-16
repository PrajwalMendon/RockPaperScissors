# create a rock paper scissors game

import random

def computer_choice():
    computerOption = ['rock', 'paper', 'scissors']
    return random.choice(computerOption)

def rockpaperscissors():
    playerChoice = str(input('Please select either rock, paper, or scissors: '))
    computerChoice = computer_choice()
    if playerChoice == 'rock':
        if computerChoice == 'rock':
            print(computerChoice)
            print("The game is a tie.")
        elif computerChoice == 'scissors':
            print(computerChoice)
            print("You win!")
        else:
            print(computerChoice)
            print("You lose.")
    elif playerChoice == 'scissors':
        if computerChoice == 'rock':
            print(computerChoice)
            print("You lose.")
        elif computerChoice == 'scissors':
            print(computerChoice)
            print("The game is a tie.")
        else:
            print(computerChoice)
            print("You win!")
    elif playerChoice == 'paper':
        if computerChoice == 'rock':
            print(computerChoice)
            print("You win!")
        elif computerChoice == 'scissors':
            print(computerChoice)
            print('You lose.')
        else:
            print(computerChoice)
            print("The game is a tie.")
    else:
        print("Please only choose either rock, paper, or scissors.")

rockpaperscissors()
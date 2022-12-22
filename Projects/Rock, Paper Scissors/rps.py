from random import randint
import sys

game_on = True
wins = 0
loss = 0
ties = 0

#instructions
print("ROCK PAPER SCISSORS")
print("\nWelcome to Rock, Paper, Scissors. The aim of the game is to beat the computer")
print("\nThe Rules")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")
print("\nEnter R for Rock. Enter P for Paper. Enter S for Scissors")
print("Enter Q to quit\n")

#player input
while game_on:
    print("Wins", wins,"\nTies",ties,"\nLoss",loss)
    choice = input("\nRock! Paper! Scissors!:\t")
    if choice.lower() == "r":
        print("ROCK versus...")
    elif choice.lower() == "p":
        print("PAPER versus...")
    elif choice.lower() == "s":
        print("SCISSORS versus...")
    elif choice.lower() == "q":
        sys.exit()

#computer input
    random_number = randint(1,3)
    if random_number == 1:
        computer_move = "p"
        print("PAPER")
    elif random_number == 2:
        computer_move = "r"
        print("ROCK")
    elif random_number == 3:
        computer_move = "s"
        print("SCISSORS")

#player - computer comparison

    if choice == "r" and computer_move == "p":
        print("\nROCK WINS")
        wins += 1
    elif choice == "r" and computer_move == "s":
        print("\nSCISSORS WINS")
        loss += 1
    elif choice == "r" and computer_move == "r":
        print("\nDRAW")
        ties += 1
    elif choice == "p" and computer_move == "r":
        print("\nPAPER WINS")
        wins += 1
    elif choice == "p" and computer_move == "s":
        print("\nSCISSORS WINS")
        loss += 1
    elif choice == "p" and computer_move == "p":
        print("DRAW")
        ties += 1
    elif choice == "s" and computer_move == "p":
        print("\nSCISSORS WINS")
        wins += 1
    elif choice == "s" and computer_move == "s":
        print("DRAW")
        ties += 1
    elif choice == "s" and computer_move == "r":
        print("\nROCK WINS")
        loss += 1
    




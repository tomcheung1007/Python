from random import randint
import sys
import time

def instructions():
    # instructions
    print("ROCK PAPER SCISSORS")
    print("\nWelcome to Rock, Paper, Scissors. The aim of the game is to beat the computer")
    time.sleep(4)
    print("\nThe Rules")
    time.sleep(1)
    print("Rock beats Scissors")
    time.sleep(2)
    print("Scissors beats Paper")
    time.sleep(2)
    print("Paper beats Rock")
    time.sleep(3)
    print("\nHow to play: Enter R for Rock. Enter P for Paper. Enter S for Scissors")
    print("Enter Q anytime to quit\n")


def game():
    game_on = True
    wins = 0
    loss = 0
    ties = 0

    # player input
    while game_on:
        print("Wins", wins, "\nTies", ties, "\nLoss", loss)
        time.sleep(2)
        choice = input("\nRock! Paper! Scissors!:\t")
        if choice.lower() == "r":
            time.sleep(0.5)
            print("ROCK versus...")
        elif choice.lower() == "p":
            time.sleep(0.5)
            print("PAPER versus...")
        elif choice.lower() == "s":
            time.sleep(0.5)
            print("SCISSORS versus...")
        elif choice.lower() == "q":
            time.sleep(0.5)
            print("\nGame ended!!")
            time.sleep(0.5)
            print("Wins", wins, "\nTies", ties, "\nLoss", loss)
            sys.exit()

        # computer input
        random_number = randint(1, 3)
        if random_number == 1:
            computer_move = "p"
            time.sleep(0.5)
            print("PAPER")
        elif random_number == 2:
            computer_move = "r"
            time.sleep(0.5)
            print("ROCK")
        elif random_number == 3:
            computer_move = "s"
            time.sleep(0.5)
            print("SCISSORS")

        # result
        if choice == "r" and computer_move == "p":
            time.sleep(0.5)
            print("\nROCK WINS")
            wins += 1
        elif choice == "r" and computer_move == "s":
            time.sleep(0.5)
            print("\nSCISSORS WINS")
            loss += 1
        elif choice == "r" and computer_move == "r":
            time.sleep(0.5)
            print("\nDRAW")
            ties += 1
        elif choice == "p" and computer_move == "r":
            time.sleep(0.5)
            print("\nPAPER WINS")
            wins += 1
        elif choice == "p" and computer_move == "s":
            time.sleep(0.5)
            print("\nSCISSORS WINS")
            loss += 1
        elif choice == "p" and computer_move == "p":
            time.sleep(0.5)
            print("\nDRAW")
            ties += 1
        elif choice == "s" and computer_move == "p":
            time.sleep(0.5)
            print("\nSCISSORS WINS")
            wins += 1
        elif choice == "s" and computer_move == "s":
            time.sleep(0.5)
            print("\nDRAW")
            ties += 1
        elif choice == "s" and computer_move == "r":
            time.sleep(0.5)
            print("\nROCK WINS")
            loss += 1


# LOGIC
def play_rps():
    # instructions()
    while True:
        play = " "
        game_on = False
        while play not in ["Y", "Q"]:
            time.sleep(2)
            play = input("Are you ready to play? Enter Y (yes) or Q (quit):\t").upper()

            if play == "Y":
                game_on = True
            elif play == "Q":
                game_on = False
            else:
                print("Error. Please enter Y to play or Q to quit")

            while game_on:
                game()

        print("ASD")


print(play_rps())



# NUMBER GUESSING GAME


from random import randint


def set_up_number_guessing_game():
    num = randint(1,100)
    result = [num]

    while True:
        difficulty = input("Enter difficulty level:\t Easy (E) or Hard (H):")
        if difficulty[0].upper() not in ["E", "H"]:
            print("\n**ERROR**\tEnter E for easy difficulty or H for hard difficulty")
        else:
            result.append(difficulty[0].upper())
            break

    return result  # [num, difficulty]


def number_guess(arr):
    num = arr[0]
    difficulty = arr[1]
    lives = 0
    if difficulty == "E":
        lives = 10
    elif difficulty == "H":
        lives = 5

    print(f"Number {num} / Difficulty {difficulty} / Lives {lives}")


    while lives != 0:
        try:
            guess = int(input("\nEnter number:\t"))
        except ValueError:
            print("\n**ERROR**Digit must be entered for guess")
        else:
            if guess < num:
                lives -= 1
                print(f"\nTOO LOW:\t{lives} lives remaining")
            elif guess > num:
                lives -= 1
                print(f"\nTOO HIGH:\t{lives} lives remaining")
            elif guess == num:
                return f"\nSUCCESS!\tNumber was {num}"
        if lives == 0:
            return f"\nGAME OVER!\tNumber was {num}"




print(number_guess(set_up_number_guessing_game()))


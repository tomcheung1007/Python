
def select_word():
    """return user input for select word to play hangman"""

    # validate user input - no numbers or special characters
    while True:
        chosen_word = input("Please enter word for hangman:\t").lower()
        if not chosen_word.isalpha():
            print("**ERROR** No numbers or special characters allowed. ")
        else:
            break

    chosen_word = list(chosen_word)

    print('\n'*1000)  # to hide visible word during user input

    hidden_word = ['_' for _ in chosen_word]  #hide letters of chosen word

    return list(hidden_word), chosen_word


def play_hangman(arr):
    """game in action"""
    lives = 11
    blanks = arr[0]
    word = arr[1]
    letters = set()

    while True:
        letter_guess = input(f"\n\nEnter letter: {blanks}\t").lower()
        # VALIDATE USER INPUT
        # if too many letters
        if len(letter_guess) != 1:
            print("\n**ERROR** Enter one letter only")
            continue
        # if letter already guessed
        if letter_guess in letters:
            print(f"Guess again. You already selected '{letter_guess}'")
            print(f"\nLetters:\t{list(sorted(letters))}")
            continue

        letters.add(letter_guess)

        # ACCEPTED USER INPUT
        # correct letter >>> replace blank with letter
        if letter_guess in word:
            for index, letter in enumerate(word):
                if letter == letter_guess:
                    blanks[index] = letter_guess
            print(f"\nCorrect: {blanks}")

        # incorrect letter >>> lives - 1
        else:
            lives -= 1
            print(f"Incorrect: {lives} remaining")
            print(f"\nLetters:\t{list(sorted(letters))}")

        # GAME RESULT
        # Success
        if "_" not in blanks:
            print(f"\nSuccess! Word was '{''.join(blanks)}'. You avoided hangman")
            break
        # Fail
        if lives == 0:
            print(f"\nGame over! Word was '{''.join(blanks)}'")
            break



play_hangman(select_word())





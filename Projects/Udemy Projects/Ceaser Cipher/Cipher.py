def valid_input():
    """validate input to return string and number in list"""

    arr = []  # to store user input
    upper_index = [] # to store index position if upper case present
    key_range = [int(_) for _ in range(1, 27)]

    # string input - ACCEPTING LETTERS, NUMBERS and SPECIAL CHARACTERS
    word = input("\nEnter text:\t")
    arr.append(word)

    # store upper case
    for i, _ in enumerate(word):
        if _.isupper():
            upper_index.append(i)

    # validate num input
    while True:
        try:
            num = int(input("Enter number for encryption key:\t"))
        except ValueError:
            print("\nERROR.\t Number must be integer")
        else:
            if num not in key_range:
                print("\nERROR.\t Number must be in range 1-26")
            else:
                print(f"\nAccepted number:\t{num}\n")
                arr.append(int(num))
                break

    return [arr, upper_index]


def encrypt(arr):
    """return encrypted message"""
    alphabet = {chr(i): i - 96 for i in range(ord("a"), ord("z") + 1)}  # dict alphabet:number
    word = arr[0][0]
    num = arr[0][1]
    upper_index = arr[1]  # stores index position if character is uppercase

    # convert character to corresponding ord
    character_ord = []
    for w in word.split(" "):
        for _ in w.lower():
            if _.isalpha():
                character_ord.append(alphabet[_])
            else:
                character_ord.append(_)
        character_ord.append("SPACE")

    # implement encryption key
    key_encryption = [_ + num if type(_) == int else " " if _ == "SPACE" else _ for _ in character_ord]

    # loop round to beginning of alphabet if ord > 26
    verify_arr = [_-26 if type(_) == int and _ > 26 else _ for _ in key_encryption]

    # convert num to corresponding character
    cipher = [chr(_+96) if type(_) == int else _ for _ in verify_arr]

    # return upper case character if present
    if upper_index:
        for _ in upper_index:
            cipher[_] = cipher[_].upper()

    return f"\nSuccess. Text encrypted:\n\tOriginal text:\t{(arr[0][0])}\n\tEncrypted:\t{''.join(cipher).rstrip()}"


def decrypt(arr):
    """return encrypted message"""
    alphabet = {chr(i): i - 96 for i in range(ord("a"), ord("z") + 1)}  # dict alphabet:number
    word = arr[0][0]
    num = arr[0][1]
    upper_index = arr[1]  # stores index position if character is uppercase

    # convert character to corresponding ord
    character_ord = []
    for w in word.split(" "):
        for _ in w.lower():
            if _.isalpha():
                character_ord.append(alphabet[_])
            else:
                character_ord.append(_)
        character_ord.append("SPACE")

    # implement encryption key
    key_encryption = [_ - num if type(_) == int else " " if _ == "SPACE" else _ for _ in character_ord]

    # loop round to beginning of alphabet if ord > 26
    verify_arr = [_ - 26 if type(_) == int and _ > 26 else _ for _ in key_encryption]

    # convert num to corresponding character
    cipher = [chr(_+96) if type(_) == int else _ for _ in verify_arr]

    # return upper case character if present
    if upper_index:
        for _ in upper_index:
            cipher[_] = cipher[_].upper()

    return f"\nSuccess. Text encrypted:\n\tOriginal text:\t{(arr[0][0])}\n\tEncrypted:\t{''.join(cipher).rstrip()}"

def ceasar_cipher():
    while True:
        encrypt_or_decrypt = input("\nWould you like to encrypt or decrypt message. Enter E (encrypt) or D (decrypt):\t")
        if encrypt_or_decrypt[0].upper() not in ["E", "D"]:
            print("\nERROR. Enter E to encrypt or D to decrypt")
        elif encrypt_or_decrypt[0].upper() == "E":
            print(encrypt(valid_input()))
        elif encrypt_or_decrypt[0].upper() == "D":
            print(decrypt(valid_input()))

        play_again = input("\nWould you like to encrypt/decrypt another message? Enter Y (yes) or N (no):\t")
        if play_again[0].upper() not in ["Y", "N"]:
            print("\nERROR. Enter Y to continue or N to quit")
        elif play_again[0].upper() == "Y":
            continue
        elif play_again[0].upper() == "N":
            return "Thank you. Goodbye"


print(ceasar_cipher())

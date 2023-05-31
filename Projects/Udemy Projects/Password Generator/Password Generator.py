import random
import string

def pw_generator_intro():
    """introduction for valid password"""
    return("""PASSWORD GENERATOR
    
    This program will generate a password for you. 
    To create your password, answer the following questions\n""")

def valid_pw_length():  # returns password length
    """validate input for length of password"""
    while True:
        try:
            total_length_pw = int(input("\nEnter number for total length of password:\t"))
        except ValueError:
            print("\n**ERROR**\tEnter number\n")
        else:
            return total_length_pw


def valid_pw_character():
    """validate input for type of characters in password and returns dict"""
    character_type = {"upper":False, "lower":False, "number":False, "special":False}

    # UPPER CASE
    while True:
        upper = input("Upper case characters in password?\tEnter Y or N:\t")
        if upper[0].lower() not in ["y", "n"]:
            print("\n**ERROR**\tPlease enter Y or N\n")
        elif upper[0].lower() == "y":
            character_type["upper"] = True
            break
        else:
            character_type["upper"] = False
            break

    # LOWER CASE
    while True:
        upper = input("Lower case characters in password?\tEnter Y or N:\t")
        if upper[0].lower() not in ["y", "n"]:
            print("\n**ERROR**\tPlease enter Y or N\n")
        elif upper[0].lower() == "y":
            character_type["lower"] = True
            break
        else:
            character_type["lower"] = False
            break

    # NUMBERS
    while True:
        upper = input("Number characters in password?\tEnter Y or N:\t")
        if upper[0].lower() not in ["y", "n"]:
            print("\n**ERROR**\tPlease enter Y or N\n")
        elif upper[0].lower() == "y":
            character_type["number"] = True
            break
        else:
            character_type["number"] = False
            break

    # SPECIAL CHARACTERS
    while True:
        upper = input("Special characters in password?\tEnter Y or N:\t")
        if upper[0].lower() not in ["y", "n"]:
            print("\n**ERROR**\tPlease enter Y or N\n")
        elif upper[0].lower() == "y":
            character_type["special"] = True
            break
        else:
            character_type["special"] = False
            break

    return character_type


def quant_character(character_dict, pw_length):
    """takes dict of character types and takes quantity of each character type"""
    x = {}  # to store character type : quantity

    # loop to get quantity of each selected character type
    for k, v in character_dict.items():
        if v:
            while True:
                quant = int(input(f"\nHow many {k} characters?\t"))
                if quant > pw_length:
                    print(f"\n**ERROR**\tnumber must be less than available characters {pw_length}\n")
                else:
                    x.setdefault(k, quant)
                    pw_length -= quant
                    print(f"\nCharacters left to fill: {pw_length}")
                    break

    return x


def create_pw(character_dict):
    """return random characters based on character type and quantity"""
    result = []

    # loop to get characters of each selected type and quantity
    for k, v in character_dict.items():
        if k == "upper":
            random_upper = random.choices(string.ascii_uppercase, k=v)
            for _ in random_upper:
                result.append(_)
        elif k == "lower":
            random_lower = random.choices(string.ascii_lowercase, k=v)
            for _ in random_lower:
                result.append(_)
        elif k == "number":
            random_number = random.choices(string.digits, k=v)
            for _ in random_number:
                result.append(_)
        elif k == "special":
            random_special = random.choices(string.punctuation, k=v)
            for _ in random_special:
                result.append(_)

    random.shuffle(result)

    return f"\nPASSWORD CREATED:\t{''.join(result)}"


def replay():
    """option to generate password or to quit"""
    marker = " "
    while marker not in ["Y", "N"]:
        marker = input(
            'Do you want to play again? Enter Y (yes) or N (no):\t').lower()
        if marker == "y":
            return True
        elif marker == "n":
            print("Goodbye")
            return False
        else:
            print("**ERROR**\tEnter Y to play again or N to quit:\t")


def password_generator():
    play_again = True
    while play_again:
        print(pw_generator_intro())
        print(create_pw(quant_character(valid_pw_character(),valid_pw_length())))


        if not replay():  # if return False >>> break
            break


print(password_generator())


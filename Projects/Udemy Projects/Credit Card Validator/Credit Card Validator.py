# Card validator takes user input for card number and uses Luhn algorithm to check if card number is valid
def card_info():
    """return valid input. len == 16 and all digits. retuurn for validate_card()"""
    while True:
        card_number = input("Please enter 16 digit card number:\t")
        if len(card_number) != 16:
            print("*ERROR* - Card number must be 16 digits long")
        else:
            if card_number.isdigit() is False:
                print("*ERROR* - Card number must be numbers only")
            else:
                print("Thank you - Card number accepted ")
                return card_number


def validate_card(card):
    """Luhn algorithm to confirm card number is valid"""

    final = [int(_) for i, _ in enumerate(card) if i % 2 == 1]  # elements that are untouched. Only used at end of
    # algorithm

    # Luhn algorithm
# 1. Starting from index 0, double every other digit.
    double_card_num = [int(_) * 2 for i, _ in enumerate(card) if i % 2 == 0]
# 2. If element is two-digits, replace element with sum of two digits together. Add to final
    two_digit = [str(_) for _ in double_card_num if len(str(_)) == 2]  # list of numbers two digit long
    for _ in two_digit:
        total = int(_[0]) + int(_[1])
        final.append(total)
# 3. Remaining single digit elements added to final
    remaining = [str(_) for _ in double_card_num if len(str(_)) == 1]
    for _ in remaining:
        final.append(int(_))
# 4. if sum(final) mod 10 equal to 0: Valid according to Luhn formula
    total_sum = sum(final)
    if total_sum % 10 == 0:
        return "Valid card"
    else:
        return "Invalid card"

print(validate_card(card_info()))

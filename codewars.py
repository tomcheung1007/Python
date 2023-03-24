# Recent practice via codewars.

def calculate_string(st):
    """clean dirty string and return sum"""
    # st = sldfj9v234.12fvi3-493mvfo3
    clean = ""

    # identify numbers, decimal point and operator
    for i in st:
        if i.isdigit() or i == ".":
            clean += i
        elif i in ["+", "-", "*", "/"]:
            clean += i
            operator = i

    # split string to two individual numbers in list
    clean = clean.split(operator)

    # calculation based on operator
    if operator == "+":
        return str(round(float(clean[0]) + float(clean[1])))
    elif operator == "-":
        return str(round(float(clean[0]) - float(clean[1])))
    elif operator == "*":
        return str(round(float(clean[0]) * float(clean[1])))
    else:
        return str(round(float(clean[0]) / float(clean[1])))


# print(calculate_string("sldfj9v234.12fvi3-493mvfo3"))
def find_even_index(arr):
    """return index position where left and right are equal. Else return -1"""
    # [1, 2, 3, 4, 3, 2, 1]
    for _ in range(len(arr)):
        if sum(arr[0:_]) == sum(arr[_ + 1:]):
            return _
    return -1  # return -1 indented here to allow for loop to complete its course


# print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
def sort_array(source_array):
    """Sort odd integers whilst maintaining order of even integers"""
    # [2, 7, 1, 4, 8, 10, 5]
    odds = []
    answer = []  # list comp [_ if _ % 2 == 0 else "X" for _ in test]
    # replace odds with X to replace later [2, 'X', 'X', 4, 8, 10, 'X']
    for _ in source_array:
        if _ % 2 != 0:
            odds.append(_)
            answer.append("X")
        else:
            answer.append(_)

    odds.sort()  # sort odds ascending to replace X in ascending order

    for i in odds:
        # index() returns the position occurrence of the specified value.
        x = answer.index("X")  # index positions 1, 2, 6
        answer[x] = i
    return answer


# print(sort_array([2, 7, 1, 4, 8, 10, 5]))
def find_missing_letter(chars):
    """find missing letter in array and return its value"""
    alphabet = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7',
                'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13',
                'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19',
                't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
    result = [alphabet[_.lower()] for _ in chars]  # convert letter to its corresponding numbers

    # for loop to find missing number
    for _ in range(len(result)):
        if int(result[_]) - int(result[_ - 1]) != 1:
            missing_number = (int(result[_]) - 1)

    # for loop to return key of missing number
    for k, v in alphabet.items():
        if v == str(missing_number):
            return k


# print(find_missing_letter(["B", "c", "d", "e", "g"]))
def longest_consec(strarr, k):
    """return longest consecutive string in array"""
    result = []
    top_word = ""  # to be returned as output

    # if strarr == []
    if not strarr:
        return ""

    if k <= 0 or k > len(strarr):
        return ""

    # for loop to concatenate string for later comparisons
    for _ in range(len(strarr) - (k - 1)):  # k-1 for concatenation
        word_combo = "".join(strarr[_:_ + k])
        result.append(word_combo)

    # comparison for longest length string
    print(result)
    for _ in result:
        if len(_) > len(top_word):
            top_word = _

    return top_word


# print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3))
def wave(people):
    """return variation string with uppercase character moving left to right"""
    result = []
    chars = list(people)  # convert string to list for mutability
    print(chars)

    # for loop: each iteration, make copy of list, convert letter to uppercase, append to result
    for i, _ in enumerate(chars):
        if _.isalpha():
            copy = chars[:]  # create copy of list
            copy[i] = copy[i].upper()  # convert iterated letter to uppercase
            result.append("".join(copy))
    return result


# print(wave(" gap "))
def expanded_form(num):
    """Return integer in expanded form (string) e.g. 22 >>> 20 + 2"""
    num_list = []
    final = ""
    x = len(str(num)) - 1  # identify length of digits for later iteration

    if len(str(num)) == 1:
        return str(num)

    # while loop to iterate through digits
    while x > 0:
        for _ in str(num):  # str(num) for accessibility
            if _ != 0:
                num_list.append(f"{_}{'0' * x}")  # x is essentially the amount of zeros to be added
                x -= 1

    # for loop to pick out numbers in expanded form
    for _ in num_list:
        if int(_) > 0:
            final += f"{_} + "

    return final[:-3]


# print(expanded_form(4030))
def camel_split(s):
    """break up camel casing with space between words"""
    result = []

    for _ in range(len(s)):
        if not s[_].isupper():  # if lowercase, add characters to result
            result.append(s[_])
        elif s[_].isupper():  # if uppercase, add space and then following characters to result
            result.append(" ")
            result.append(s[_])

    return "".join(result)  # convert list to string


# print(camel_split("breakCamelCase"))
def two_sum(numbers, target):
    """return index position for integers that add to target"""
    result = []
    for _ in range(len(numbers)):
        if numbers[_] + numbers[_ - 1] == target:
            result.append(_)
            result.append(_ - 1)
            break
    for _ in result:
        if _ == -1:
            result[_] = 2
    return result


# print(two_sum([1, 2, 3, 2], 5))
import math
def gps(s, x):
    """calculate maximum average speed"""
    # hourly speed formula = (3600 * delta_distance) / s

    # duration of each section
    sections = [x[_ + 1] - x[_] for _ in range(len(x) - 1)]  # [0.19, 0.31, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]

    # speed calculation for each section
    speed = [(3600 * _) / s for _ in sections]  # [45.6, 74.4, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0]
    if len(x) <= 1:
        return 0

    return math.floor(max(speed))


# print(gps(15, [0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]))
def alphabet_symmetry(arr):
    """given an array of words, return array of integers for the total amount of letters that occupy their position
    in the alphabet for each word"""

    # Dictionary comprehension for alphabet:integer
    my_dict = {chr(i): i - 96 for i in range(ord("a"), ord("z") + 1)}
    # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
    # 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
    # 'z': 26}

    result = []
    for _ in arr:
        total = 0
        for i, c in enumerate(_):
            i += 1
            if i == my_dict[c.lower()]:
                total += 1
        result.append(total)

    return result


# print(alphabet_symmetry(["encode", "abc", "xyzD", "ABmD"]))
def encrypt_this(text):
    """encrypt text: 1.Replace first letter with its ordered code. 2.swap 2nd character with last character"""
    encrypted = ""
    text = text.split()
    for word in text:
        for i, c in enumerate(word):
            # replace first letter with ord equivalent
            if i == 0:
                encrypted += " "  # maintain space between words
                encrypted += str(ord(c))

            # swap 2nd character with last character
            elif i == 1:
                encrypted += word[-1]
            elif i == len(word) - 1:
                encrypted += word[1]

            else:
                encrypted += c

    return encrypted.lstrip().rstrip()


# print(encrypt_this("hello world"))
def decipher_this(text):
    """Decipher text: 1.Replace first letter with its character code. 2.Swap 2nd character with last character"""
    decipher = ""
    num = ""  # to store numbers
    text = text.split()

    for word in text:
        # replace number with chr equivalent
        for _ in word:
            if _.isdigit():
                num += _
                word = word.replace(_, "")  # remove redundant digits. Makes it's easier to iterate later
        decipher += " "  # maintain space between words
        decipher += chr(int(num))
        num = ""  # reset to capture numbers for next iterated word

        # swap 2nd character with last character
        for i, _ in enumerate(word):
            if _.isdigit():
                pass
            elif i == 0:
                decipher += word[-1]
            elif i == len(word)-1:
                decipher += word[0]
            else:
                decipher += _

    return decipher.lstrip().rstrip()


# print(decipher_this("72olle 103doo 100ya"))
def clean_string(s):
    """program that detects # and treats it as a backspace"""
    result = []
    # for loop to iterate through string. When # is detected, check if result contains info
    for c in s:
        if c == '#':
            if result:
                result.pop()  # acts as backspace
        else:
            result.append(c)
    return ''.join(result)


# print(clean_string('1A#?#EMC5[(3@C'))
from collections import Counter
def highest_rank(arr):
    if arr:
        c = Counter(arr)
        m = max(c.values())
        return max(k for k, v in c.items() if v == m)


#print(highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10] ))
def cube_odd(arr):
    if any(type(_) is not int for _ in arr):
        return None
    return sum(x ** 3 for x in arr if x % 2 != 0)






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

def solution(s):
    """break up camel casing with space between words"""
    result = []

    for _ in range(len(s)):
        if not s[_].isupper():  # if lowercase, add characters to result
            result.append(s[_])
        elif s[_].isupper():  # if uppercase, add space and then following characters to result
            result.append(" ")
            result.append(s[_])

    return "".join(result)  # convert list to string



print(solution("breakCamelCase"))

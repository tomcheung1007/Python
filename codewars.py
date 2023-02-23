def calculate_string(st):
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
    print(clean)

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
    # [1, 2, 3, 4, 3, 2, 1]
    for _ in range(len(arr)):
        print(sum(arr[0:_]), sum(arr[_ + 1:]))
        if sum(arr[0:_]) == sum(arr[_ + 1:]):
            return _
    return -1  # return -1 indented her to allow for loop to complete its course


# print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
def sort_array(source_array):
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
    upper = False
    alphabet = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7',
                'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13',
                'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19',
                't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
    result = [alphabet[_.lower()] for _ in chars]  # convert letter to its corresponding numbers
    for _ in chars:
        if _.isupper():
            upper = True
    print(result)
    # for loop to find missing number
    for _ in range(len(result)):
        if int(result[_]) - int(result[_ - 1]) != 1:
            missing_number = (int(result[_]) - 1)

    for k, v in alphabet.items():
        if v == str(missing_number):
            if upper:
                return k.upper()
            else:
                return k


# print(find_missing_letter(["b", "c", "d", "e", "g"]))



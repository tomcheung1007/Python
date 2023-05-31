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
def spacify(string):
    """add space between every character"""
    result = ""
    # for loop to add space
    for _ in string:
        result += _
        result += " "
    # to account for all cases, space may or may not be required at end
    for _ in result[-2:]:  # last two characters
        if _[0].isalnum():
            return result.rstrip()
        else:
            return result[:-1]
    return result


# print(spacify("hello world"))
def men_from_boys(arr):
    """return array where even numbers ascend and then odd numbers descend"""
    result = []

    even = set([_ for _ in arr if _ % 2 == 0])
    odd = set([_ for _ in arr if _ % 2 == 1])

    even = sorted(even)  # ascending order
    odd = sorted(odd, reverse=True)  # descending order

    # add ordered arrays to result
    for _ in even:
        result.append(_)
    for _ in odd:
        result.append(_)

    return result


# print(men_from_boys([2,15,17,15,2,10,10,17,1,1]))
def remove_rotten(bag_of_fruits):
    """remove word "rotten" and return updated array all lowercase"""
    try:
        result = [_[6:].lower() if _[:6] == "rotten" else _.lower() for _ in bag_of_fruits]
    except TypeError:
        return []

    return result


#print(remove_rotten(["rottenApple","rottenBanana","rottenApple","rottenPineapple","rottenKiwi"]))
def protein_synthesis(dna):
    """Convert DNA to its  protein"""
    # amino acid dictionary - amino acid: RNA
    amino_acid = {"Ala": ["GCU", "GCC", "GCA", "GCG"], "Leu": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
                  "Arg": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"], "Lys": ["AAA", "AAG"], "Asn": ["AAU", "AAC"],
                  "Met": ["AUG"], "Asp": ["GAU", "GAC"], "Phe": ["UUU", "UUC"], "Cys": ["UGU", "UGC"], "Pro":
                      ["CCU", "CCC", "CCA", "CCG"], "Gln": ["CAA", "CAG"],
                  "Ser": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
                  "Glu": ["GAA", "GAG"], "Thr": ["ACU", "ACC", "ACA", "ACG"], "Gly": ["GGU", "GGC", "GGA", "GGG"],
                  "Trp":["UGG"], "His": ["CAU", "CAC"], "Tyr": ["UAU", "UAC"], "Ile": ["AUU", "AUC", "AUA"], "Val":
                      ["GUU", "GUC", "GUA", "GUG"], "Stop": ["UAG", "UGA", "UAA"]}
    codon = []
    protein = ""  # to return as output
    #translate DNA to RNA
    dna_to_rna = dna.maketrans("TAGC", "AUCG")
    rna = dna.translate(dna_to_rna)

    # split RNA into triplets
    for _ in range(0, len(rna), 3):
        codon.append(rna[_:_ + 3])

    for c in codon:
        for k, v in amino_acid.items():
            if c in v:
                protein += f"{k} "

    return " ".join(codon), protein.rstrip()


# print(protein_synthesis("GGCCGCCCATCAGCTTAAGGTAGAGAGCCACAATTGTTTATGAGAGTGATGGGGTCCGGTGGAGGTCCCC"))
def solve(s):
    alphabet = {chr(i): i - 96 for i in range(ord("a"), ord("z") + 1)}
    c = ""
    vowels = ["a", "e", "i", "o", "u"]

    score = 0
    # for loop to remove vowels from string
    for _ in s:
        if _ not in vowels:
            c += _
        elif _ in vowels:
            c += " "

    c_list = c.split(" ")

    for x in c_list:
        total = 0  # to compare scores
        for _ in x:
            if _ in alphabet:
                total += alphabet[_]
            if total > score:
                score = total

    return score


# print(solve("zodiac"))
import re

def sum_of_integers_in_string(s):
    return sum(int(x) for x in re.findall(r"\d+", s))


# print(sum_of_integers_in_string("qeoihf238ryrejkfhhbv453yt493eifhurbvdfhvei123udchwiefh209"))
def count_bits(n):
    bit = []
    num_list = []
    x = 2

    while n > 0:
        y = n / x
        num_list.append(y)
        if y % 1 != 0:
            y = int(y)
            bit.append(1)
        elif y % 1 == 0:
            bit.append(0)
        n = y
    return bit.count(1)


#print(count_bits(1234))
def valid_braces(s):
    """return bool if order of braces are valid"""
    accepted = ["{}", "[]", "()"]  # for comparison of valid braces
    confirmation = len(s) // 2  # minimum valid braces for True boolean

    # valid braces are either immediately next to or on the equal opposite end of character
    # use l and r as placeholders for iteration
    l = 0  # next to character
    r = -1 # opposite end

    # for loop to create and store each brace combo
    result = [] # to store brace combo
    for _ in range(len(s) // confirmation):
        x, y = f"{s[l]+s[l+1]}", f"{s[l]+s[r]}"
        result.append(x)
        result.append(y)
        l += 1
        r -= 1

    # for loop to check if brace combos matches accepted list
    check = []  # Append "YES" to confirm valid brace
    for _ in result:
        if _ in accepted:
            check.append("YES")

    return True if len(check) >= confirmation else False


#print(valid_braces("({}}{[]})"))
def valid_braces_v_2(string):
    while '()' in string or '[]' in string or '{}' in string:
        print(string)
        string = string.replace('{}', '')
        print(string)
        string = string.replace('()', '')
        print(string)
        string = string.replace('[]', '')
        print(string)
    return not string


#print(valid_braces_v_2(test))
def in_array(array1, array2):
    """return array in lexicographical order if string in array1 and array2 share same first letter"""
    result = []  # to store results

    # for loop to check if first letter of word in array1 matches in array2
    for a1_word in array1:
        for a2_word in array2:
            if a1_word[0] == a2_word[0]:
                result.append(a1_word)

    result = dict.fromkeys(result)  # dict.fromkeys - way to remove duplicate
    return sorted(list(dict.fromkeys(result)))  # return back to list and sorted


# print(in_array(["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))
def alternate_case(s):
    """return updated string where upper case becomes lower case and vice versa """
    return "".join([_.lower() if _.isupper() else _.upper() for _ in s])


#print(alternate_case("cODEwARS"))
def tower_builder(n_floors):
    """return tower made of * based on n floors"""
    x = (2*n_floors)-1  # total number of * on bottom floor
    star = "*"
    space = " "

    # star will always start with 1 and increase by 2 until it reaches x i.e. 1, 3, 5, 7
    # space will do reverse. start with x-1 and decrease by 2 i.e. 6, 4, 2
    result = [f"{space * ((x-_)//2)}{star*_}{space * ((x-_)//2)}" for _ in range(1, x+1, 2)]

    return result


# print(tower_builder(4))
def rot13(message):
    """return ciphered string where a-z characters are replaced by the character 13 steps ahead of original character """
    print(f"MESSAGE : {message}")
    result = []
    upper = [_ for _ in range(len(message)) if message[_].isupper()]  # store index position of any upper case character

    # characters that are upper case must maintain their upper case when returned
    # special characters and numbers remain unchanged

    # for loop to store chr() of each character as lower case
    for _ in message:
        if _.isalpha():
            if _.isupper():
                upper_c = ord(_)-64
                if upper_c <= 13:
                    upper_c += 13
                else:
                    upper_c -= 13
                result.append(chr(upper_c+96))

            else:
                c = ord(_) - 96
                if c <= 13:
                    c += 13
                else:
                    c -= 13
                result.append(chr(c+96))

        # anything other than alpha i.e. num and special character >> append to result
        elif _ == " ":
            result.append(" ")
        else:
            result.append(_)

    # bring back upper case character to result
    if upper:
        for _ in upper:
            c = result[_]
            c = ord(c)-32
            result[_] = chr(c)

    return f"CIPHERED : {''.join(result)}"


# print(rot13("Test"))
def dirReduc(arr):
    opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
    print(arr)
    new_plan = []

    for d in arr:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan


# print(dirReduc(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']))
def wave(people):
    """simulate mexican wave with upper case character through string"""
    result = []  # to store iterations of mexican wave string
    people = list(people)  # working with list because mutable

    # for each iteration, make a copy and replace character with upper
    for i, _ in enumerate(people):
        if _ == " ":
            continue
        copy = people[:]
        copy[i] = copy[i].upper()
        result.append("".join(copy))

    return result


# print(wave("two words"))


def roman_numerals_encoder(n):
    """translate number to roman numerals"""
    roman_numerals = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L",
                      40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
    result = ""  # to return as output

    # for each key, while n is greater than iterated key, append value to roman numerals, deduct from n
    for _ in roman_numerals.keys():
        while n >= _:
            print(_)
            result += roman_numerals[_]
            n -= _

    return result


# print(roman_numerals_encoder(269))


import re
def domain_name(url):
    result = [_ for _ in url.split(".")]

    mo = re.search(r"www", url)
    mo_2 = re.search(f"//", url)

    if mo:
        return result[1]
    elif mo_2:
        http = [_ for _ in result[0].split("/")]
        return http[-1]
    else:
        return result[0]


# print(domain_name("http://www.kdpszzdxcd4k2.name/error"))


def title_case(title, minor_words=''):
    result = title.title().split()
    minor_words = minor_words.lower().split()

    for _ in range(len(result)):
        if _ == 0:
            pass
        elif result[_].lower() in minor_words:
            result[_] = result[_].lower()

    return " ".join(result)


test = "a clash of KINGS"
x = "a an the OF"


# print(title_case(test, x))

arr_1 = ['cod', 'code', 'wars', 'ewar', 'ar']
arr_2 = ['lively', 'alive', 'harp', 'sharp', 'armstrong', 'codewars']

result = set()
z = [x for x in arr_1 if x in arr_2]

for x in arr_1:
    for y in arr_2:
        if x in y:
            result.add(x)

# print(list(sorted(result)))


# 1. move first letter of each work to end


def pig_it(text):
    first_letter = [f"{_[0]}ay" if _.isalpha() else _ for _ in text.split(" ")]
    word = [_[1:] for _ in text.split(" ")]

    comp = [x+y for x, y in zip(word, first_letter)]

    return " ".join(comp)


print(pig_it("O tempora o mores !"))
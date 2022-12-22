from collections import Counter

# without using collections Counter
def vowel_count():
    text = input("Enter text:\t")
    vowels = "AEIOU"
    vowel_dict = {}

    for _ in vowels:
        if _ in text.upper():
            vowel_dict.setdefault(_, 0)

    print(vowel_dict)

    for _ in text.upper():
        if _ in vowels:
            vowel_dict[_] += 1

    return vowel_dict


# Using collections Counter
def refact_vowel_count():
    text = input("Enter text:\t")
    vowels = "AEIOU"

    count = Counter()
    for _ in text.upper():
        if _ in vowels:
            count.update(_)
    print(count)

print(refact_vowel_count())
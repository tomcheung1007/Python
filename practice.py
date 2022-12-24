def expanded_form(num):
    string = list()
    length = len(str(num)) - 1

    print(str(num))
    for char in str(num):
        if char != '0':
            string.append(char + length * '0')
        length -= 1
    return ' + '.join(string)


print(expanded_form(70304))

good = {"Hobbits": 1, "Men": 2, "Elves": 3, "Dwarves": 3, "Eagles": 4, "Wizards": 10}
evil = {"Orcs": 1, "Men": 2, "Wargs": 2, "Goblins": 2, "Uruk Hai": 3, "Trolls": 5,
        "Wizards": 10}

test = ('0 0 0 0 0 10', '0 1 1 1 1 0 0')

x, y = test

print(x)
print(y)
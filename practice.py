
test = {'u': True, 'l': True, 'n': False, 's': True}

type = [k for k, v in test.items() if v == True]

print(type)
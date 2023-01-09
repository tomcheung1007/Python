test = "79927398713"
result = [int(_) for i, _ in enumerate(test) if i % 2 == 0]  # test[0::2]
num_list = [int(_)*2 for i, _ in enumerate(test) if i % 2 == 1]  # test[1::2]

td = [str(_) for _ in num_list if len(str(_)) == 2]  # list of numbers two digit long

# replace two-digit numbers with sum of digits i.e. 18 = 1+8
for _ in num_list:
    if len(str(_)) == 2:
        num_list.remove(_)
for _ in td:
    total = int(_[0]) + int(_[1])
    num_list.append(total)

# add elements in num_list to result
for _ in num_list:
    result.append(_)

total_sum = sum(result)

# if total modulo 10 is equal to 0: Valid according to Luhn formula
if total_sum % 10 == 0:
    print("Yes")
else:
    print("No")


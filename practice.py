def change_owed(difference):
    """calculate change to display what is owed"""
    change = {"£20": 2000, "£10": 1000, "£5": 500, "£2": 200, "£1": 100, "50p": 50, "20p": 20,
              "10p": 10, "5p": 5, "2p": 2, "1p": 1,
              }
    return_change = []
    result = []
    finish = 0

    # while loop to add change item to return_change array
    while difference != finish:
        for k, v in change.items():
            if v <= difference:
                total = difference - v
                return_change.append(v)
                difference = total
            if v in return_change:
                result.append(k)
        break
    # if 1 remains. for loop to add remaining 1 to result
    for k, v in change.items():
        if difference == v:
            result.append(k)
    return result

print(change_owed(100))



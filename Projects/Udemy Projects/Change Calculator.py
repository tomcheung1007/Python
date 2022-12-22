def change_calculator():
    """Takes valid input and calculates difference in monetary change"""
    change = {"£20": 2000, "£10": 1000, "£5": 500, "£2": 200, "£1": 100, "50p": 50, "20p": 20,
              "10p": 10, "5p": 5, "2p": 2, "1p": 1,
              }
    return_change = []
    result = []
    finish = 0

    total_cost = True
    paid = True
    # Valid input
    while total_cost:
        try:
            total_cost = float(input("Please enter cost of item:\t"))
        except ValueError:
            print("**ERROR** Exclude special characters and letters\n")
        else:
            break
    while paid:
        try:
            paid = float(input("Please enter amount paid:\t"))
        except ValueError:
            print("**ERROR** Exclude special characters and letters\n")
        else:
            break
    while paid < total_cost:
        print("**ERROR** Amount must be greater than cost\n")
        paid = float(input("Please enter amount paid:\t"))

    # calculate difference 
    difference = paid * 100 - total_cost * 100
    print(f"Change owed: £{round((difference / 100), 2)}")

    # while loop to deduct to calculate change 
    while difference != finish:
        for k, v in change.items():
            if v <= difference:
                difference -= v
                return_change.append(v)

    for k, v in change.items():
        if v in return_change:
            result.append(k)

    print(result)
    return result


change_calculator()


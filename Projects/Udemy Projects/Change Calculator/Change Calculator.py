# Change calculator takes user input and calculates amount of exact change
def change_calculator():
    """User input for cost of item and amount paid. Return change owed"""
    cost, paid = cost_paid()
    return change_owed(calculate_change(cost, paid))


def cost_paid():
    """Valid user input for cost of item and amount paid. Return for calculate_change()"""
    total_cost = True
    paid = True
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

    return total_cost, paid


def calculate_change(cost, paid):
    """return difference between cost and amount paid"""
    difference = paid * 100 - cost * 100  # Convert to workable figure for change_owed()
    print(f"Change owed: £{round((difference / 100), 2)}")
    return difference


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


print(change_calculator())

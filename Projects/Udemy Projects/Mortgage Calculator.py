import time

def mortgage_info():
    """takes input to calculate mortgage payments and duration"""
    total_amount = True
    total_years = True
    interest_rate = True
    # valid input
    while total_amount:
        try:
            amount_borrowed = int(input("Please enter amount borrowed:\t"))
        except ValueError:
            print("**ERROR** Please exclude currency signs")
        else:
            break
    while total_years:
        try:
            years = int(input("Enter number of years mortgage:\t"))
        except ValueError:
            print("**ERROR** Please enter numbers only")
        else:
            break
    while interest_rate:
        interest = float(input("Enter interest rate:\t"))
        break

    # mortgage calculations
    total_months = years * 12
    monthly_pay = amount_borrowed / total_months
    monthly_interest = (interest / 100 * amount_borrowed) / 12

    # display information
    print(f"""\nSummary:
Amount borrowed: £{amount_borrowed}
Duration of mortgage: {total_months} months
Interest rate: {interest}%""")
    time.sleep(1)

    print(f"""
Monthly payments: £{round(monthly_pay, 2)}
Monthly interest: £{monthly_interest}\n""")
    time.sleep(2)

    print("Number of years to pay mortgage taking into account interest")
    count = 0
    while amount_borrowed > 0:
        amount_borrowed -= monthly_pay
        amount_borrowed += monthly_interest
        count += 1

    print(round(count/12))

mortgage_info()




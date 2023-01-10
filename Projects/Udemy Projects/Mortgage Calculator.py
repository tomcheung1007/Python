import time
# Mortgage calculator takes user input to obtain information to provide summary

def mortgage_info():
    """valid input to get amount, duration and interest rate"""
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

    return amount_borrowed, years, interest


def monthly_calculations(amount, years, interest):
    """uses mortgage_info() and calculate monthly payment, years and interest"""
    total_months = years * 12
    monthly_pay = amount / total_months
    monthly_interest = (interest / 100 * amount) / 12

    return total_months, monthly_pay, monthly_interest


def mortgage_calculator():
    """provide summary of mortgage details"""
    amount, years, interest = mortgage_info()
    total_months, monthly_pay, monthly_interest = monthly_calculations(amount, years, interest)
    print(f"""\nSummary:
Amount borrowed: £{amount}
Duration of mortgage: {total_months} months
Interest rate: {interest}%""")
    time.sleep(2)
    print(f"""
Monthly payments: £{round(monthly_pay, 2)}
Monthly interest: £{monthly_interest}\n""")
    time.sleep(2)

    print("Number of years to pay mortgage taking into account interest:")
    count = 0
    while amount > 0:
        amount -= monthly_pay
        amount += monthly_interest
        count += 1
    return round(count / 12)


print(mortgage_calculator())
# Have the user enter a number and find all Prime Factors (if there are any)
# and display them

def prime_factorization():
    prime_list = set()

    p = 2
    # User input - number
    n = int(input("Please enter number:\t"))

    while n >= p:
        if n % p == 0:
            prime_list.add(p)
            n = n / p
        else:
            p += 1
    if len(prime_list) == 0:
        print("No prime factors")
    else:
        print(prime_list)


prime_factorization()

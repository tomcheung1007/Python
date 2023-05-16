# The sequence follows the rule that each number is equal
# to the sum of the preceding two numbers
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
# 987, 1597, 2584, 4181.

def fib(n):
    a = 0
    b = 1

    count = 0
    if n <= 0:
        print("Can only accept positive numbers")
    elif n == 1:
        return a
    else:
        while count < n:
            print(a)
            c = a + b
            a = b
            b = c
            count += 1

fib(10)
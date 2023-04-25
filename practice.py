

test = [4, 1, 1, 1, 4]
t = 2

def trouble(x, t):
    result = []
    for _ in range(len(test)-1):
        if test[_] + test[_+1] != t:
            result.append(test[_])

    print(result)
print(trouble(test, t))




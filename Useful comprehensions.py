# Alphabet dictionary
alphabet = {chr(i): i - 96 for i in range(ord("a"), ord("z") + 1)}

# if else structure
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
x = [_ if _ % 2 == 0 else "X" for _ in num_list]
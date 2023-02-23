import csv

file = "/Users/tomcheung/Python/CSV data/Employee Details.csv"
data = open(file, encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)


age = []
x = []
for _ in data_lines[1:]:
    age.append(_[4])


for _ in range(len(age)):
    if age[_] > age[_-1]:
        print(f"{age[_]} is higher than {age[_-1]}")
        x.append(age[_])

print(x)

test = [1, 2, 3, 4, 5, 6, 7]

print(test[-1])



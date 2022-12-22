# Working with CSV files
# CSV files contain only raw data. No formulas etc
import csv

# user_details = "/Users/tomcheung/Python/CSV data example.csv"
# data = open(user_details, encoding="utf-8")
# NOTE - encoding="utf-8" required to prevent error and allow Python to read csv file

# csv_data = csv.reader(data)  # Allow Python to read csv file
# data_lines = list(csv_data)  # reformat file into python object - list
# data.close()

# print(data_lines)

# ACCESSING INFO - EXAMPLES
# print(data_lines[0])  # top row i.e. column names

# CHECK NUMBER OF ROWS
# print(len(data_lines))

# GRABBING TOP 5 ROWS
# for line in data_lines[:5]:
#   print(line)

# SINGLE VALUE WITHIN ROW
# print(data_lines[4][3])  # [row 4] [column 3]

# ENTIRE COLUMN
# all_emails = []
# for line in data_lines[1:5]:
#    all_emails.append(line[3])
# print(all_emails)

# LIST OF FULL NAMES
# full_name = []
# for row in data_lines[1:5]:
#    name = row[1]
#    surname = row[2]
#    full_name.append(f"{name} {surname}")

# print(full_name)

# WRITING A CSV FILE
# file = "/Users/tomcheung/Python/Write to csv file example.csv"
# file_to_output = open(file, mode="w", newline="")  # mode="w" >> write (this will overwrite data)
# csv_writer = csv.writer(file_to_output, delimiter=",")  # delimiter - another word for seperator between columns

# WRITE SINGLE ROW
# print(csv_writer.writerow(["A", "B", "C"]))
# file_to_output.close()

# ENTER DATA
# print(csv_writer.writerows([["RED", "GREEN", "BLUE"], ["DOG", "CAT", "FISH"]]))
# file_to_output.close()

# APPEND CSV FILE
# f = open(file, mode="a", newline="")  # mode="a" >> append (add to file)
# csv_writer = csv.writer(f)
# csv_writer.writerow(["SAM", "BARB", "BOB"])
# f.close()

import csv

file = "/Users/tomcheung/Python/Working with CSV & PDF files/CSV Exercise.csv"
data = open(file, encoding="utf-8")
csv_reader = csv.reader(data)
data_lines = list(csv_reader)

element = 0
index = 0
url = []

for line in data_lines[1:]:
    url.append(line[element])
    element += 1

print("".join(url))
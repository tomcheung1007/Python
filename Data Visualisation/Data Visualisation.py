import matplotlib.pyplot as plt

# matplotlib is a library for creating static, animated and interactive data visualisation

# matplotlib comes with predefined styles for your data visualisation
print("Graph styles")
print(plt.style.available)

# BASIC GRAPH
# SUMMARY
# 1. Set up graph using subplot()
# 2. Input data into graph using plot()
# 3. Set heading for title, X and Y-axis

# data to use in graph
input_values_x = [1, 2, 3, 4, 5]
squares_y = [1, 4, 9, 3, 25]

# set up graph
fig, ax = plt.subplots()  # fig - graph, ax - plots
ax.plot(input_values_x, squares_y, linewidth=3)  # y-axis, x-axis, line width

# chart tite, and label axis
ax.set_title("Graph using plot()", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# size of tick labels (values)
ax.tick_params(axis="both", labelsize=14)

# PLOT SINGLE POINT USING SCATTER()
fig, ax = plt.subplots()

ax.set_title("Single plot using scatter()", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.scatter(2, 4, s=200)  # (x, y, size)

# size of tick labels (values)
ax.tick_params(axis="both", which="major", labelsize=14)

# PLOT SERIES OF POINTS USING SCATTER()

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)
ax.set_title("Scatter graph using scatter()", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# APPLYING FOR LOOPS TO GRAPHS

x = [_ for _ in range(0, 101)]
y = [_ ** 2 for _ in x]

fig, ax = plt.subplots()
ax.scatter(x, y, s=5, c="red")  # c=colour
ax.set_title("Scatter graph using range to generate values", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# size of tick labels (values)
ax.tick_params(axis="both", which="major", labelsize=14)

# EXAMPLE
# Create a graph using Bank - Agency - data.csv file
import matplotlib.pyplot as plt
import csv

file = "/Users/tomcheung/Downloads/Bank - Agency - data.csv"
data = open(file, encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

bank_shifts = [int(_[1]) for _ in data_lines[1:61]]
agency_shifts = [int(_[2]) for _ in data_lines[1:61]]
months = [_[0] for _ in data_lines[1:61]]

fig, ax = plt.subplots()
ax.plot(months, agency_shifts, c="green", linewidth=1)
ax.plot(months, bank_shifts, c="red", linewidth=1)
ax.set_title("Bank and Agency shifts - 2018-2022", fontsize=15)
ax.set_xlabel("Months", fontsize=7)
ax.set_ylabel("Shifts", fontsize=7)

ax.tick_params(axis="x", rotation=90, labelsize=5)  # rotation=n to rotate ticker
ax.tick_params(axis="y", labelsize=5)
plt.show()


# HISTOGRAM - Plotly

from random import randint


class Dice:
    """class for single 6 sided die"""
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """reenact roll of die"""
        return randint(1,self.num_sides)


die = Dice()
roll_results = []

for _ in range(101):
    result = die.roll()
    roll_results.append(result)





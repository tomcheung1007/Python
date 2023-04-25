# Collect results of rolling die and visualise data using Plotly
from plotly.graph_objs import Bar, Layout
from plotly import offline
from random import randint

# CREATING DICE CLASS
class Die:
    """class for single 6 sided die"""
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """reenact roll of die"""
        return randint(1,self.num_sides)

# CREATING INSTANCE OF DIE CLASS
die = Die()

# ROLL DIE
roll_results = []
for _ in range(1001):
    result = die.roll()
    roll_results.append(result)

# ANALYSING THE RESULTS
frequencies = []  # later used for y-axis of graph
for _ in range(1, die.num_sides+1):
    frequency = roll_results.count(_)
    frequencies.append(frequency)
# print(frequencies)

# VISUALISING THE DATA
x_values = list(range(1, die.num_sides+1))  # for x-axis
data = [Bar(x=x_values, y=frequencies)]  # store data

x_axis_config = {'title' : 'Die value'}
y_axis_config = {'title' : 'Score'}
my_layout = Layout(title="Results of rolling die 1000 times",
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data":data, "layout":my_layout}, filename="d6.html")  # to generate plot










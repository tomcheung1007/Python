# Collect results of two rolling dice and visualise data using Plotly
from plotly.graph_objs import Bar, Layout
from plotly import offline

from Die import Die

# CREATING INSTANCE OF DIE CLASS
die_1 = Die()
die_2 = Die()

# ROLL DIE
roll_results = []
for _ in range(1001):
    result = die_1.roll() + die_2.roll()
    roll_results.append(result)

# ANALYSING THE RESULTS
frequencies = []
max_result = die_1.num_sides + die_2.num_sides  # this allows us to model variety of situations i.e. any number sides
for _ in range(2, max_result+1):
    frequency = roll_results.count(_)
    frequencies.append(frequency)
# print(frequencies)

# VISUALISING THE DATA
x_values = list(range(2, max_result+1))  # this is better alternative to range(2, 13) because it is easier to model
# different situations e.g. can change number of sides in dice
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'Dice value', 'dtick':1}  # dtick - label each bar
y_axis_config = {'title':'Score '}
my_layout = Layout(title="Results of rolling two dice 1000 times",
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data":data, "layout":my_layout}, filename="d6_x2.html")










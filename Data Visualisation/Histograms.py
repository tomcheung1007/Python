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
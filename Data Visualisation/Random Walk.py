# A random walk is a path that has no clear directions and is dictated by random decisions
# e.g. a drunk man's path where every step taken is random

from random import choice


class Random_Walk:
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        """calculate points in walk"""

        # while loop to generate points to max limit
        while len(self.x_value) < self.num_points:
            # decide direction to go and how far in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # reject move that goes nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate new position
            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step

            self.x_value.append(x)
            self.y_value.append(y)

# PLOTTING RANDOM WALK - Data visualisation
import matplotlib.pyplot as plt
from random_walk import Random_Walk

# REPRESENT RANDOM WALK IN SCATTER GRAPH

while True:
    # create object of class Random_Walk()
    rw = Random_Walk()
    rw.fill_walk()
    # plot points
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 9))

    # COLORING THE POINTS
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Spectral,
               edgecolors="none", s=5)

    # EMPHASIZE FIRST AND LAST POINT
    ax.scatter(0, 0, c="green", edgecolors="none", s=50)
    ax.scatter(rw.x_value[-1], rw.y_value[-1], c="red", edgecolors="none", s=50)

    # REMOVE AXES / MAKE AVES INVISIBLE
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    # GENERATING MULTIPLE RANDOM WALKS - While True and keep_running as switch
    keep_running = input("Make another walk (y/n)?:\t")
    if keep_running == "n":
        break

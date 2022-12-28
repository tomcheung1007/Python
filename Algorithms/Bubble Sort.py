# Bubble sort is often an entry level algorithm for beginners
# Used as an introduction to algorithms
# Important to note Bubble Sort is one of the worst performing sorting algorithms

# Concept
# Looks at pairs of adjacent elements one pair at a time
# Swap position if first element is larger than second element
# It then looks at the next adjacent element


def bubble_sort(array):
    swap = True

    while swap:
        swap = False
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swap = True

test = [1,4,8,2,43,76,123,56,78,26,48,51]

bubble_sort(test)
print(test)
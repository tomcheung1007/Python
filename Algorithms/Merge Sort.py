# Sorting - Implement two types of sorting algorithms:
# Merge sort and bubble sort.

# MERGE SORT
# An efficient sorting algorithm - for large data sets
# A recursive method (a method/function that calls itself)

# Technique
# 1.involves dividing a problem into multiple sub problems
# 2.each sub problem is solved individually
# 3.sub problems are combined


def mergeSort(arr):
    if len(arr) > 1:
        # arr = [6, 5, 4, 8, 1, 9]
        # Create start ← A[start..mid] and end ← A[mid+1..end]
        mid = len(arr) // 2
        left = arr[:mid]  # arr = [6, 5, 4]
        right = arr[mid:]  # arr = [8, 1, 9]

        # Sort the two halves and recursively divide until base case reached
        mergeSort(left)
        mergeSort(right)

        i = 0  # index for left array
        j = 0  # index for right array
        k = 0  # index for original array

        # Until we reach the end of either left or right, pick larger among elements
        # start and end and place them in the correct position in the sorted array

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # the above reads if left[0] is less than right[0], value of left[0] becomes arr[0]
        # and vice versa. Then we repeat by index += 1

        # When all elements are traversed in either left or right,
        # pick up the remaining elements and put in sorted array

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = [6, 5, 4, 8, 1, 9]


# mergeSort(arr)
# print(arr)


def merge_sort(array):
    # 1. Store the length of the list
    list_length = len(array)

    # 2. List with length less than is already sorted
    if list_length == 1:
        return array

    # 3. Identify the list midpoint and partition the list into a left_partition and a right_partition
    mid_point = list_length // 2

    # 4. To ensure all partitions are broken down into their individual components,
    # the merge_sort function is called and a partitioned portion of the list is passed as a parameter
    left_partition = merge_sort(array[:mid_point])
    right_partition = merge_sort(array[mid_point:])

    # 5. The merge_sort function returns a list composed of a sorted left and right partition.
    return merge(left_partition, right_partition)


# 6. takes in two lists and returns a sorted list made up of the content within the two lists
def merge(left, right):
    # 7. Initialize an empty list output that will be populated with sorted elements.
    # Initialize two variables i and j which are used pointers/indexing when iterating through the lists.
    output = []
    i = j = 0

    # 8. Executes the while loop if both pointers i and j are less than the length of the left and right lists
    while i < len(left) and j < len(right):
        # 9. Compare the elements at every position of both lists during each iteration
        if left[i] < right[j]:
            # output is populated with the lesser value
            output.append(left[i])
            # 10. Move pointer to the right
            i += 1
        else:
            output.append(right[j])
            j += 1
    # 11. The remnant elements are picked from the current pointer value to the end of the respective list
    output.extend(left[i:])
    output.extend(right[j:])

    return output


def run_merge_sort():
    unsorted_list = [2, 6, 8, 2, 3, 9, 1, 4, 9]
    print(unsorted_list)
    sorted_list = merge_sort(unsorted_list)
    print(sorted_list)


run_merge_sort()

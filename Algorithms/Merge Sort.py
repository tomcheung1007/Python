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

        # Sort the two halves
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
mergeSort(arr)
print(arr)
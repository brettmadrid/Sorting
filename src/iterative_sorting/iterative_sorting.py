# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr)):
        lowest = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest]:
                lowest = j

        # TO-DO: swap
        if i != lowest:
            arr[i], arr[lowest] = arr[lowest], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # set variable to track if swaps were made
    swaps_occurred = True  # to start the loop
    while swaps_occurred:
        # Now reset swaps to False & only set to True if a swap occurs
        swaps_occurred = False
        for i in range(0, len(arr) - 1):
            # if element to the right is smaller, swap them
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps_occurred = True

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_val = arr[i]
        j = i - 1

        # if value to the right is smaller
        while j >= 0 and current_val < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # already in order, move on to the next
        if j + 1 != i:
            arr[j + 1] = current_val

    return arr


# STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):
#     return arr

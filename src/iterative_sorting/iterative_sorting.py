# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        lowest = i
        smallest_index = lowest
        # TO-DO: find next smallest element
        for j in range(i + 1, len(arr) - 1):
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


# STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):
#     return arr

print(bubble_sort([25, 67, 4, 33, 19, 40]))

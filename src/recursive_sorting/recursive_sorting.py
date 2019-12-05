# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0

    '''
    Both arrA and arrB are already sorted, so only need to compare
    the same index of each to each other and store the value
    that is smaller in the merged_arr.  Starting at index 0 for 
    both arrays, the while loop runs as long as the length of the 
    arrays are valid
    '''

    for i in range(0, elements):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, add to merged_arr
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, add to merged_arr
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr

    # # # Split array into two halves
    mid = len(arr) // 2

    # # # recursively keep splitting until each side is an array of one item
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])

    # # # now recursively join back together using the merge helper function
    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr


# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):

#     return arr


print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

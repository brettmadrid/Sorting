'''
Both arrA and arrB are already sorted, so only need to compare
the same index of each to each other and store the value
that is smaller in the merged_arr.  Starting at index 0 for 
both arrays, the while loop runs as long as the length of the 
arrays are valid
'''


import random


def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []
    a, b = 0, 0

    # loop iterates until all the elements are used up in one of the arrays
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1

    if a == len(arrA):  # if at the end of arrA
        merged_arr.extend(arrB[b:])  # add any remaining items from arrB
    else:
        merged_arr.extend(arrA[a:])  # add any remaining items from arrA

    return merged_arr


def merge_sort(arr):
    # an array of zero or one element is sorted by definition
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # split array into halves and recursively call merge_sort on each half
    left, right = merge_sort(arr[0:mid]), merge_sort(arr[mid:])

    # merge the now sorted sub arrays
    return merge(left, right)


'''
Pseudo code for merge sort in place
1. maintain two pointers that point to both halves that need to be sorted
2. compare the elements for where the pointers are present
3. if element1 < element2, then element1 is in the right place, so increase the pointer to the next item
4. Else place element2 in its right position and all the elements at the right of element2 will be shifted right by one position. Increment all the pointers by 1.
'''
# STRETCH: implement an in-place merge sort algorithm


# def merge_in_place(arr, start, mid, end):
#     # TO-DO
#     left = arr[start:mid]
#     right = arr[mid:end]
#     i = 0
#     j = 0
#     k = start
#     for l in range(k, end):
#         if j >= len(right) or (i < len(left) and left[i] < right[j]):
#             arr[l] = left[i]
#             i = i + 1
#         else:
#             arr[l] = right[j]
#             j = j + 1
#     return arr


# def merge_sort_in_place(arr, l, r):
#     # TO-DO
#     if r - l > 1:
#         mid = int((l + r) / 2)
#         merge_sort_in_place(arr, l, mid)
#         merge_sort_in_place(arr, mid, r)
#         merge_in_place(arr, l, mid, r)
#     return arr


# arr1 = random.sample(range(200), 50)
# print(merge_sort_in_place(arr1, 0, len(arr1)-1))


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):

#     return arr

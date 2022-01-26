import time
import numpy as np

def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


arr = np.random.randint(1, 900, 950)

bubble_sort_start_time = time.time()
bubbleSort(arr)
bubble_sort_end_time = time.time()
quick_sort_start_time = time.time()
quickSort(arr, 0, len(arr)-1)
quick_sort_end_time = time.time()

print('Bubble sort time')
print(bubble_sort_end_time - bubble_sort_start_time)
print('Quicksort time')
print(quick_sort_end_time - quick_sort_start_time)

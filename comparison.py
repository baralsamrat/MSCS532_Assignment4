import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    while left and right:
        if left[0] <= right[0]:
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))

    sorted_arr.extend(left if left else right)
    return sorted_arr

def time_sorting_algorithm(algorithm, arr):
    start_time = time.time()
    algorithm(arr)
    end_time = time.time()
    return end_time - start_time

# Compare Heapsort, Quicksort, and Merge Sort on different input distributions
arr_sizes = [1000, 5000, 10000, 20000]
distributions = ["random", "sorted", "reverse_sorted"]

for size in arr_sizes:
    for distribution in distributions:
        if distribution == "random":
            arr = [random.randint(1, size) for _ in range(size)]
        elif distribution == "sorted":
            arr = list(range(1, size + 1))
        elif distribution == "reverse_sorted":
            arr = list(range(size, 0, -1))

        print(f"\nArray Size: {size}, Distribution: {distribution}")
        
        # Heapsort Algo
        heap_arr = arr.copy()
        heap_time = time_sorting_algorithm(heapsort, heap_arr)
        print(f"Heapsort Time: {heap_time:.6f} seconds")
        
        # Quicksort Algo
        quick_arr = arr.copy()
        quick_time = time_sorting_algorithm(quicksort, quick_arr)
        print(f"Quicksort Time: {quick_time:.6f} seconds")
        
        # Merge Sort Algo
        merge_arr = arr.copy()
        merge_time = time_sorting_algorithm(merge_sort, merge_arr)
        print(f"Merge Sort Time: {merge_time:.6f} seconds")

def iterative_heapify(arr, n, i):
    largest = i
    while True:
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest  # Continue heapifying down the tree
        else:
            break

def heapsort(arr):
    n = len(arr)
    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        iterative_heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        iterative_heapify(arr, i, 0)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
heapsort(arr)
print("Sorted array is:", arr)

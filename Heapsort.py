# Heapsort implementation in Python

def heapify(arr, n, i):
    # Implement heapify
  
def heapsort(arr):
    n = len(arr)

    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # Swaping
        heapify(arr, i, 0)

# Example usage

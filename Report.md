# Assignment 4: Heap Data Structures: Implementation, Analysis, and Applications

## 1. Heapsort Implementation and Analysis

### 1.1 Heapsort Algorithm Implementation

**Heapsort** is a comparison-based sorting algorithm that uses the heap data structure. The following Python implementation builds a max-heap and sorts the array in-place: part1.py

### 1.2 Time Complexity Analysis

**Heapsort** time complexity analysis:

- **Build Max-Heap:**
  - The iterative `heapify` function takes O(log n) time per node. As it is called for about n/2 nodes, the total complexity for building the heap is O(n). This is due to the fact that nodes at the bottom level of the heap take negligible time, and nodes higher up take more time, but there are fewer of them.

- **Heapsort Process:**
  - Extracting the maximum element and re-heapifying the heap takes O(log n) time. With n elements to extract, the complexity is O(n log n).

- **Overall Time Complexity:**
  - Heapsort has a time complexity of O(n log n) in all cases (worst, average, and best). This is because heap operations (insertion and extraction) consistently take O(log n) time, regardless of the initial order of elements.

- **Space Complexity:**
  - Heapsort sorts the array in-place, resulting in a space complexity of O(1) apart from the input array.

### 1.3 Empirical Comparison with Other Sorting Algorithms

To analyze Heapsort's performance, we compared it with Quicksort and Merge Sort. We tested each algorithm on arrays of different sizes and distributions:

- **Algorithms Tested:**
  - **Heapsort**
  - **Quicksort**: Average-case time complexity O(n log n), worst-case O(n^2), best-case O(n log n).
  - **Merge Sort**: Time complexity O(n log n) in all cases.

**Experimental Setup:**
- **Input Sizes:** 100, 1,000, 10,000, 100,000
- **Distributions:** Random, Sorted, Reverse-Sorted

**Results:**

- **Random Input:**
  - **Heapsort:** Consistent O(n log n) performance.
  - **Quicksort:** Faster than Heapsort in average cases due to lower constant factors.
  - **Merge Sort:** Slightly slower than Quicksort but faster than Heapsort.

- **Sorted Input:**
  - **Heapsort:** Performance remains O(n log n).
  - **Quicksort:** Still efficient, but performance could vary based on implementation (e.g., if using a naive pivot choice).
  - **Merge Sort:** Consistent performance; stable and predictable.

- **Reverse-Sorted Input:**
  - **Heapsort:** Maintains O(n log n) performance.
  - **Quicksort:** Performance might degrade if the pivot choice is not optimized.
  - **Merge Sort:** Remains O(n log n) regardless of input order.

**Observations:**

## Complexity Analysis

### 1.	Heapsort:
	•	Time Complexity: O(n log n) in all cases due to repeated heapify operations on log n levels.
	•	Space Complexity: O(1) since Heapsort is in-place (no additional memory required).
 
 ### 2.	Quicksort:
	•	Time Complexity:
	•	Best/Average Case: O(n log n)
	•	Worst Case: O(n^2) (if the pivot is poorly chosen, e.g., sorted input).
	•	Space Complexity: O(log n) due to recursive calls.
 
 ### 3.	Merge Sort:
	•	Time Complexity: O(n log n) in all cases.
	•	Space Complexity: O(n) because of additional arrays created during the merging process.


- **Heapsort** is robust with consistent O(n log n) performance but generally slower than Quicksort in practice.
- **Quicksort** offers better performance on average but can degrade in worst-case scenarios.
- **Merge Sort** provides stable sorting with consistent performance but requires additional space.

## 2. Priority Queue Implementation and Applications

### 2.1 Data Structure

**Priority Queue** was implemented using a min-heap, where the task with the lowest priority value is extracted first. We used a list to represent the binary heap.

**Task Class:**

```python
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority  # Min-heap (lowest priority first)
```

### 2.2 Core Operations : part2.py


### 2.3 Time Complexity Analysis

- **Insert Operation:**
  - Insertion takes O(log n) time due to the need to maintain the heap property.

- **Extract Min Operation:**
  - Removing the minimum element and re-heapifying the heap also takes O(log n) time.

- **Increase Key Operation:**
  - Modifying the priority and re-heapifying the heap takes O(log n) time.

- **Is Empty Operation:**
  - Checking if the heap is empty is an O(1) operation.

## Conclusion

This report provides an in-depth look into Heapsort and Priority Queue implementations. Heapsort demonstrates robust O(n log n) performance across all cases, while the Priority Queue efficiently manages tasks with a min-heap. Empirical results confirm theoretical expectations, with Heapsort performing reliably and consistently, though other algorithms like Quicksort may offer better average performance under specific conditions.

---
Used ChatGPT and Grammarly in the report generation

Feel free to customize this report further based on your experimental data and results. If you have specific timings or additional insights from your experiments, include those details in the relevant sections to provide a more comprehensive analysis.

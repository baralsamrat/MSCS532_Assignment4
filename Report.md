#### **Part 1: Heapsort Implementation & Analysis**

1. **Implementation**:
    - We will implement the Heapsort algorithm step-by-step:
      - First, build a max-heap from the array.
      - Then, repeatedly extract the maximum element from the heap and rebuild it, placing the extracted element at the end of the sorted portion of the array.
  
2. **Analysis**:
    - We will rigorously analyze the time complexity:
      - **Worst case**: `O(n log n)` (since each heapify operation takes `O(log n)` and we perform it `n` times).
      - **Average case**: `O(n log n)` (as the same operations are performed irrespective of input distribution).
      - **Best case**: `O(n log n)` (since we must heapify and sort, even if the input is already sorted).
    - The space complexity of the in-place Heapsort algorithm is `O(1)` auxiliary space (apart from the input array).

3. **Comparison**:
    - We will compare Heapsort with Quicksort and Merge Sort using different input distributions: sorted, reverse-sorted, and random.
    - We will provide empirical comparisons and discuss how the performance results relate to the theoretical complexity.

---

#### **Part 2: Priority Queue Implementation & Applications**

1. **Data Structure**:
    - We'll represent the binary heap using a Python list (array-based heap), as it allows efficient indexing and manipulation for heap operations.
    - We'll create a `Task` class with attributes like `task_id`, `priority`, `arrival_time`, and `deadline`.
    - Depending on the problem context, we will use either a max-heap or min-heap. For scheduling, typically a **min-heap** (lower priority number = higher priority) is preferred.

2. **Core Operations**:
    - **Insert**: Insert a task into the heap, maintaining the heap property.
    - **Extract Max/Min**: Remove the highest (or lowest) priority task.
    - **Increase/Decrease Key**: Change the priority of an existing task and adjust the heap structure.
    - **Is Empty**: A helper method to check if the queue is empty.

3. **Deliverables**:
    - Well-documented Python code for both the Heapsort and Priority Queue operations.
    - A detailed report on design choices and complexity analysis.
    - A GitHub repository with all the source code and documentation.

---
### Next Steps:

1. **Run Comparisons** for Heapsort, Quicksort, and Merge Sort.
2. Write the **detailed report** with complexity analysis.
3. Prepare the GitHub repository for final submission.

---

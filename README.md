# Assignment 4: Heap Data Structures: Implementation, Analysis, and Applications

[Report of Assignment](/Report.md)

## Overview:
This assignment aims to solidify your understanding of heap data structures, their implementation using
arrays, and their applications in sorting (Heapsort) and priority queue operations. You will analyze the
efficiency of these algorithms and explore their use in real-world scenarios.

##  Heapsort Implementation and Analysis

### 1. Implementation
- Implement the Heapsort algorithm using Python. Ensure your implementation is clear, efficient, and follows
the correct steps for building a max-heap, extracting the maximum element, and maintaining the heap
property.


### 2. Analysis of Implementation
- Provide a rigorous analysis of the time complexity of Heapsort in the worst, average, and best cases.
- Explain why it is O(n log n) in all cases.
- Discuss the space complexity and any additional overheads.


### 3. Comparison
- Empirically compare the running time of Heapsort with other sorting algorithms like Quicksort and Merge
Sort on different input sizes and distributions (e.g., sorted, reverse-sorted, random).
- Discuss the observed results and relate them to the theoretical analysis.

## Priority Queue Implementation and Applications

### Part A: Priority Queue Implementation

### 1. Data Structure:
- Choose a suitable data structure to represent your binary heap (array or list). Justify your choice based on
the ease of implementation and the efficiency of heap operations.
- Design a Task class or struct to represent individual tasks, storing relevant information like task ID, priority,
arrival time, deadline, etc.
- Decide whether you'll use a max-heap (highest priority first) or min-heap (lowest priority first) based on
your chosen scheduling algorithm.

### 2. Core Operations:
- insert(task): Implement the logic to insert a new task into the heap while maintaining the heap property.
Analyze the time complexity of this operation.
- extract_max/min(): Implement the logic to remove and return the task with the highest/lowest priority
from the heap, again ensuring the heap property is maintained. Analyze the time complexity.
- increase/decrease_key(task, new_priority): Implement the logic to modify the priority of an existing task in
the heap and adjust its position accordingly. Analyze the time complexity.
- is_empty(): Implement a simple check to determine if the priority queue is empty.


### Deliverables:
- Well-documented source code for your priority queue implementation and scheduler simulation.
- A detailed report discussing your design choices, implementation details, and analysis of the scheduling
results.
- Clear explanations of the time complexity analysis for priority queue operations.


## Submission Instructions:
### 1. GitHub Repository:
- Create a new GitHub repository for this assignment.
- Upload the following materials to your repository:
- Your Python implementation of Heapsort and the Priority Queue.
- A report detailing your design choices, implementation details, and analysis.
- A README file with instructions on how to run your code and a summary of your findings.


### 2. Submit the GitHub Repository Link:
- Submit the link to your GitHub repository as your final submission.

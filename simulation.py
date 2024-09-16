def scheduling_simulation():
    pq = PriorityQueue()

    # Create tasks with task_id, priority, arrival_time, deadline
    tasks = [
        Task(1, 5, 0, 10),  # Task 1: Priority 5
        Task(2, 1, 2, 8),   # Task 2: Priority 1 (highest priority)
        Task(3, 3, 4, 12)   # Task 3: Priority 3
    ]
    
    # Insert tasks into the priority queue
    for task in tasks:
        pq.insert(task)
    
    # Extract tasks based on priority
    print("Tasks executed in the order of priority:")
    while not pq.is_empty():
        task = pq.extract_min()
        print(f"Executing Task ID: {task.task_id}, Priority: {task.priority}")

# Run scheduling simulation
scheduling_simulation()

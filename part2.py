class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline
    
    def __lt__(self, other):
        return self.priority < other.priority  # For min-heap (lower value = higher priority)
    
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, task):
        return
    
    def extract_min(self):
        return

    def decrease_priority(self, task_index, new_priority):
        return
        
    def is_empty(self):
        return 
        
    def _sift_up(self, idx):
        return
        
    def _sift_down(self, idx):
        return 
        
# Example 

print("Tasks sorted by priority:")
while not pq.is_empty():
    task = pq.extract_min()
    print(f"Task ID: {task.task_id}, Priority: {task.priority}")

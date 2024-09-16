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
        self.heap.append(task)
        self._sift_up(len(self.heap) - 1)

    def extract_min(self):
        if self.is_empty():
            return None
        self._swap(0, len(self.heap) - 1)
        min_task = self.heap.pop()
        self._sift_down(0)
        return min_task

    def decrease_priority(self, task_index, new_priority):
        self.heap[task_index].priority = new_priority
        self._sift_up(task_index)

    def is_empty(self):
        return len(self.heap) == 0

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        if parent >= 0 and self.heap[idx] < self.heap[parent]:
            self._swap(idx, parent)
            self._sift_up(parent)

    def _sift_down(self, idx):
        left = 2 * idx + 1
        right = 2 * idx + 2
        smallest = idx

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != idx:
            self._swap(idx, smallest)
            self._sift_down(smallest)

    
# Example usage
pq = PriorityQueue()
tasks = [Task(1, 3, 0, 5), Task(2, 1, 1, 4), Task(3, 2, 2, 6)]
for task in tasks:
    pq.insert(task)

print("Tasks sorted by priority:")
while not pq.is_empty():
    task = pq.extract_min()
    print(f"Task ID: {task.task_id}, Priority: {task.priority}")

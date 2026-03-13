#Priority queue removes element based on priority.

import heapq

pq = []
# (priority_number, task_name)
heapq.heappush(pq, (2, "Task B"))
heapq.heappush(pq, (1, "Task A")) # Sabse high priority
heapq.heappush(pq, (3, "Task C"))

# Sabse high priority wala task pehle niklega
print(heapq.heappop(pq)) # Output: (1, 'Task A')

from collections import deque
from queue import Queue, PriorityQueue

# Example 1: Queue Using `collections.deque`
print("Example 1: Queue Using `collections.deque`")
queue = deque()
queue.append("apple")
queue.append("banana")
queue.append("cherry")
print("Queue after enqueuing:", queue)
item = queue.popleft()
print("Dequeued item:", item)
print("Queue after dequeuing:", queue)
print("-" * 50)


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

# Example 2: Queue Using `queue.Queue`
print("Example 2: Queue Using `queue.Queue`")
q = Queue()
q.put("apple")
q.put("banana")
q.put("cherry")
print("Queue size after enqueuing:", q.qsize())
item = q.get()
print("Dequeued item:", item)
print("Queue size after dequeuing:", q.qsize())
print("-" * 50)

# Example 3: Queue with Maximum Size Limit
print("Example 3: Queue with Maximum Size Limit")
q = Queue(maxsize=3)
q.put("apple")
q.put("banana")
q.put("cherry")
print("Queue full:", q.full())
try:
    q.put("date", timeout=1)
except:
    print("Couldn't add date, queue is full")
while not q.empty():
    print("Dequeued item:", q.get())
print("-" * 50)

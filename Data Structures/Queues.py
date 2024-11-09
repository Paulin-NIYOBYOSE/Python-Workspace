from collections import deque
from queue import Queue, PriorityQueue
from collections import deque
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

# Example 4: Queue with `PriorityQueue`
print("Example 4: Queue with `PriorityQueue`")
pq = PriorityQueue()
pq.put((2, "banana"))

pq.put((1, "apple"))
pq.put((3, "cherry"))
while not pq.empty():
    priority, item = pq.get()
    print(f"Dequeued item with priority {priority}: {item}")
print("-" * 50)


# Example 5: Implementing Queue with List
print("Example 5: Implementing Queue with List")
queue = []
queue.append("apple")
queue.append("banana")
queue.append("cherry")
print("Queue after enqueuing:", queue)
item = queue.pop(0)
print("Dequeued item:", item)
print("Queue after dequeuing:", queue)
print("-" * 50)

#More queue exercises
data = []
data.append(5)
data.append(10)
data.append(15)
data.append(20)
data.pop(0)
data.pop(0)
print(data)


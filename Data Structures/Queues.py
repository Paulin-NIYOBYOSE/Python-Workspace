from collections import deque
from queue import Queue, PriorityQueue
from collections import deque

from numpy.random import normal

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

#Queues exercises
#Customer service line
customers = []
def add_customer(customerToAdd):
    customers.append(customerToAdd);
def serve_customer():
    if customers:
        customerToServe = customers.pop(0)
        print("Serving " + customerToServe)
    else:
        print("No customer to serve")
serve_customer()
add_customer("Customer 01")
add_customer("Customer 02")
add_customer("Customer 03")
print(customers)
serve_customer()
serve_customer()
serve_customer()

#Combined Exercises: Using Both Stack and Queue
#Text Editor with Undo and Redo
text = []
undo_stack = []
def add_text(textToAdd):
    text.append(textToAdd)
    undo_stack.clear
def undo():
    if text:
     textToUndo = text.pop()
     undo_stack.append(textToUndo)
     print("Removed"+ textToUndo)
    else:
        print("No text")
def redo():
    if undo_stack:
        textToRedo = undo_stack.pop()
        text.append(textToRedo)
        print("Redone" + textToRedo)
    else:
        print("No text to redo")
add_text("Hello")
add_text("World")
undo()          # Output: Removed " World"
redo()          # Output: Redone " World"

#Task Manager with Prioritization
# Desc: Normal tasks are added to a queue.
# High-priority tasks are added to a stack to be handled first.
normal_tasks = []
priority_tasks = []
def add_normal_task(normal_task):
    normal_tasks.append(normal_task)

def add_priority_task(priority_task):
    priority_tasks.append(priority_task)

def process_task():
    if priority_tasks:
        task_to_process = priority_tasks.pop(0)
        print("Processing " + task_to_process)
    elif normal_tasks:
        task_to_process = normal_tasks.pop(0)
        print("Processing " + task_to_process)
    else:
        print("No task to process")

add_normal_task("Check email")
add_priority_task("Fix critical bug")
add_normal_task("Write report")
add_priority_task("Respond to urgent client")
process_task()  # Should process high-priority task first
process_task()  # Continue processing tasks








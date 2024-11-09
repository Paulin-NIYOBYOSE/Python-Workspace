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

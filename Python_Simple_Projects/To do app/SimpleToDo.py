# todo_list.py
todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if todo_list:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task}")
    else:
        print("No tasks in the list.")

def remove_task(index):
    if 0 < index <= len(todo_list):
        removed = todo_list.pop(index - 1)
        print(f"Task '{removed}' removed.")
    else:
        print("Invalid index.")

while True:
    print("\nTo-Do List Options:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        index = int(input("Enter task number to remove: "))
        remove_task(index)
    elif choice == '4':
        break
    else:
        print("Invalid choice, please try again.")

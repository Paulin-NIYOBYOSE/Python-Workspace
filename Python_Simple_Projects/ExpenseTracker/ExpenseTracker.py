import json

def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)

def add_expense():
    item = input("Enter item name: ")
    cost = float(input("Enter item cost: "))
    expenses.append({"item": item, "cost": cost})
    save_expenses(expenses)
    print(f"Added {item} - ${cost}")

def view_expenses():
    print("Your Expenses:")
    total = 0
    for expense in expenses:
        print(f"{expense['item']}: ${expense['cost']}")
        total += expense["cost"]
    print(f"Total: ${total}")

def delete_expense():
    view_expenses()
    item_to_delete = input("Enter item name to delete: ")
    for expense in expenses:
        if expense["item"] == item_to_delete:
            expenses.remove(expense)
            save_expenses(expenses)
            print(f"Deleted {item_to_delete}")
            return
    print("Item not found")

# Main program loop
expenses = load_expenses()
while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Delete Expense\n4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        delete_expense()
    elif choice == '4':
        break
    else:
        print("Invalid choice")

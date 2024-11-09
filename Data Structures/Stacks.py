# stack_list.py
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Item '{item}' pushed to stack.")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Item '{item}' popped from stack.")
            return item
        else:
            print("Stack is empty.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty.")
            return None

    def is_empty(self):
        return len(self.stack) == 0

# Test the stack
stack = Stack()
stack.push(1)
stack.push(2)
print(f"Top item is: {stack.peek()}")
stack.pop()
print(f"Stack is empty: {stack.is_empty()}")

#Browser history navigation

history = ["Instagram", "Facebook"]
def visit(websiteToVisit):
    history.append(websiteToVisit)

def back():
    if history:
        history.pop()
    else:
        print("The history is empty")

visit("Facebook")
print(history)
back()
print(history)
back()
print(history)
back()
print(history)

#Undo feature
text = []
def add_text(textToAdd):
    text.append(textToAdd)
def undo():
    if text:
        text.pop()
    else:
       print("The text is empty")
add_text("Hello")
add_text("World")
print(text)
undo()
print(text)
undo()
print(text)
undo()
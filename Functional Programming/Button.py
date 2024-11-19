from tkinter import Tk, Button

# Create the main application window
root = Tk()
root.title("Button Example")

# Define a function to handle button click
def on_button_click():
    print("Button clicked!")

# Create a button widget
button = Button(root, text="Click Me", command=on_button_click)
button.pack(pady=20)  # Add the button to the window with some padding

# Run the application
root.mainloop()

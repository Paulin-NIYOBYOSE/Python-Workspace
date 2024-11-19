from tkinter import Tk, Button

#main application window
root = Tk()
root.title("Button Example")
def on_button_click():
    print("Button clicked!")
button = Button(root, text="Click Me", command=on_button_click)
button.pack(pady=20)

# Run the application
root.mainloop()

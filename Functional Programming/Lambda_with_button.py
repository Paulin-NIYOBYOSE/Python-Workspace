from tkinter import Tk, Button

root = Tk()
root.title("Lambda Button Example")
button = Button(root, text="Click Me!", command=lambda:print("clicked with lamnda"))
button.pack(pady=20)
root.mainloop()

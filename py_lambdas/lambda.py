def square(num):
    return num * num

print(square(9))

# these are functionally the same ^ v
square2 = lambda num: num * num
print(square2(9))

# you will use it more often like this
import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="CLICK ME", 
                   fg="red",
                   command=lambda: print("Hello"))




button.pack(side=tk.LEFT)
root.mainloop() 


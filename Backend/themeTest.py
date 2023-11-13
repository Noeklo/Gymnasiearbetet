import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Default Themes")

root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")
root.title("FysiKol")
root.geometry("800x500")


# Set a minsize for the window, and place it in the middle
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))


# w1 = tk.Scale(root, from_=0, to=200, length=200)
# w1.pack(ipadx = 50, ipady = 50)
# w1.place(x=100, y=125)

scale = ttk.Scale(
    from_=100,
    to=0,
    length=200,
)
scale.pack()
# scale.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")


# Run the main loop
root.mainloop()

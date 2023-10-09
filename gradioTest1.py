import tkinter as tk
import ttkbootstrap as ttk

window = tk.Tk()
window.title("FysiKol")
window.geometry("1100x700")

title_label = ttk.Label(window, text="FysiKol", font=("Arial", 25, 'bold'))
title_label.pack()

def convert():
    print("Hello World")

input_frame = ttk.Frame(window)
entry = ttk.Entry(input_frame, width=50)
button = ttk.Button(input_frame, text = 'Convert', command = convert)
entry.pack(side = 'left')
button.pack(side = 'left', padx = 25)
input_frame.pack(pady = 25)

def show_values():
    print (w1.get())

w1 = ttk.Scale(window, from_=0, to=200, length=200, orient=tk.HORIZONTAL)
w1.pack(ipadx = 30, ipady = 0)
slider_button = ttk.Button(window, text='Show', command=show_values).pack()



window.mainloop()

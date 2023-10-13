
from Backend.AnimationWriter import AnimationWriter
import tkinter as tk
import ttkbootstrap as ttk


ani = AnimationWriter()

# def InitTkinter():

window = tk.Tk()
window.title("FysiKol")
window.geometry("1100x700")

title_label = ttk.Label(window, text="FysiKol", font=("Roboto", 35, 'bold'))
title_label.pack()

def convert():
    print("Hello World")

def show_values():
    print (w1.get())

def Start():
    print("Hello World")
    ani.generate_Animation()

# Mass Slider

def update_label(value):
    rounded_value = round(value, 1)
    label.config(text=f"{rounded_value:.1f} KG")
    massa = rounded_value

# import pyglet,tkinter
# pyglet.font.add_file('C:\FysikSim\Backend\Roboto.ttf')

title_label = ttk.Label(window, text="Massa", font=("Roboto", 13, 'bold'))
title_label.pack()
title_label.place(x=100, y=95)

w1 = ttk.Scale(window, from_=0, to=200, length=200, orient=tk.HORIZONTAL)
w1.pack(ipadx = 50, ipady = 50)
w1.place(x=100, y=125)

label = tk.Label(window, text="0 KG")
label.pack()
label.place(x=310, y=120)
w1.bind("<Motion>", lambda e: update_label(w1.get()))

# Velocity Slider

def update_label2(value):
    rounded_value = round(value, 1)
    labelvelocity.config(text=f"{rounded_value:.1f} m/s")
    massa = rounded_value

title_label = ttk.Label(window, text="Hastighet", font=("Roboto", 13, 'bold'))
title_label.pack()
title_label.place(x=100, y=195)

w2 = ttk.Scale(window, from_=0, to=50, length=200, orient=tk.HORIZONTAL)
w2.pack(ipadx = 50, ipady = 50)
w2.place(x=100, y=225)

labelvelocity = tk.Label(window, text="0 m/s")
labelvelocity.pack()
labelvelocity.place(x=310, y=220)
w2.bind("<Motion>", lambda e: update_label2(w2.get()))

# Random Slider

title_label2 = ttk.Label(window, text="Hastighet", font=("Roboto", 13, 'bold'))
title_label2.pack()
title_label2.place(x=100, y=195)

w22 = ttk.Scale(window, from_=0, to=100, length=200, orient=tk.HORIZONTAL)
w22.pack(ipadx = 50, ipady = 50)
w22.place(x=100, y=325)

labelvelocity2 = tk.Label(window, text="0 m/s")
labelvelocity2.pack()
labelvelocity2.place(x=310, y=320)
w22.bind("<Motion>", lambda e: 2)

# Toggle Button

def Simpletoggle():
    
    if toggle_button.config('text')[-1] == 'ON':
        toggle_button.config(text='OFF')
    else:
        toggle_button.config(text='ON')



button_label = ttk.Label(window, text="Elasticitet", font=("Roboto", 13, 'bold'))
button_label.pack()
button_label.place(x=100, y=395)

toggle_button = ttk.Button(text="ON", width=10, command=Simpletoggle)
toggle_button.pack(pady=10)
toggle_button.place(x=100, y=425)

init_button = ttk.Button(text="START", width=10, command=Start)
init_button.pack(pady=10)
init_button.place(x=100, y=525)


window.mainloop()

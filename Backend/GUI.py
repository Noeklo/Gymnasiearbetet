
from AnimationWriter import AnimationWriter
from Canvas import Canvas
import tkinter as tk
import ttkbootstrap as ttk


class GUI:

    def __init__(self,):
        None

    ani = AnimationWriter()
    window = tk.Tk()
    window.title("FysiKol")
    window.geometry("1100x700")

    title_label = ttk.Label(window, text="FysiKol", font=("Roboto", 35, 'bold'))
    title_label.pack()

    def Start(self):
        print('start')
        self.ani.generate_Animation()

    def Stop(self):
        self.ani.stop_Animation()

    # # Mass Slider

    def update_label(self, value):
        self.rounded_value = round(value, 1)
        self.label.config(text=f"{self.rounded_value:.1f} KG")
        self.massa = self.rounded_value


    # # import pyglet,tkinter
    # # pyglet.font.add_file('C:\FysikSim\Roboto.ttf')

    title_label = ttk.Label(window, text="Massa", font=("Roboto", 13, 'bold'))
    title_label.pack()
    title_label.place(x=100, y=95)

    w1 = ttk.Scale(window, from_=0, to=200, length=200, orient=tk.HORIZONTAL)
    w1.pack(ipadx = 50, ipady = 50)
    w1.place(x=100, y=125)

    label = tk.Label(window, text="0 KG")
    label.pack()
    label.place(x=310, y=120)
    w1.bind("<Motion>", lambda self, e: self.update_label(self.w1.get()))

    # Velocity Slider

    def update_label2(self, value):
        self.rounded_value = round(value, 1)
        self.labelvelocity.config(text=f"{self.rounded_value:.1f} m/s")
        self.massa = self.rounded_value

    title_label = ttk.Label(window, text="Hastighet", font=("Roboto", 13, 'bold'))
    title_label.pack()
    title_label.place(x=100, y=195)

    w2 = ttk.Scale(window, from_=0, to=50, length=200, orient=tk.HORIZONTAL)
    w2.pack(ipadx = 50, ipady = 50)
    w2.place(x=100, y=225)

    labelvelocity = tk.Label(window, text="0 m/s")
    labelvelocity.pack()
    labelvelocity.place(x=310, y=220)
    w2.bind("<Motion>", lambda self, e: self.update_label2(self.w2.get()))

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

    def Simpletoggle(self):
        
        if self.toggle_button.config('text')[-1] == 'ON':
            self.toggle_button.config(text='OFF')
        else:
            self.toggle_button.config(text='ON')


    button_label = ttk.Label(window, text="Elasticitet", font=("Roboto", 13, 'bold'))
    button_label.pack()
    button_label.place(x=100, y=395)

    toggle_button = ttk.Button(text="ON", width=10, command=Simpletoggle())
    toggle_button.pack(pady=10)
    toggle_button.place(x=100, y=425)

    stop_button = ttk.Button(text="STOP", width=10, command=Stop())
    stop_button.pack(pady=10)
    stop_button.place(x=100, y=575)

    stop_button = ttk.Button(text="SPARA", width=10, command=Stop())
    stop_button.pack(pady=10)
    stop_button.place(x=225, y=575)

    init_button = ttk.Button(text="START", width=10, command=Start())
    init_button.pack(pady=10)
    init_button.place(x=100, y=525)




GUI1 = GUI()
GUI1.window.mainloop()

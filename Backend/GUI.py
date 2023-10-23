
from AnimationWriter import AnimationWriter
from Canvas import Canvas
import tkinter as tk
# import ttkbootstrap as ttk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)


class GUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("FysiKol")
        self.window.geometry("1100x700")

        self.canvas1 = Canvas((6,6), 60, "Projectile Motion", self.window)
        self.canvas1.tkCanvas.get_tk_widget().place(x=450, y=80)
#        self.ani = AnimationWriter(self.canvas1, self.window, self.velocity)

        style = ttk.Style(self.window)

        # Set the theme with the theme_use method
        style.theme_use('vista')
        
        
        self.massa = 0 
        self.velocity = 0


        title_label = tk.Label(self.window, text="FysiKol", font=("Roboto", 35, 'bold'))
        title_label.pack()

        title_label = tk.Label(self.window, text="Massa", font=("Roboto", 13, 'bold'))
        title_label.pack()
        title_label.place(x=100, y=95)

        w1 = tk.Scale(self.window, from_=0, to=200, length=200, orient=tk.HORIZONTAL)
        w1.pack(ipadx = 50, ipady = 50)
        w1.place(x=100, y=125)

        def update_label(value):
            rounded_value = round(value, 1)
            label.config(text=f"{rounded_value:.1f} KG")
            self.massa = rounded_value


        label = tk.Label(self.window, text="0 KG")
        label.pack()
        label.place(x=310, y=120)
        w1.bind("<Motion>", lambda  e: update_label(w1.get()))

        title_label = tk.Label(self.window, text="Hastighet", font=("Roboto", 13, 'bold'))
        title_label.pack()
        title_label.place(x=100, y=195)

        w2 = tk.Scale(self.window, from_=0, to=50, length=200, orient=tk.HORIZONTAL)
        w2.pack(ipadx = 50, ipady = 50)
        w2.place(x=100, y=225)

        labelvelocity = tk.Label(self.window, text="0 m/s")
        labelvelocity.pack()
        labelvelocity.place(x=310, y=220)
        
        def update_label2(value):
            rounded_value = round(value, 1)
            labelvelocity.config(text=f"{rounded_value:.1f} m/s")
            self.velocity = rounded_value

        w2.bind("<Motion>", lambda  e: update_label2(w2.get()))

        title_label2 = tk.Label(self.window, text="Hastighet", font=("Roboto", 13, 'bold'))
        title_label2.pack()
        title_label2.place(x=100, y=295)

        w22 = tk.Scale(self.window, from_=0, to=100, length=200, orient=tk.HORIZONTAL)
        w22.pack(ipadx = 50, ipady = 50)
        w22.place(x=100, y=325)

        labelvelocity2 = tk.Label(self.window, text="0 m/s")
        labelvelocity2.pack()
        labelvelocity2.place(x=310, y=320)
        w22.bind("<Motion>", lambda e: 2)



        button_label = tk.Label(self.window, text="Elasticitet", font=("Roboto", 13, 'bold'))
        button_label.pack()
        button_label.place(x=100, y=395)

        def Simpletoggle():
    
            if toggle_button.config('text')[-1] == 'ON':
                toggle_button.config(text='OFF')
            else:
                toggle_button.config(text='ON')


        toggle_button = tk.Button(text="ON", width=10, command=Simpletoggle)
        toggle_button.pack(pady=10)
        toggle_button.place(x=100, y=425)



        stop_button = tk.Button(text="STOP", width=10, command=self.Stop)
        stop_button.pack(pady=10)
        stop_button.place(x=100, y=575)

        stop_button = tk.Button(text="SPARA", width=10, command=self.Stop)
        stop_button.pack(pady=10)
        stop_button.place(x=225, y=575)

        init_button = tk.Button(text="START", width=10, command=self.Start)
        init_button.pack(pady=10)
        init_button.place(x=100, y=525)

    def Start(self):
        print('start')
        self.ani = AnimationWriter(self.canvas1, self.window, self.velocity)
        self.ani.generate_Animation()

    def Stop(self):
        self.ani.stop_Animation()




GUI1 = GUI()
GUI1.window.mainloop()

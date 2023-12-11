
from AnimationWriter import AnimationWriter
from Canvas import Canvas
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from PIL import Image, ImageTk

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("FysiKol")
        self.window.geometry("1100x700")
        self.window.tk.call("source", "azure.tcl")
        self.window.tk.call("set_theme", "light")
        self.massa = 0 
        self.velocity = 8
        self.vectors = []
        self.amount = 0


        title_label = ttk.Label(self.window, text="FysiKol", font=("Roboto", 35, 'bold'))
        title_label.pack()

        start_point = None
        strength = 0
        color = None

        def calculate_vector(start, end):
            return end[0] - start[0], end[1] - start[1]

        def calculate_distance(start, end):
            return ((end[0] - start[0])**2 + (end[1] - start[1])**2)**0.5

        def update_strength(distance):
            return distance * 0.01

        def left_click(event):
            global start_point, strength

            start_point = (event.x, event.y)
            strength = 0

        def left_click_hold(event, canvas):
            x, y = event.x, event.y
            print(x,y)
            if (x > 75 and x < 540 and y > 75 and y < 540):
                global start_point, strength
                if self.line_tag:
                    self.canvas1.tkCanvas.get_tk_widget().delete(self.line_tag)
                end_point = (event.x, event.y)
                self.vectors = [start_point, end_point]
                #print(vectors[0], vectors[1])
                distance = calculate_distance(start_point, end_point)
                strength = update_strength(distance)
                #print("Distance:", distance)
                #print("Strength:", strength)
                if strength > 0.5:
                    update_label2(strength * 10)
                
                if strength < 1:
                    self.color = f'#{int(strength * 255):1x}0000'

                self.line_tag = self.canvas1.tkCanvas.get_tk_widget().create_line(start_point[0], start_point[1], end_point[0], end_point[1], fill=self.color, width=2)
        self.line_tag = None
        self.canvas1 = Canvas((6,6), 60, "Projectile Motion", self.window)
        self.canvas1.tkCanvas.get_tk_widget().place(x=450, y=80)
        self.canvas1.tkCanvas.get_tk_widget().bind("<Button-1>", left_click)
        self.canvas1.tkCanvas.get_tk_widget().bind("<B1-Motion>", lambda event: left_click_hold(event, self.canvas1))


        lbl = ttk.Label(self.window, text="O", font=("Roboto", 35, 'bold'))
        lbl.pack()
        lbl.place(x=50, y=100)

        tab_parent = ttk.Notebook(lbl)
        tab1 = ttk.Frame(tab_parent)
        tab2 = ttk.Frame(tab_parent)
        tab_parent.add(tab1, text="Exakt Styrning")
        tab_parent.add(tab2, text="Slumpmässig Styrning")
        tab_parent.pack(ipadx = 75, ipady = 250)


        def update_label(value):
            rounded_value = round(value, 1)
            label.config(text=f"{rounded_value:.1f} KG")
            self.massa = rounded_value

        def update_label2(value):
            rounded_value = round(value, 1)
            labelvelocity.config(text=f"{rounded_value:.1f} m/s")
            self.velocity = rounded_value
            w2.set(self.velocity)

        def Simpletoggle():
            if toggle_button.config('text')[-1] == 'PÅ':
                toggle_button.config(text='AV')
            else:
                toggle_button.config(text='PÅ')






        # INSIDE TAB 1
        title_label = ttk.Label(tab1, text="Massa", font=("Roboto", 13, 'bold'))
        title_label.pack()
        title_label.place(x=50, y=50)

        w1 = ttk.Scale(tab1, from_=0, to=200, length=200, orient=tk.HORIZONTAL)
        w1.pack(ipadx = 50, ipady = 50)
        w1.place(x=50, y=75)


        label = tk.Label(tab1, text="0.0 KG")
        label.pack()
        label.place(x=275, y=70)
        w1.bind("<Motion>", lambda  e: update_label(w1.get()))

        title_label = ttk.Label(tab1, text="Hastighet", font=("Roboto", 13, 'bold'))
        title_label.pack()
        title_label.place(x=50, y=150)

        w2 = ttk.Scale(tab1, from_=0, to=20, length=200, orient=tk.HORIZONTAL)
        w2.set(self.velocity)
        w2.pack(ipadx = 50, ipady = 50)
        w2.place(x=50, y=175)

        labelvelocity = ttk.Label(tab1, text="8.0 m/s")
        labelvelocity.pack()
        labelvelocity.place(x=275, y=170)

        w2.bind("<Motion>", lambda  e: update_label2(w2.get()))

        button_label = ttk.Label(tab1, text="Elasticitet", font=("Roboto", 13, 'bold'))
        button_label.pack()
        button_label.place(x=50, y=250)

        toggle_button = ttk.Button(tab1, text="PÅ", width=10, command=Simpletoggle)
        toggle_button.pack(pady=10)
        toggle_button.place(x=50, y=280)

        init_button = ttk.Button(tab1, text="START", width=10, command=self.Start)
        init_button.pack(pady=10)
        init_button.place(x=50, y=375)

        stop_button = ttk.Button(tab1, text="STOP", width=10, command=self.Stop)
        stop_button.pack(pady=10)
        stop_button.place(x=50, y=425)

        stop_button = ttk.Button(tab1, text="SPARA", width=10, command=self.Stop)
        stop_button.pack(pady=10)
        stop_button.place(x=175, y=425)












        # INSIDE TAB 2




        title_label = ttk.Label(tab2, text="Massa", font=("Roboto", 13, 'bold'))
        title_label.pack()
        title_label.place(x=50, y=50)

        w1 = ttk.Scale(tab2, from_=0, to=200, length=200, orient=tk.HORIZONTAL)
        w1.pack(ipadx = 50, ipady = 50)
        w1.place(x=50, y=75)

        label = tk.Label(tab2, text="0.0 KG")
        label.pack()
        label.place(x=275, y=70)
        w1.bind("<Motion>", lambda  e: update_label(w1.get()))

        title_label = ttk.Label(tab2, text="Hastighet", font=("Roboto", 13, 'bold'))
        title_label.pack()
        title_label.place(x=50, y=150)

        w2 = ttk.Scale(tab2, from_=0, to=20, length=200, orient=tk.HORIZONTAL)
        w2.set(self.velocity)
        w2.pack(ipadx = 50, ipady = 50)
        w2.place(x=50, y=175)

        labelvelocity = ttk.Label(tab2, text="8.0 m/s")
        labelvelocity.pack()
        labelvelocity.place(x=275, y=170)

        w2.bind("<Motion>", lambda  e: update_label2(w2.get()))
        
        button_label = ttk.Label(tab2, text="Elasticitet", font=("Roboto", 13, 'bold'))
        button_label.pack()
        button_label.place(x=50, y=250)


        entry_label = ttk.Label(tab2, text="Antal Objekt", font=("Roboto", 13, 'bold'))
        entry_label.pack()
        entry_label.place(x=200, y=250)
        numeric_entry = ttk.Entry(tab2,  validate="key")
        numeric_entry.pack(pady=10)
        numeric_entry.place(x=200, y=280)


        toggle_button = ttk.Button(tab2, text="PÅ", width=10, command=Simpletoggle)
        toggle_button.pack(pady=10)
        toggle_button.place(x=50, y=280)

        init_button = ttk.Button(tab2, text="START", width=10, command=self.Start)
        init_button.pack(pady=10)
        init_button.place(x=50, y=375)

        stop_button = ttk.Button(tab2, text="STOP", width=10, command=self.Stop)
        stop_button.pack(pady=10)
        stop_button.place(x=50, y=425)

        stop_button = ttk.Button(tab2, text="SPARA", width=10, command=self.Stop)
        stop_button.pack(pady=10)
        stop_button.place(x=175, y=425)












    def Start(self):
        self.ani = AnimationWriter(self.canvas1, self.window)
        self.ani.generate_Spec_Animation(self.vectors, self.velocity)

    def RandomStart(self):
        self.ani = AnimationWriter(self.canvas1, self.vectors, self.window, self.velocity)
        self.ani.generate_Rnd_Animation(self.amount, self.velocity)

    def Stop(self):
        self.ani.stop_Animation()

GUI1 = GUI()
GUI1.window.mainloop()

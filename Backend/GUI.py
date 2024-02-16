
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
        self.window.geometry("1050x600")
        self.window.tk.call("source", "azure.tcl")
        self.window.tk.call("set_theme", "light")
        self.massa = 0 
        self.velocity = 8
        self.vectors = []
        self.count = 0
        self.canvas1 = None
        self.size = 1
        self.time = 0
        self.ani = None



        # self.responsive = 0.5
        # self.window.tk.call('tk', 'scaling', self.responsive)

        # screen_width = self.window.winfo_screenwidth()
        # screen_height = self.window.winfo_screenheight()
        # print(screen_height, screen_width)

        # self.window.bind("<Motion>", lambda  e: print(self.window.winfo_screenheight()))
        # self.window.bind("<Configure>", print(self.window.winfo_screenheight()))
        
        # title_label = ttk.Label(self.window, text="FysiKol", font=("Roboto", 35, 'bold'))
        # title_label.pack() 

        start_point = None
        strength = 0
        color = None



        


        self.line_tag = None
        self.canvas1 = Canvas((6,6), 60, "Projectile Motion", self.window)
        self.canvas1.tkCanvas.get_tk_widget().place(x=450, y=0)
        self.canvas1.tkCanvas.get_tk_widget().bind("<Button-1>", self.left_click)
        self.canvas1.tkCanvas.get_tk_widget().bind("<B1-Motion>", lambda event: self.left_click_hold(event, self.canvas1))

        lbl = ttk.Label(self.window, text="O", font=("Roboto", 35, 'bold'))
        lbl.pack()
        lbl.place(x=50, y=30)

        tab_parent = ttk.Notebook(lbl)
        tab1 = ttk.Frame(tab_parent)
        tab2 = ttk.Frame(tab_parent)
        tab_parent.add(tab1, text="Standard")
        tab_parent.add(tab2, text="Avancerad")
        tab_parent.pack(ipadx = 100, ipady = 250)



        def is_float(value):
            try:
                float(value)
                return True
            except ValueError:
                return False
        

        # INSIDE TAB 1
        title_label = ttk.Label(tab1, text="Massa", font=("Roboto", 13, 'bold'))
        title_label.pack()
        title_label.place(x=50, y=50)

        self.w1 = ttk.Scale(tab1, from_=0, to=200, length=200, orient=tk.HORIZONTAL)
        self.w1.pack(ipadx = 50, ipady = 50)
        self.w1.place(x=50, y=75)

        def on_mass1_change(*args):
            entry_text = entry_var1.get()
            if is_float(entry_text):
                if float(entry_text) > 200.0:
                    entry_var1.set('200')
                    self.massa = 200.0
                self.massa = float(entry_text)
                self.w1.set(self.massa)

        entry_var1 = tk.StringVar()
        entry_var1.trace_add("write",  on_mass1_change)


        self.inputmass = ttk.Entry(tab1, width=4, textvariable=entry_var1)
        self.inputmass.insert(0, "0.0") 
        self.inputmass.pack(pady=10)
        self.inputmass.place(x=275, y=65)
        self.labelw1 = tk.Label(tab1, text="KG")
        self.labelw1.pack()
        self.labelw1.place(x=320, y=70)
        self.w1.bind("<Motion>", lambda  e: self.update_mass1(self.w1.get()))

        title_label = ttk.Label(tab1, text="Hastighet", font=("Roboto", 13, 'bold'))
        title_label.pack()
        title_label.place(x=50, y=125)

        self.w2 = ttk.Scale(tab1, from_=0, to=20, length=200, orient=tk.HORIZONTAL)
        self.w2.set(self.velocity)
        self.w2.pack(ipadx = 50, ipady = 50)
        self.w2.place(x=50, y=150)

        
        def on_vel1_change(*args):
            entry_text = entry_var2.get()
            if is_float(entry_text):
                if float(entry_text) > 20.0:
                    entry_var2.set('20')
                    self.velocity = 20.0
                self.velocity = float(entry_text)
                self.w2.set(self.velocity)


        entry_var2 = tk.StringVar()
        entry_var2.trace_add("write",  on_vel1_change)
        

        self.inputvel = ttk.Entry(tab1, width=4, textvariable=entry_var2)
        self.inputvel.insert(0, "8.0") 
        self.inputvel.pack(pady=10)
        self.inputvel.place(x=275, y=140)
        self.labelvelocityw2 = ttk.Label(tab1, text="m/s")
        self.labelvelocityw2.pack()
        self.labelvelocityw2.place(x=320, y=145)



        self.w2.bind("<Motion>", lambda  e: self.update_vel1(self.w2.get()))

        title_label = ttk.Label(tab1, text="Storlek", font=("Roboto", 13, 'bold'))
        title_label.pack()
        title_label.place(x=50, y=205)

        self.sizeslider = ttk.Scale(tab1, from_=0, to=20, length=200, orient=tk.HORIZONTAL)
        self.sizeslider.set(self.size)
        self.sizeslider.pack(ipadx = 50, ipady = 50)
        self.sizeslider.place(x=50, y=230)

        def on_size_change(*args):
            entry_text = entry_var6.get()
            if is_float(entry_text):
                if float(entry_text) > 20.0:
                    entry_var6.set('20')
                    self.size = 20.0
                self.size = float(entry_text)
                self.sizeslider.set(self.size)

        entry_var6 = tk.StringVar()
        entry_var6.trace_add("write",  on_size_change)

        self.inputsize = ttk.Entry(tab1, width=4, textvariable=entry_var6)
        self.inputsize.insert(0, "8.0") 
        self.inputsize.pack(pady=10)
        self.inputsize.place(x=275, y=220)

        self.labelsize = ttk.Label(tab1, text="m")
        self.labelsize.pack()
        self.labelsize.place(x=320, y=225)

        self.sizeslider.bind("<Motion>", lambda  e: self.update_size1(self.sizeslider.get()))

        button_label = ttk.Label(tab1, text="Elasticitet", font=("Roboto", 13, 'bold'))
        button_label.pack()
        button_label.place(x=50, y=280)

        toggle_button = ttk.Button(tab1, text="PÅ", width=10, command=self.Simpletoggle)
        toggle_button.pack(pady=10)
        toggle_button.place(x=50, y=310)

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

        self.title_label = ttk.Label(tab2, text="Massa", font=("Roboto", 13, 'bold'))
        self.title_label.pack()
        self.title_label.place(x=50, y=50)

        self.w3 = ttk.Scale(tab2, from_=0, to=200, length=200, orient=tk.HORIZONTAL)
        self.w3.pack(ipadx = 50, ipady = 50)
        self.w3.place(x=50, y=75)

        def on_mass2_change(*args):
            entry_text = entry_var3.get()
            if is_float(entry_text):
                if float(entry_text) > 200.0:
                    entry_var3.set('200')
                    self.massa = 200.0
                self.massa = float(entry_text)
                self.w3.set(self.massa)

        entry_var3 = tk.StringVar()
        entry_var3.trace_add("write",  on_mass2_change)

        self.inputmass2 = ttk.Entry(tab2, width=4, textvariable=entry_var3)
        self.inputmass2.insert(0, "0.0") 
        self.inputmass2.pack(pady=10)
        self.inputmass2.place(x=275, y=65)
        self.labelw3 = tk.Label(tab2, text="KG")
        self.labelw3.pack()
        self.labelw3.place(x=320, y=70)
        self.w3.bind("<Motion>", lambda  e: self.update_mass2(self.w3.get()))

        self.title_label = ttk.Label(tab2, text="Hastighet", font=("Roboto", 13, 'bold'))
        self.title_label.pack()
        self.title_label.place(x=50, y=150)

        self.w4 = ttk.Scale(tab2, from_=0, to=20, length=200, orient=tk.HORIZONTAL)
        self.w4.set(self.velocity)
        self.w4.pack(ipadx = 50, ipady = 50)
        self.w4.place(x=50, y=175)



        def on_vel2_change(*args):
            entry_text = entry_var4.get()
            if is_float(entry_text):
                if float(entry_text) > 20.0:
                    entry_var4.set('20')
                    self.velocity = 20.0
                self.velocity = float(entry_text)
                self.w4.set(self.velocity)


        entry_var4 = tk.StringVar()
        entry_var4.trace_add("write",  on_vel2_change)

        self.inputvel2 = ttk.Entry(tab2, width=4,  textvariable=entry_var4)
        self.inputvel2.insert(0, "8.0")
        self.inputvel2.pack(pady=10)
        self.inputvel2.place(x=275, y=165)



        self.labelvelocityw4 = ttk.Label(tab2, text="m/s")
        self.labelvelocityw4.pack()
        self.labelvelocityw4.place(x=320, y=170)

        self.w4.bind("<Motion>", lambda  e: self.update_vel2(self.w4.get()))
        
        self.button_label = ttk.Label(tab2, text="Elasticitet", font=("Roboto", 13, 'bold'))
        self.button_label.pack()
        self.button_label.place(x=50, y=250)


        self.entry_label = ttk.Label(tab2, text="Antal Objekt", font=("Roboto", 13, 'bold'))
        self.entry_label.pack()
        self.entry_label.place(x=175, y=250)
        self.numeric_entry = ttk.Entry(tab2,  validate="key")
        self.numeric_entry.pack(pady=10)
        self.numeric_entry.place(x=175, y=280)

        self.time_label = ttk.Label(tab2, text="Tid i sek", font=("Roboto", 13, 'bold'))
        self.time_label.pack()
        self.time_label.place(x=175, y=325)
        self.time_entry = ttk.Entry(tab2)
        self.time_entry.pack(pady=10)
        self.time_entry.place(x=175, y=350)
        
        self.toggle_button = ttk.Button(tab2, text="PÅ", width=10, command=self.Simpletoggle)
        self.toggle_button.pack(pady=10)
        self.toggle_button.place(x=50, y=280)

        init_button = ttk.Button(tab2, text="START", width=10, command=self.RandomStart)
        init_button.pack(pady=10)
        init_button.place(x=50, y=375)

        stop_button = ttk.Button(tab2, text="STOP", width=10, command=self.Stop)
        stop_button.pack(pady=10)
        stop_button.place(x=50, y=425)

        stop_button = ttk.Button(tab2, text="SPARA", width=10, command=self.Stop)
        stop_button.pack(pady=10)
        stop_button.place(x=175, y=425)



    def calculate_vector(self, start, end):
        return end[0] - start[0], end[1] - start[1]

    def calculate_distance(self, start, end):
        return ((end[0] - start[0])**2 + (end[1] - start[1])**2)**0.5

    def update_strength(self, distance):
        return distance * 0.01

    def left_click(self, event):
        global start_point, strength

        start_point = (event.x, event.y)
        strength = 0

    def left_click_hold(self, event, canvas):
        x, y = event.x, event.y
        if (x > 75 and x < 540 and y > 75 and y < 540):
            global start_point, strength
            if self.line_tag:
                self.canvas1.tkCanvas.get_tk_widget().delete(self.line_tag)
            end_point = (event.x, event.y)
            self.vectors = [start_point, end_point]
            distance = self.calculate_distance(start_point, end_point)
            strength = self.update_strength(distance)
            self.update_vel1(strength * 10)
            if strength < 1 and strength > 0.5:
                self.color = f'#{int(strength * 255):1x}0000'
            else:
                if strength > 1:
                    self.color = f'#ff0000'
                elif strength < 0.3:
                    self.color = f'#2b0202'

            self.line_tag = self.canvas1.tkCanvas.get_tk_widget().create_line(start_point[0], start_point[1], end_point[0], end_point[1], fill=self.color, width=2)

    def update_size1(self, value):
        rounded_value = round(value, 1)
        # self.labelsize.config(text=f"{rounded_value:.1f} m")
        self.inputsize.delete(0, 'end')
        self.inputsize.insert(-1, f"{rounded_value:.1f}")
        self.size = rounded_value
        self.sizeslider.set(self.size)


    def update_mass1(self, value):
        rounded_value = round(value, 1)
        # self.labelw1.config(text=f"{rounded_value:.1f} KG")
        self.inputmass.delete(0, 'end')
        self.inputmass.insert(-1, f"{rounded_value:.1f}")
        self.massa = rounded_value
        self.w1.set(self.massa)

    def update_mass2(self, value):
        rounded_value = round(value, 1)
        # self.labelw3.config(text=f"{rounded_value:.1f} KG")
        self.inputmass2.delete(0, 'end')
        self.inputmass2.insert(-1, f"{rounded_value:.1f}")
        self.massa = rounded_value
        self.w3.set(self.massa)

    def update_vel1(self, value):
        rounded_value = round(value, 1)
        if rounded_value < 21.0:
            if rounded_value > 20.0:
                rounded_value = 20.0
            # self.labelvelocityw2.config(text=f"{rounded_value:.1f} m/s")
            self.inputvel.delete(0, 'end')
            self.inputvel.insert(-1, f"{rounded_value:.1f}")
            self.velocity = rounded_value
            self.w2.set(self.velocity)

    def update_vel2(self, value):
        rounded_value = round(value, 1)
        if rounded_value < 21.0:
            if rounded_value > 20.0:
                rounded_value = 20.0
            self.inputvel2.delete(0, 'end')
            self.inputvel2.insert(-1, f"{rounded_value:.1f}")
            self.velocity = rounded_value
            self.w4.set(self.velocity)


    def Simpletoggle(self):
        if self.toggle_button.config('text')[-1] == 'PÅ':
            self.toggle_button.config(text='AV')
        else:
            self.toggle_button.config(text='PÅ')

    def Start(self):
        if self.ani != None:
            self.Stop()
        self.ani = AnimationWriter(self.canvas1, self.window)
        self.ani.generate_Spec_Animation(self.vectors, self.velocity)
        self.canvas1.tkCanvas.get_tk_widget().delete(self.line_tag)        

    def RandomStart(self):
        if self.ani != None:
            self.Stop()
        self.count = int(self.numeric_entry.get())
        self.time = int(self.time_entry.get())
        self.ani = AnimationWriter(self.canvas1, self.window)
        print(self.velocity)
        self.ani.generate_Rnd_Animation(self.count, self.velocity, 0.1, 1, self.time)

    def Stop(self):
        self.ani.stop_Animation()
        self.canvas1.tkCanvas.get_tk_widget().destroy()
        self.canvas1 = Canvas((6,6), 60, "Projectile Motion", self.window)
        self.canvas1.tkCanvas.get_tk_widget().place(x=450, y=0)
        self.canvas1.tkCanvas.get_tk_widget().bind("<Button-1>", self.left_click)
        self.canvas1.tkCanvas.get_tk_widget().bind("<B1-Motion>", lambda event: self.left_click_hold(event, self.canvas1))





GUI1 = GUI()
GUI1.window.mainloop()

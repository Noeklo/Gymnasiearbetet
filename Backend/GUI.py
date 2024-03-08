
from AnimationWriter import AnimationWriter
from Canvas import Canvas
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from PIL import Image, ImageTk
from win32api import GetSystemMetrics
import math


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
        self.size = 0.1
        self.time = 0
        self.ani = None
        self.standard_deviation_velocity = 0
        self.standard_deviation_mass = 0
        self.standard_deviation_radius = 0
        self.elasticity = True

        self.responsive = 1
        self.screens_width = self.window.winfo_screenwidth()
        self.window.resizable(False, False)
        #print("Width =", GetSystemMetrics(0))
        #print("Height =", GetSystemMetrics(1))
        #self.screens_width = GetSystemMetrics(0)
        
        # if self.screens_width < 1920:
        #     self.responsive = 0.5
        #     w = 1050*0.5
        #     h = 600*0.5
        #     self.window.geometry(f"{int(w)}x{int(h)}")
        if self.screens_width < 1920:
            self.responsive = 1
            w = 1050*1
            h = 600*1
            self.window.geometry(f"{int(w)}x{int(h)}")
        elif self.screens_width < 2560:
            self.responsive = 4/3
            w = 1050*4/3
            h = 600*4/3
            self.window.geometry(f"{int(w)}x{int(h)}")
        elif self.screens_width < 3840:
            self.responsive = 2
            w = 1050*2
            h = 600*2
            self.window.geometry(f"{int(w)}x{int(h)}")

        def normal_round(n):
            if n - math.floor(n) < 0.5:
                return math.floor(n)
            return math.ceil(n)
        


        self.line_tag = None
        self.canvas1 = Canvas((self.responsive*6,self.responsive*6), 60, "Projectile Motion", self.window)
        self.canvas1.tkCanvas.get_tk_widget().place(x=self.responsive*450, y=self.responsive*0)
        self.canvas1.tkCanvas.get_tk_widget().bind("<Button-1>", self.left_click)
        self.canvas1.tkCanvas.get_tk_widget().bind("<B1-Motion>", lambda event: self.left_click_hold(event, self.canvas1))

        lbl = ttk.Label(self.window, text="O", font=("Roboto", 35, 'bold'))
        lbl.pack()
        lbl.place(x=self.responsive*50, y=self.responsive*30)

        tab_parent = ttk.Notebook(lbl)
        tab1 = ttk.Frame(tab_parent, width=self.responsive*400, heigh=self.responsive*500)
        tab2 = ttk.Frame(tab_parent, width=self.responsive*400, heigh=self.responsive*500)
        tab_parent.add(tab1, text="Standard")
        tab_parent.add(tab2, text="Avancerad")
        # tab_parent.pack(ipadx=self.responsive* 100 - 50*self.responsive, ipady=self.responsive* 250 - 30*self.responsive)
        tab_parent.pack()

        def is_float(value):
            try:
                float(value)
                return True
            except ValueError:
                return False
        

        # INSIDE TAB 1
        title_label = ttk.Label(tab1, text="Massa", font=("Roboto", normal_round(13*self.responsive), 'bold'))
        title_label.pack()
        title_label.place(x=self.responsive*50, y=self.responsive*50)

        self.w1 = ttk.Scale(tab1, from_=1, to=200, length=self.responsive*200, orient=tk.HORIZONTAL)
        self.w1.pack()
        self.w1.place(x=self.responsive*50, y=self.responsive*75)

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

        self.inputmass = ttk.Entry(tab1, width=normal_round(self.responsive*4), textvariable=entry_var1, font=("Roboto", normal_round(13*self.responsive)))
        self.inputmass.insert(0, "1.0") 
        self.inputmass.pack()
        self.inputmass.place(x=self.responsive*275, y=self.responsive*65)
        self.labelw1 = tk.Label(tab1, text="KG", font=("Roboto", normal_round(13*self.responsive)))
        self.labelw1.pack()
        self.labelw1.place(x=self.responsive*330, y=self.responsive*70)
        self.w1.bind("<Motion>", lambda  e: self.update_mass1(self.w1.get()))

        title_label = ttk.Label(tab1, text="Hastighet", font=("Roboto", normal_round(13*self.responsive), 'bold'))
        title_label.pack()
        title_label.place(x=self.responsive*50, y=self.responsive*125)

        self.w2 = ttk.Scale(tab1, from_=0, to=20, length=self.responsive*200, orient=tk.HORIZONTAL)
        self.w2.set(self.velocity)
        self.w2.pack()
        self.w2.place(x=self.responsive*50, y=self.responsive*150)

        
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
        

        self.inputvel = ttk.Entry(tab1, width=normal_round(self.responsive*4), textvariable=entry_var2, font=("Roboto", normal_round(13*self.responsive)))
        self.inputvel.insert(0, "8.0") 
        self.inputvel.pack(pady=self.responsive*10)
        self.inputvel.place(x=self.responsive*275, y=self.responsive*140)
        self.labelvelocityw2 = ttk.Label(tab1, text="m/s", font=("Roboto", normal_round(13*self.responsive)))
        self.labelvelocityw2.pack()
        self.labelvelocityw2.place(x=self.responsive*330, y=self.responsive*145)



        self.w2.bind("<Motion>", lambda  e: self.update_vel1(self.w2.get()))

        title_label = ttk.Label(tab1, text="Storlek", font=("Roboto", normal_round(13*self.responsive), 'bold'))
        title_label.pack()
        title_label.place(x=self.responsive*50, y=self.responsive*205)

        self.sizeslider = ttk.Scale(tab1, from_=1, to=5, length=self.responsive*200, orient=tk.HORIZONTAL)
        self.sizeslider.set(self.size*10)
        self.sizeslider.pack()
        self.sizeslider.place(x=self.responsive*50, y=self.responsive*230)

        def on_size_change(*args):
            entry_text = entry_var6.get()
            if is_float(entry_text):
                if float(entry_text) > 20.0:
                    entry_var6.set('20')
                    self.size = 20.0
                self.size = float(entry_text)/10
                self.sizeslider.set(self.size*10)

        entry_var6 = tk.StringVar()
        entry_var6.trace_add("write",  on_size_change)

        self.inputsize = ttk.Entry(tab1, width=normal_round(self.responsive*4), textvariable=entry_var6, font=("Roboto", normal_round(13*self.responsive)))
        self.inputsize.insert(0, "0.1")
        self.inputsize.pack(pady=self.responsive*10)
        self.inputsize.place(x=self.responsive*275, y=self.responsive*220)

        self.labelsize = ttk.Label(tab1, text="m", font=("Roboto", normal_round(13*self.responsive)))
        self.labelsize.pack()
        self.labelsize.place(x=self.responsive*330, y=self.responsive*225)

        self.sizeslider.bind("<Motion>", lambda  e: self.update_size1(self.sizeslider.get()/10))

        button_label = ttk.Label(tab1, text="Elasticitet", font=("Roboto", normal_round(13*self.responsive)))
        button_label.pack()
        button_label.place(x=self.responsive*50, y=self.responsive*280)

        toggle_button = tk.Button(tab1, text="PÅ", width=normal_round(self.responsive*10), font=("Roboto", normal_round(13*self.responsive)), command=self.Simpletoggle)
        toggle_button.pack()
        toggle_button.place(x=self.responsive*50, y=self.responsive*310)

        init_button = tk.Button(tab1, text="START", width=normal_round(self.responsive*10), font=("Roboto", normal_round(13*self.responsive)), command=self.Start)

        init_button.pack()
        # init_button.pack(pady=self.responsive*10)
        init_button.place(x=self.responsive*50, y=self.responsive*375)

        stop_button = tk.Button(tab1, text="STOP", width=normal_round(self.responsive*10), font=("Roboto", normal_round(13*self.responsive)), command=self.Stop)
        # stop_button.pack(pady=self.responsive*10)
        stop_button.place(x=self.responsive*50, y=self.responsive*425)

        # stop_button = ttk.Button(tab1, text="SPARA", width=self.responsive*10, command=self.Stop)
        # stop_button.pack(pady=self.responsive*10)
        # stop_button.place(x=self.responsive*175, y=self.responsive*425)






        # INSIDE TAB 2

        self.sigma = ttk.Label(tab2, text="σ", font=("Roboto", normal_round(self.responsive*18)))
        self.sigma.pack()
        self.sigma.place(x=self.responsive*342, y=self.responsive*35)

        self.title_label = ttk.Label(tab2, text="Massa", font=("Roboto", normal_round(self.responsive*13), 'bold'))
        self.title_label.pack()
        self.title_label.place(x=self.responsive*50, y=self.responsive*50)

        self.w3 = ttk.Scale(tab2, from_=1, to=200, length=self.responsive*150, orient=tk.HORIZONTAL)
        self.w3.pack(ipadx=self.responsive* 50, ipady=self.responsive* 50)
        self.w3.place(x=self.responsive*50, y=self.responsive*75)

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

        self.standardavikelse = ttk.Entry(tab2, width=normal_round(self.responsive*4), font=("Roboto", normal_round(13*self.responsive)))
        self.standardavikelse.insert(0, "0")
        self.standardavikelse.pack(pady=self.responsive*10)
        self.standardavikelse.place(x=self.responsive*325, y=self.responsive*65)
        
        self.inputmass2 = ttk.Entry(tab2, width=normal_round(self.responsive*4), textvariable=entry_var3, font=("Roboto", normal_round(13*self.responsive)))
        self.inputmass2.insert(0, "1.0") 
        self.inputmass2.pack(pady=self.responsive*10)
        self.inputmass2.place(x=self.responsive*225, y=self.responsive*65)

        self.labelw3 = tk.Label(tab2, text="KG", font=("Roboto", normal_round(13*self.responsive)))
        self.labelw3.pack()
        self.labelw3.place(x=self.responsive*280, y=self.responsive*70)
        self.w3.bind("<Motion>", lambda  e: self.update_mass2(self.w3.get()))

        self.title_label = ttk.Label(tab2, text="Hastighet", font=("Roboto", normal_round(self.responsive*13), 'bold'))
        self.title_label.pack()
        self.title_label.place(x=self.responsive*50, y=self.responsive*120)

        self.w4 = ttk.Scale(tab2, from_=0, to=20, length=self.responsive*150, orient=tk.HORIZONTAL)
        self.w4.set(self.velocity)
        self.w4.pack(ipadx=self.responsive* 50, ipady=self.responsive*50)
        self.w4.place(x=self.responsive*50, y=self.responsive*145)



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

        self.inputvel2 = ttk.Entry(tab2, width=normal_round(self.responsive*4),  textvariable=entry_var4, font=("Roboto", normal_round(13*self.responsive)))
        self.inputvel2.insert(0, "8.0")
        self.inputvel2.pack(pady=self.responsive*10)
        self.inputvel2.place(x=self.responsive*225, y=self.responsive*135)

            

        self.labelvelocityw4 = ttk.Label(tab2, text="m/s", font=("Roboto", normal_round(self.responsive*13)))
        self.labelvelocityw4.pack()
        self.labelvelocityw4.place(x=self.responsive*280, y=self.responsive*140)

        self.w4.bind("<Motion>", lambda  e: self.update_vel2(self.w4.get()))

        self.standardavikelse2 = ttk.Entry(tab2, width=normal_round(self.responsive*4), font=("Roboto", normal_round(13*self.responsive)))
        self.standardavikelse2.insert(0, "0")
        self.standardavikelse2.pack(pady=self.responsive*10)
        self.standardavikelse2.place(x=self.responsive*325, y=self.responsive*135)

        title_label = ttk.Label(tab2, text="Storlek", font=("Roboto", normal_round(13*self.responsive), 'bold'))
        title_label.pack()
        title_label.place(x=self.responsive*50, y=self.responsive*190)

        self.sizeslider2 = ttk.Scale(tab2, from_=1, to=5, length=self.responsive*150, orient=tk.HORIZONTAL)
        self.sizeslider2.set(self.size)
        self.sizeslider2.pack()
        self.sizeslider2.place(x=self.responsive*50, y=self.responsive*215)

        def on_size_change2(*args):
            entry_text = entry_var7.get()
            if is_float(entry_text):
                self.size = float(entry_text)/10
                self.sizeslider2.set(self.size*10)

        entry_var7 = tk.StringVar()
        entry_var7.trace_add("write",  on_size_change2)

        self.inputsize2 = ttk.Entry(tab2, width=normal_round(self.responsive*4), textvariable=entry_var7, font=("Roboto", normal_round(13*self.responsive)))
        self.inputsize2.insert(0, "0.1") 
        self.inputsize2.pack(pady=self.responsive*10)
        self.inputsize2.place(x=self.responsive*225, y=self.responsive*205)

        self.labelsize2 = ttk.Label(tab2, text="m", font=("Roboto", normal_round(13*self.responsive)))
        self.labelsize2.pack()
        self.labelsize2.place(x=self.responsive*280, y=self.responsive*210)

        self.standardavikelse3 = ttk.Entry(tab2, width=normal_round(self.responsive*4), font=("Roboto", normal_round(13*self.responsive)))
        self.standardavikelse3.insert(0, "0")
        self.standardavikelse3.pack(pady=self.responsive*10)
        self.standardavikelse3.place(x=self.responsive*325, y=self.responsive*205)

        
        self.sizeslider2.bind("<Motion>", lambda  e: self.update_size2(self.sizeslider2.get()/10))

        self.button_label = ttk.Label(tab2, text="Elasticitet", font=("Roboto", normal_round(self.responsive*13), 'bold'))
        self.button_label.pack()
        self.button_label.place(x=self.responsive*50, y=self.responsive*250)


        self.entry_label = ttk.Label(tab2, text="Antal Objekt", font=("Roboto", normal_round(self.responsive*13), 'bold'))
        self.entry_label.pack()
        self.entry_label.place(x=self.responsive*175, y=self.responsive*250)
        self.numeric_entry = ttk.Entry(tab2,  validate="key", width=normal_round(self.responsive*15), font=("Roboto", normal_round(13*self.responsive)))
        self.numeric_entry.pack(pady=self.responsive*10)
        self.numeric_entry.place(x=self.responsive*175, y=self.responsive*280)

        self.time_label = ttk.Label(tab2, text="Tid i sek", font=("Roboto", normal_round(self.responsive*13), 'bold'))
        self.time_label.pack()
        self.time_label.place(x=self.responsive*175, y=self.responsive*335)
        self.time_entry = ttk.Entry(tab2, width=normal_round(self.responsive*15), font=("Roboto", normal_round(13*self.responsive)))
        self.time_entry.pack(pady=self.responsive*10)
        self.time_entry.place(x=self.responsive*175, y=self.responsive*360)
        
        self.toggle_button = tk.Button(tab2, text="PÅ", width=normal_round(self.responsive*10), command=self.Simpletoggle, font=("Roboto", normal_round(13*self.responsive)))
        self.toggle_button.pack(pady=self.responsive*10)
        self.toggle_button.place(x=self.responsive*50, y=self.responsive*280)

        init_button = tk.Button(tab2, text="START", width=normal_round(self.responsive*10), command=self.RandomStart, font=("Roboto", normal_round(13*self.responsive)))
        init_button.pack(pady=self.responsive*10)
        init_button.place(x=self.responsive*50, y=self.responsive*375)

        stop_button = tk.Button(tab2, text="STOP", width=normal_round(self.responsive*10), command=self.Stop, font=("Roboto", normal_round(13*self.responsive)))
        stop_button.pack(pady=self.responsive*10)
        stop_button.place(x=self.responsive*50, y=self.responsive*425)

        # stop_button = ttk.Button(tab2, text="SPARA", width=self.responsive*10, command=self.Stop)
        # stop_button.pack(pady=self.responsive*10)
        # stop_button.place(x=self.responsive*175, y=self.responsive*425)



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

            self.line_tag = self.canvas1.tkCanvas.get_tk_widget().create_line(start_point[0], start_point[1], end_point[0], end_point[1], fill=self.color, width=self.responsive*2)

    def update_size1(self, value):
        rounded_value = round(value, 1)
        # self.labelsize.config(text=f"{rounded_value:.1f} m")
        self.inputsize.delete(0, 'end')
        self.inputsize.insert(-1, f"{rounded_value:.1f}")
        self.size = rounded_value
        self.sizeslider.set(self.size*10)

    def update_size2(self, value):
        rounded_value = round(value, 1)
        # self.labelsize.config(text=f"{rounded_value:.1f} m")
        self.inputsize2.delete(0, 'end')
        self.inputsize2.insert(-1, f"{rounded_value:.1f}")
        self.size = rounded_value
        self.sizeslider2.set(self.size*10)


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
            self.elasticity = False
        else:
            self.toggle_button.config(text='PÅ')
            self.elasticity = True

    def Start(self):
        if self.ani != None:
            self.Stop()
        try:
            self.ani = AnimationWriter(self.canvas1, self.window)
            self.ani.generate_Spec_Animation(self.vectors, self.velocity)
            self.canvas1.tkCanvas.get_tk_widget().delete(self.line_tag)        
        except IndexError: 
            print("Vektor Saknas!")
        except Exception as e:
            print(e)
            
    def RandomStart(self):
        if self.ani != None:
            self.Stop()
        try:
            self.count = int(self.numeric_entry.get())
            self.time = int(self.time_entry.get())
        except ValueError:
            print("Infogade alternativ måste vare heltal!")
        except Exception as e:
            print(e)
        else:
            self.standard_deviation_mass = int(self.standardavikelse.get())
            self.standard_deviation_velocity = int(self.standardavikelse2.get())
            self.standard_deviation_radius = float(self.standardavikelse3.get())
            self.ani = AnimationWriter(self.canvas1, self.window)
            self.ani.generate_Rnd_Animation(
                self.count, 
                self.velocity, 
                self.size, 
                1, 
                self.time, 
                self.standard_deviation_velocity, 
                self.standard_deviation_mass, 
                self.standard_deviation_radius,
                self.elasticity
            )

    def Stop(self):
        self.ani.stop_Animation()
        self.canvas1.tkCanvas.get_tk_widget().destroy()
        self.canvas1 = Canvas((self.responsive*6,self.responsive*6), 60, "Projectile Motion", self.window)
        self.canvas1.tkCanvas.get_tk_widget().place(x=self.responsive*450, y=self.responsive*0)
        self.canvas1.tkCanvas.get_tk_widget().bind("<Button-1>", self.left_click)
        self.canvas1.tkCanvas.get_tk_widget().bind("<B1-Motion>", lambda event: self.left_click_hold(event, self.canvas1))
    




GUI1 = GUI()
GUI1.window.mainloop()

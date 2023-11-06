from AnimationWriter import AnimationWriter
from tkinter import *
from Canvas import Canvas
import time

#ani = AnimationWriter()
#
#ani.generate_Animation()

window = Tk() 

canvas1 = Canvas((6,6), 60, "Projectile Motion", window)
  
ani = AnimationWriter(canvas1, window)
# setting the title  
window.title('Plotting in Tkinter') 
  
# dimensions of the main window 
window.geometry("500x500") 
  
# button that displays the plot 
plot_button = Button(master = window,  
                     command = ani.generate_Animation(), 
                     height = 2,  
                     width = 10, 
                     text = "Plot") 
  
# place the button  
# in main windows
plot_button.pack() 
  
# run the gui 
window.mainloop() 
time.sleep(5)

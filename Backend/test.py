from AnimationWriter import AnimationWriter
from tkinter import *
import matplotlib.pyplot as plt
from Canvas import Canvas

canvas1 = Canvas((6,6), 60, "Projectile Motion")
ani = AnimationWriter(canvas1)
ani.generate_Animation()
plt.show(block=False)


#window = Tk() 
#  
#ani = AnimationWriter(window)
## setting the title  
#window.title('Plotting in Tkinter') 
#  
## dimensions of the main window 
#window.geometry("500x500") 
#  
## button that displays the plot 
#plot_button = Button(master = window,  
#                     command = ani.generate_Animation(), 
#                     height = 2,  
#                     width = 10, 
#                     text = "Plot") 
#  
## place the button  
## in main windows
#plot_button.pack() 
#  
## run the gui 
#window.mainloop() 
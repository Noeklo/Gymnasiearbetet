from AnimationWriter import AnimationWriter
from tkinter import *


ani = AnimationWriter()

ani.generate_Animation()

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
## in main window 
#plot_button.pack() 
#  
## run the gui 
#window.mainloop() 
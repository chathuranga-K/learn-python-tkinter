from tkinter import *

# Widgets - GUI elements: buttons, textboxes, labels, images
# Windows - serves as a container to hold or contain these widgets

window = Tk() # instantiate an instance of a window
window.geometry("900x600") # set Width & Length of the window
window.title("GUI Template") # set window title

# change background color
window.configure(background="black") # set background color using 'color names'
window.configure(background="#5cfcff") # set background color using 'hex value'

# Create a title icon
icon = PhotoImage(file ='Images/laptop-coding.png') # convert 'png' to a photoImage format
window.iconphoto(True, icon) # set image as the window icon

window.mainloop() # place window on computer screen

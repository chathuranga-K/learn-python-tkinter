from tkinter import *

window = Tk() # instantiate an instance of a window
window.geometry('500x400') # set Width & Length of the window
window.title('Count Calculator') # set window title

# create & initialize variable
count = 0
# create a simple function
def count_digit():
    global count
    count+=1
    count_label.config(text=count) # update the count variable
    popupText.pack() # as return prompts the popup Text

# ---------- BUTTON ----------
# Button - Click me
clickButton = Button(
    window,# locate the button
    text = "Click me",
    font=('Arial', 48 , 'bold'), # customize font style (font, size, style)
    background='red', # button background
    foreground='white', # font color
    activebackground='green', # active button background
    activeforeground='black', # active font color
    command = count_digit, # set command of button to be functioned
    state=ACTIVE, # disable or enable button functionality (ACTIVE/DISABLED)

    )
clickButton.pack(pady=50)

# ---------- LABEL ----------
# Label - Count
count_label = Label(
    window, # locate the label
    text = count, # set default text as '0'
    font=('Arial', 50)
    )
count_label.pack(pady=5) # add label to the window

# Label -  Pop Up Text
popupText = Label(
    window,
    text = "Congratulations! You discovered a Button",
    font=('Arial', 16),
    foreground='red', # font color (foreground color/fg color)
    )
popupText.pack() # add button to the window

window.mainloop() # place window on computer screen
from tkinter import *

# display whether if the user agree or not
def display():
    # check switch values are on or not
    if switch.get():
        print("User agree to Terms and Conditions")
    else: print("User did not agree to Terms and Conditions")

window = Tk()
window.title("User Agreement") # window title
switch = BooleanVar() # initialize String variable (StringVar/ IntVar/ BooleanVar)
# convert PNG to a PhotoImage
agree_icon =  PhotoImage(file ='../Images/agree-icon.png')

# Check Button - tick/untick
check_button = Checkbutton(
    window,
    text="I agree to Terms and Conditions",
    variable = switch, # initialize a variable
    onvalue=True, # marked value
    offvalue=False, # unmarked value
    font=("Arial", 25),
    foreground='#00FF00', # font color
    background = 'black', # background color
    activeforeground = '#00FF00', # active font color
    activebackground = 'black',
    command = display,
    padx = 25,
    pady = 10,
    image = agree_icon, # add image
    compound = "left", # position image to left
)
check_button.pack()
window.mainloop()
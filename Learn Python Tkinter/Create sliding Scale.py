from tkinter import *

def submit():
    print(f"Temperature is: {scale.get()} degree Celsius")

window = Tk()

# high temperature icon
high_temperature_icon = PhotoImage(file = "temperature-high.png")
high_temp = Label(window,
                 image=high_temperature_icon)
high_temp.pack()

# Scale
scale = Scale(
    window,
    from_=100, # start value
    to=0, # end value
    length=600,
    width=10,
    highlightcolor="yellow",
    orient=VERTICAL, # orientation of scale (VERTICAL/ HORIZONTAL)
    font = ("Consolas", 20),
    tickinterval = 10, # adds numeric indicators in each sections
    showvalue = True, # hide current value (TRUE/FALSE)
    resolution = 5, # increment of slider
    relief = SUNKEN,
    troughcolor = "red", # slider color
    foreground = "black", # text color
    background = "white", # scale background color
)
scale.set(55)
# formula to set current value of slider as 0.5
# scale.set(((scale['from']-scale['to'])/2) + scale['to'])
scale.pack()

# low temperature icon
low_temperature_icon = PhotoImage(file = "temperature-low.png")
low_temp = Label(window,
                 image=low_temperature_icon)
low_temp.pack()


# Submit Button
submit_button = Button(
    window,
    text="Submit",
    font=("Arial", 15),
    width=11,
    command=submit
)
submit_button.pack()

window.mainloop()
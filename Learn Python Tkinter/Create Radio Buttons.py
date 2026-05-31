# radio button = similar to checkbox, but you can only select one from a group

# import all items from tkinter
from tkinter import *
# create & initialize a list
food = ["Pizza", "Hamburger", "Hotdog"]


window = Tk()
window.configure(background = "black") # set window color as black

# ---------- function ----------
def order():
    if item.get() == 0:
        print("You ordered Pizza!")
    elif item.get() == 1:
        print("You ordered Hamburger!")
    elif item.get() == 2:
        print("You ordered Hotdog!")
    else:print('Opps somthing went wrong! try again')
# convert PNG to PhotoImage format
pizzaImage = PhotoImage(file ="../Images/pizza.png")
hamburgerImage = PhotoImage(file ="../Images/hamburger.png")
hotdogImage = PhotoImage(file ="../Images/hot-dog.png")

# create a list for images
foodImages = [pizzaImage, hamburgerImage, hotdogImage]
item = IntVar() # initialize variable as Integer for radio_button

# use for loop to irritate through the list
for index in range(len(food)):
    radio_button = Radiobutton(
        window,
        text = food[index], # adds text to radio buttons
        value = index, # groups radiobuttons together (if they share the same variable)
        variable = item, # assigns each other radio buttons a different value
        image = foodImages[index], # add images to radio button
        compound = "left", # adds image to the left side of text
        indicatoron = FALSE, # eliminates circle indicators (TRUE/ FALSE)
        command = order # set command of radio button

    )
    radio_button.configure(
        font=("Impact", 30),
        background = "black", # background color
        foreground = "#00FF00", # font color
        activebackground = "black", # active background color
        activeforeground = "#00FF00", # active font color
        width=300, # sets width of radio buttons
        padx = 40, # adds padding on x-axis
    )
    # anchor radio buttons to the west
    radio_button.pack(anchor = 'w') # anchor must be n, ne, e, se, s, sw, w, nw, or center

window.mainloop() # display window
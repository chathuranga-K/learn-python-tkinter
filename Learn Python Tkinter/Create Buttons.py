from tkinter import *

# variables
count=0

# function that displays when clicked the button
def click_function():
    global count
    count+=1
    print(count)

window = Tk()
window.geometry("240x190")
window.title("Like Count")

# Image - like button
likeButton = PhotoImage(file="Images//love-circled.png")

# Button - click me
button = Button(window,
                text="Click me",
                font=("Comic Sans", 30, 'bold'),
                command=click_function,
                foreground="#ffffff", # font color
                background="#000000", # button color
                activeforeground="#ffffff", # clicked font color
                activebackground="#000000", # clicked button color
                state=ACTIVE, # Set button functionality (ACTIVE/DISABLED)
                image = likeButton,
                compound="top")
button.pack()

window.mainloop()

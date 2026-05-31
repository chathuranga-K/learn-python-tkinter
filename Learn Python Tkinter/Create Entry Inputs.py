# entry widget -> textbox that accepts a single line of user input

# from tkinter import all packages
from tkinter import *

window = Tk()

# print Entry text in cmd
def submit():
    username = entry.get() # get Entry text as String
    print("Hello", username)
    entry.config(state=DISABLED) # disable entry functionability
    submit_button.config(state=DISABLED) # disable submit button functionality

# removes the entire typed text in Entry
def delete():
    entry.delete(0, END)

# removes the last character of Entry
def backspace():
    entry.delete(len(entry.get())-1, END) # get length of Entry & substitute by 1

entry = Entry(
    window,
    font=("Arial", 50),
    foreground="#00FF00", # set green hex value as background color
    background="black", # set black as foreground color
    show = '*' # replace entry text (hide user input in Entry)
)
entry.insert(0, 'Spongebob') # set default text placeholder
entry.pack(side = "left")

# Submit Button
submit_button = Button(
    window,
    text = "Submit",
    font=("Arial", 12),
    command=submit # set command
)
submit_button.pack(side = "right")

# Delete Button
delete_button = Button(
    window,
    text = "Delete",
    font=("Arial", 12),
    command=delete # set command
)
delete_button.pack(side="right")

# Backspace Button
backspace_button = Button(
    window,
    font = ("Arial", 12),
    text = "Backspace",
    command = backspace # set command
)
backspace_button.pack(side="right")

window.mainloop() # display window
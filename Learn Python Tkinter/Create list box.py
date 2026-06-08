# listbox = A listing of selectable text items within a container

# import all tkinter packages
from tkinter import *

# ---------- functions ----------
# send select items from menu
def submit():
    food = [] # create empty list to store selected items

    # irritate through selected items in listbox
    for items in listbox.curselection():
        food.insert(items, listbox.get(items)) # insert each item into list

    print(f"You ordered:")
    # irritate through items in list
    for items in food:
        print(items) # print each item

    """
    NOTE: Use when selecting only single items in ListBox
    print(listbox.get(listbox.curselection()))
    """

# add new items to menu
def add():
    listbox.insert(listbox.size(), entryBox.get()) # insert entered item
    listbox.configure(height = listbox.size()) # increase height of listbox after each item
    entryBox.delete(0, "end") # delete the entered text in entryBox each time inserted

# delete selected items from menu
def delete():

    # irritate through selected items in list
    for items in reversed(listbox.curselection()): # NOTE: reversed the operation for accurate results
        listbox.delete(items) # delete each item

    """
    NOTE: Use when selecting only single items in ListBox
    listbox.delete(listbox.curselection()) # remove selected item
    """

    listbox.configure(height = listbox.size()) # decrease height of listbox after each item removed

# ---------- Tkinter GUI Window ----------
window = Tk()
window.title("Restaurant Menu")

# create listbox
listbox = Listbox(window,
                  background='#f7ffde',
                  font=('Constantia', 35),
                  width=15, # adjust width of listbox
                  selectmode= MULTIPLE # select multiple items in listbox
                  )
listbox.pack()

# insert items inside listbox
listbox.insert(0, "Pizza")
listbox.insert(1, "Pasta")
listbox.insert(2, "Garlic Bread")
listbox.insert(3, "Soup")
listbox.insert(4, "Salad")

# adjust height of listbox according to items in listbox
listbox.configure(height=listbox.size())

# EntryBox: enter name of the item to be added
entryBox = Entry(
    window,
    font=("Arial", 25),
    width=21,
)
entryBox.pack()

# Submit button: to send selected items from menu
submitButton = Button(
    window,
    text="Submit",
    font=("Arial", 15),
    command=submit,
)
submitButton.pack()

# Add button: to add new items to the menu
addButton = Button(
    window,
    text="Add",
    font=("Arial", 15),
    command=add,
)
addButton.pack()

# Delete Button: remove selected items from menu
deleteButton = Button(
    window,
    text="Delete",
    font=("Arial", 15),
    command=delete,
)
deleteButton.pack()

window.mainloop()
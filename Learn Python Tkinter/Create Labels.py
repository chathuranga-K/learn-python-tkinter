from tkinter import *

window = Tk()
window.title("Sample Label")

# convert png file into a PhotoImage format
photo = PhotoImage(file="Images/laptop-coding.png")

# Label
label = Label(window,
              text="Bro, do you even code?",
              font=('Arial',30,'bold'), # font style
              foreground='black', # Foreground color (font color)
              background='dark gray', # Background color
              relief=RAISED, # solid / RAISED / SUNKEN (border style)
              borderwidth=1, # border width
              padx=20, # horizontal space between text & border
              pady=20,  # vertical space between text & border
              image=photo,
              compound="top"
              )
label.pack()
# label.place(x=20, y=10) # label.pack() # label.grid()

window.mainloop()
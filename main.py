"""from tkinter import *

#creating the application main window
root = Tk()


redbutton = Button(root, text='right', fg='red', bg='black')

redbutton.pack(side = LEFT)

# Entering the event main loop
root.mainloop()"""

"""from tkinter import *

root=Tk()

myLabel1=Label(root, text ="Tkinter basics")
myLabel2=Label(root, text ="Led Learning class running")
myLabel3=Label(root, text ="Covid")

myLabel1.grid(row=1, column=3)
myLabel2.grid(row=3, column=1)
myLabel3.grid(row=5, column=7)

root.mainloop()"""

"""from tkinter import *

root=Tk()

myButton = Button(root, text = "Click Me")
myButton.pack()

myButton1 = Button(root, text = "Click Me", state=DISABLED)
myButton1.pack()

myButton2 = Button(root, text = "Click Me", padx=60)
myButton2.pack()

myButton3 = Button(root, text = "Click Me",padx=40, pady=80)
myButton3.pack()


root.mainloop()"""


"""from tkinter import *

root=Tk()

e1 = Entry(root, width=40, fg="red", bg="green", borderwidth=4)
e1.pack()

def myClick():
    textoutput= "Hello" + e1.get()

    myLabel = Label(root, text=textoutput)

    myLabel.pack()

myButton=Button(root, text="Click Here", command=myClick)
myButton.pack()


root.mainloop()"""

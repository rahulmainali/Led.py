from tkinter import *

root =Tk()

# Title Defined
root.title("Simple Calculator")

e=Entry(root, width=45, height=30, borderwidth="4")
e.grid(row=0, column=0, columnspan=4, padx=7, pady=7)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def button_add():
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0,END)

def clear():
    e.delete(0, END)

def button_add():
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0,END)

def button_equal():
    second_number=e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_number))

button_1=Button(root, text="1", padx=35 pady=15, command=lambda:button_click(1).grid(row=1, column=0)
button_2=Button(root, text="1", padx=35 pady=15, command=lambda:button_click(2)
button_3=Button(root, text="1", padx=35 pady=15, command=lambda:button_click(3))
button_4=Button(root, text="1", padx=35 pady=15, command=lambda:button_click(4))
button_5=Button(root, text="1", padx=35 pady=15, command=lambda:button_click(5))
button_6=Button(root, text="1", padx=35 pady=15, command=lambda:button_click(6))
button_7=Button(root, text="1", padx=35 pady=15, command=lambda:button_click(7))
button_8=Button(root, text="1", padx=35 pady=15, command=lambda:button_click(8))
button_9=Button(root, text="1", padx=35 pady=15, command=lambda:button_click(9))
button_0=Button(root, text="1", padx=35 pady=15, command=lambda:button_click(0))

button_equal=Button(root, text="=", padx=80, pady=16, command=button_equal )
button_add=Button(root, text="+", padx=80, pady=16, command=button_add )
button_clear=Button(root, text="Clear", padx=80, pady=16, command=button_clear )


















root.mainloop()
from tkinter import *


def button_clicked():
    lab3.config(text=f"{round(float(input.get()) * 1.6)}")


window = Tk()
window.title("Mile to KM")
window.minsize(width=200, height=100)

# wdigets
input = Entry(width=10)
lab1 = Label(text ="Miles")
lab2 = Label(text=" is equal to")
lab3 = Label(text="")
lab4 = Label(text="Km")

button = Button(text="Calculate", command=button_clicked)


#layout

input.grid(column=2, row=0)
lab1.grid(column=3,row=0)
lab2.grid(column=0,row=1)
lab3.grid(column=2, row=1)
lab3.grid(column=2, row=1)
lab4.grid(column=3, row=1)
button.grid(column=2,row=2)

window.mainloop()
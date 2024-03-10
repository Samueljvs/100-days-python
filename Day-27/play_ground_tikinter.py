from tkinter import *




def button_clicked():
    my_label.config(text=f"{input.get()}")


window = Tk()
window.title("First GUI")
window.minsize(width=500, height=300)
window.config(padx = 50, pady = 60)

# wdigets
my_label = Label(text ="Label one", font = ("Arlial", 24, "italic"))
button_2 = Button(text = "click me!")
button = Button(text="click me", command=button_clicked)
input = Entry(width=10)

button.config(padx=50, pady=20)



#layout
#button.pack()
#my_label.pack()
#input.pack()

#place
#button.place(x=200,y=200)

# grid, row col
my_label.grid(column=0,row=0)
button_2.grid(column=2, row=0)
button.grid(column=1,row=1)
input.grid(column=3, row=3)
window.mainloop()
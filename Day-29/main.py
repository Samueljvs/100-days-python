from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(0,randint(8, 10)-1)]
    password_symbols= [choice(symbols) for char in range(0,randint(2, 4)-1)]
    password_numbers = [choice(numbers) for char in range(0,randint(2, 4)-1)]

    combine_list = password_list + password_symbols + password_numbers
    shuffle(combine_list)

    password = "".join(combine_list)
    pwd_ent.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# get value from entry with save function

def save():

    if len(web_ent.get()) > 0 and len(pwd_ent.get()) > 0: 
    
        is_ok = messagebox.askokcancel(title=web_ent.get(), message=f"There are the details entered: "
                            f"\nEmail:{user_ent.get()} \nPassword: {pwd_ent.get()}")

        if is_ok:
            with open("Day-29/data.txt", "a") as data_file:
                data_file.write(f"{web_ent.get()} | {user_ent.get()} | {pwd_ent.get()}\n")
            web_ent.delete(0,END)
            pwd_ent.delete(0,END)
    else:
        messagebox.showerror(title="Oops", message= "Oops don't leave feild empty")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

mypass_img = PhotoImage(file="Day-29/logo.png")

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image = mypass_img)

web_lb = Label(text = "Website:")
user_lb = Label(text = "Email/Username:")
pwd_lb = Label(text = "Password:")

web_ent = Entry(width= 36)
web_ent.focus()
user_ent = Entry(width= 36)
user_ent.insert(0, "sam.john.vs@gmail.com")


pwd_ent = Entry(width= 28)
gen_pwd_bttn = Button(text="Create PWD", command=generate_password)
add_bttn = Button(text="Add", width = 35, command = save)


canvas.grid(column=1,row=0)
web_lb.grid(column=0, row=1)
user_lb.grid(column=0, row=2)
pwd_lb.grid(column=0,row=3)
web_ent.grid(column=1, row=1, columnspan=2)
user_ent.grid(column=1, row=2, columnspan=2)
pwd_ent.grid(column=1, row=3)
gen_pwd_bttn.grid(column=2, row=3)
add_bttn.grid(column=1, row = 4, columnspan=2)

window.mainloop()


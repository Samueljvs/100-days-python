from tkinter import *
import pandas as pd
import random as rnd

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_word = {}


# Read in data
try:  
    data = pd.read_csv("Day-31/data/words_to_learn.csv")
except FileNotFoundError:
    org_data = pd.read_csv("Day-31/data/french_words.csv")
    to_learn = org_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



print(len(data))



# function for getting new words when buttons are clicked
def get_new_card():
    global current_word, flip_timer, to_learn
    window.after_cancel(flip_timer) 
    canvas.itemconfig(card_background, image = front_card)

    current_word = rnd.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill = 'black')                        # Update title
    canvas.itemconfig(word_text, text=current_word["French"], fill = 'black')           # Update word
    flip_timer = window.after(3000, flip_card)                          # Flip after 3 seconds

def flip_card():
    canvas.itemconfig(card_background, image = back_card)
    canvas.itemconfig(title_text, text="English", fill = 'white')                               # Update title
    canvas.itemconfig(word_text, text=current_word["English"], fill = 'white')                  # Update word


def is_known():
    to_learn.remove(current_word)
    
    new_df = pd.DataFrame(to_learn)
    new_df.to_csv("Day-31/data/words_to_learn.csv", index=False)

    get_new_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800)

## Main Card
front_card = PhotoImage(file="Day-31/images/card_front.png")
back_card = PhotoImage(file = "Day-31/images/card_back.png")

card_background = canvas.create_image(400, 263, image=front_card)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness= 0)
canvas.grid(row=0, column=0, columnspan=2)

# text
title_text = canvas.create_text(400, 150, text="Title", font = ("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font = ("Ariel", 60, "bold"))

## Buttons
right_img = PhotoImage(file = "Day-31/images/right.png")
wrong_img = PhotoImage(file = "Day-31/images/wrong.png")

button_right = Button(image=right_img, highlightthickness=0, command=is_known)
button_right.grid(row=1, column=1)
button_unknown = Button(image=wrong_img, highlightthickness=0, command=get_new_card)
button_unknown.grid(row=1, column=0)


##Start APP##

flip_timer = window.after(3000, flip_card)
get_new_card()
window.mainloop()



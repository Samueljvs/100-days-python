import turtle
import pandas as pd

image = 'Day-25/US-States-Game/blank_states_img.gif'
states_df = pd.read_csv("Day-25/US-States-Game/50_States.csv")

screen = turtle.Screen()
screen.title("U.S States Game")

screen.addshape(image)
turtle.shape(image)

all_states = states_df.state.tolist()
guessed_states = []
missing_states = []

while len(guessed_states) < 50:
## collect answer
    
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50: Guess the State", prompt="What's the state?").title()    

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states] 
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("Day-26/US-States-Game/states_learn.csv")
        break
    
    if answer_state in states_df.state.to_list():    
## get cords
        guessed_states.append(answer_state)

        x_cord = states_df[states_df.state == answer_state].x.to_list()
        y_cord = states_df[states_df.state == answer_state].y.to_list()

        guess = turtle.Turtle()
        guess.hideturtle()
        guess.penup()
        guess.goto(x = x_cord[0], y = y_cord[0])
        guess.write(answer_state)

print(len(missing_states))


screen.exitonclick()
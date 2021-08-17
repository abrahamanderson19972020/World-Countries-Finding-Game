from turtle import Turtle, Screen
import pandas as pd
from scoreboard import Scoreboard
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
FONT2 = ("Courier", 7, "normal")


#
# def get_mouse_click_coor(x, y):
#     print(x, y)
screen = Screen()
screen.title("World Map Game")
screen.addshape("world_map.gif")
my_turtle = Turtle()
my_turtle.shape("world_map.gif")
screen.tracer(0)
user_score = Scoreboard()
df = pd.read_csv("countries.csv")
guessed_states = list()
states = df["state"].to_list()
print(states)
is_game_on = True
while is_game_on:
    screen.update()
    answer = screen.textinput(title= f"{user_score.score}/144 Countries Correct ", prompt="What is country name:")
    if answer.title() == "Exit":
        user_score.color("maroon1")
        user_score.goto(0, 0)
        user_score.write(f"You knew {user_score.score} states correctly.Try again!", align=ALIGNMENT, font=FONT)
        states_to_learn = list()
        for state in states:
            if states not in guessed_states:
                states_to_learn.append(states)
                with open("states_to_learn.csv", "w") as file:
                    for state in states_to_learn:
                        file.write(str(state))
        break
    if answer.title() in df["state"].values:
        user_score.increase_score()
        guessed_states.append(answer.title())
        x = df[df["state"] == answer.title()]["x"].values
        y = df[df["state"] == answer.title()]["y"].values
        new_turtle = Turtle()
        new_turtle.color("black")
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(int(x[0]), int(y[0]))
        print(x[0])
        print(y[0])
        new_turtle.write(answer.title(), align=ALIGNMENT, font=FONT2)
        if user_score.score == 144:
            is_game_on = False

screen.exitonclick()
# screen.onscreenclick(get_mouse_click_coor)
#
# screen.mainloop()


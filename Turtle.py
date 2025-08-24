import random
from turtle import Turtle, Screen
# import turtle


screen = Screen()
screen.setup(width=500,height=400)
screen.bgpic(picname="download1.gif")
screen.bgcolor("black")
user_guess = screen.textinput(title="Make a bet",prompt="Which one will win: ")
colors = ['white','red','pink','green','orange','yellow']
y_positions = [-100,-70,-40,-10,20,50]
all_turtle = []
is_game_on = False
# print(user_guess)
# tim = Turtle()
# tom = Turtle()
# tqm = Turtle()
# twm = Turtle()
# tem = Turtle()
# trm = Turtle()
#
#
# tim.penup()
# tim.color("red")
# tim.shape("turtle")
# tim.goto(x=-230,y=-100)
#
# tom.penup()
# tom.color("blue")
# tom.shape("turtle")
# tom.goto(x=-230,y=-50)
#
# tqm.penup()
# tqm.color("pink")
# tqm.shape("turtle")
# tqm.goto(x=-230,y=0)
#
# twm.penup()
# twm.color("yellow")
# twm.shape("turtle")
# twm.goto(x=-230,y=50)
#
# tem.penup()
# tem.color("green")
# tem.shape("turtle")
# tem.goto(x=-230,y=100)
#


for turtle_index in range(6):
    tim = Turtle()
    tim.color(colors[turtle_index])
    tim.shape("turtle")
    tim.penup()
    tim.goto(x=-230,y=y_positions[turtle_index])
    all_turtle.append(tim)

if user_guess:
    is_game_on = True
while is_game_on:
    for turtle in all_turtle:
        random_speed = random.randint(0,10)
        turtle.forward(random_speed)

        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_guess:
                print(f"you've own {winning_color} turtle own the race..")
            else:
                print(f"you've lost {winning_color} turtle lost")


screen.exitonclick()

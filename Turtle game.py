from turtle import Turtle, Screen
import random
import turtle


#Setup screen

screen = Screen()
screen.setup(width=500, height=400)


#define turtles

y_position = [-70, -40, -10, 20, 50, 80]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)
    
    
#Input user bet

user_bet = screen.textinput(title ='Make your bet',prompt ='Which turtle will win?')

if user_bet:
    is_race_on = True


#Move turtle, check for winner

while is_race_on:
    
    for i in all_turtles:
        
        if i.xcor() > 230:
            winning_color=i.pencolor()
            
            if winning_color==user_bet:
                print("You've won")
                is_race_on=False
                break
                
            else:
                print("Winning color is " + winning_color)
                print("You have lost please try again")
                is_race_on=False
                break
                
                
        rand_distance = random.randint(0,10)
        i.forward(rand_distance)
    
screen.exitonclick()

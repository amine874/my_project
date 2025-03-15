from turtle import Turtle , Screen
import random

window=Screen()
window.setup(width=800,height=600)
window.bgcolor("black")

sam=Turtle()
sam.shape("turtle")
sam.color("white")
sam.pensize(5)
sam.speed("fast")

tom=Turtle()
tom.shape("square")
tom.color("orange")
tom.pensize(5)
tom.speed("fastest")

my_angles=[0.90,180,270]
my_distance=[20,30,40,50,60,70,80,90,100]
loop_count=[13,23,45,21]
def draw_random(turtle_name):
    for _ in range(random.choice(loop_count)):
        turtle_name.forward(random.choice(my_distance))
        turtle_name.left(random.choice(my_angles))

for _ in range(80):
    tom.circle(100)
    tom.left(10)

    

window.exitonclick()
               
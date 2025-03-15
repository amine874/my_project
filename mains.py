from turtle import Screen,Turtle
from paadle import Paddle
from ball import Ball


screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("octucode:ping pong")
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")



screen.exitonclick()
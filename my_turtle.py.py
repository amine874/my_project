from turtle import Turtle , Screen
import random

sam=Turtle()
window=Screen()
list_of_schapes=["turtle","square","triangle","circle"]
list_of_sizes=[2,3,4,5,6,7,8]
list_of_colors=["green","purple","orange","red","black","blue"]
sam.speed("slowest")
def draw_a_square():
    for _ in range(4):
        sam.color(random.choice(list_of_colors))
        sam.pensize(random.choice(list_of_sizes))
        sam.shape(random.choice(list_of_schapes))
        sam.forward(100)
        sam.left(90)

draw_a_square()
window.exitonclick()
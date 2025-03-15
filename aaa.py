from turtle import Turtle, Screen

sam=Turtle("turtle")
sam.color("red")

for _ in range(4):
  sam.forward(100)
  sam.left(90)

ka=Turtle()
ka.color("black")
for x in range(3):
  ka.forward(100)
  ka.left(120)
  
#sam.left(90)
#sam.forward(100)
window=Screen()

window.exitonclick()
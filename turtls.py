from turtle import Turtle , Screen
window=Screen()
sam=Turtle()
user_name=window.textinput(title="hello",prompt="was wurdest du malen? Quadrat,Dreieck,Kreis")
if user_name=="Quadrat":
    for _ in range(4):
     sam.forward(100)
     sam.left(90)
elif user_name=="Dreieck":
   for _ in range(3):
     sam.forward(100)
     sam.left(120)
elif user_name=="kreis":
   for _ in range(360):
      sam.forward(1)
      sam.left(1)
elif user_name=="exit":
   sam.reset()
sam.hideturtle()
#sam.write("hello",font="arial",align="center")










window.exitonclick()


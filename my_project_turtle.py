import turtle

# إعداد نافذة التيرتل
screen = turtle.Screen()
screen.bgcolor("white")

# إعداد السلحفاة للرسم
flag = turtle.Turtle()
flag.speed(5)

# رسم الألوان الثلاثة في العلم (أحمر، أبيض، أخضر)
# الخطوط الأفقية
def draw_rect(color, y_position):
    flag.penup()
    flag.goto(-400, y_position)
    flag.pendown()
    flag.begin_fill()
    flag.fillcolor(color)
    for _ in range(2):
        flag.forward(800)
        flag.left(90)
        flag.forward(100)
        flag.left(90)
    flag.end_fill()

# رسم المستطيل الأحمر
draw_rect("red", 100)

# رسم المستطيل الأبيض
draw_rect("white", 0)

# رسم المستطيل الأخضر
draw_rect("green", -100)

# رسم مثلث الأسود في الجانب الأيسر
flag.penup()
flag.goto(-400, 100)
flag.setheading(90)
flag.pendown()
flag.begin_fill()
flag.fillcolor("black")
flag.goto(-250, 0)
flag.goto(-400, -100)
flag.goto(-400, 100)
flag.end_fill()

# إنهاء الرسم
flag.hideturtle()
screen.mainloop()


import turtle

def draw_peppa():
    # 设置画布
    turtle.setup(800, 600)
    t = turtle.Turtle()
    t.speed(5)

    # 画头
    t.penup()
    t.goto(-50, 100)
    t.pendown()
    t.color("pink")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    # 画眼睛
    t.penup()
    t.goto(-70, 130)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    t.penup()
    t.goto(-30, 130)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    # 画眼珠
    t.penup()
    t.goto(-70, 135)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    t.penup()
    t.goto(-30, 135)
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    # 画鼻子
    t.penup()
    t.goto(-50, 90)
    t.pendown()
    t.color("pink")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    # 画鼻孔
    t.penup()
    t.goto(-60, 95)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(3)
    t.end_fill()

    t.penup()
    t.goto(-40, 95)
    t.pendown()
    t.begin_fill()
    t.circle(3)
    t.end_fill()

    # 画嘴巴
    t.penup()
    t.goto(-70, 80)
    t.pendown()
    t.setheading(-30)
    t.circle(20, 60)

    # 画身体
    t.penup()
    t.goto(-90, 50)
    t.pendown()
    t.color("pink")
    t.begin_fill()
    t.setheading(-90)
    t.circle(100, 180)
    t.setheading(0)
    t.forward(200)
    t.setheading(90)
    t.circle(100, 180)
    t.end_fill()

    # 画腿
    for i in range(2):
        t.penup()
        t.goto(-70 + i * 40, -50)
        t.pendown()
        t.setheading(-90)
        t.forward(50)

    # 画手
    for i in range(2):
        t.penup()
        t.goto(-90 + i * 180, 50)
        t.pendown()
        t.setheading(-30 if i == 0 else -150)
        t.forward(50)

    t.hideturtle()
    turtle.done()

draw_peppa()

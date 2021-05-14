import turtle


screen = turtle.Screen()
screen.title('Doraemon')
doremon = turtle.Turtle()
doremon.setheading(180)
doremon.pensize(2)
doremon.speed(1000)


# Eyes
for i in range(90):
    doremon.forward(1)
    doremon.right(4)

doremon.up()
doremon.goto(9, 10)
doremon.dot(4)
doremon.goto(30, 0)
doremon.down()

for i in range(90):
    doremon.forward(1)
    doremon.right(4)

doremon.up()
doremon.goto(21, 10)
doremon.dot(4)
doremon.goto(15, -10)
doremon.down()

# Nose
doremon.fillcolor('red')
doremon.begin_fill()

for i in range(45):
    doremon.forward(1)
    doremon.right(8)

doremon.end_fill()
doremon.fillcolor('black')

doremon.left(90)
doremon.forward(32)

doremon.up()
doremon.goto(-15, 10)
doremon.right(80)
doremon.down()

for i in range(29):
    doremon.forward(3)
    doremon.left(5)

# Neck
doremon.left(-3)
for i in range(35):
    doremon.forward(3)
    doremon.left(2)

doremon.left(10)
for i in range(27):
    doremon.forward(3)
    doremon.left(5)

doremon.up()
doremon.goto(-38, -48)
doremon.setheading(132)
doremon.down()

for i in range(130):
    doremon.forward(1)
    doremon.right(1)

# Head
doremon.right(2)
doremon.forward(27)

for i in range(131):
    doremon.forward(1)
    doremon.right(1)

doremon.up()
doremon.goto(-38, -48)
doremon.down()

# Hand
for i in range(50):
    doremon.forward(1)
    doremon.left(1)

for i in range(51):
    doremon.forward(1)
    doremon.left(7)

doremon.up()
doremon.goto(72.81, -46.55)
doremon.down()

doremon.setheading(-49)
for i in range(50):
    doremon.forward(1)
    doremon.right(1)

for i in range(51):
    doremon.forward(1)
    doremon.right(7)

doremon.up()
doremon.goto(15, -79)
doremon.setheading(180)
doremon.down()

# bell
doremon.fillcolor('yellow')
doremon.begin_fill()
for i in range(45):
    doremon.forward(1)
    doremon.right(8)

doremon.end_fill()

doremon.fillcolor('black')

doremon.up()
doremon.goto(7, -70)
doremon.down()
doremon.goto(22, -70)

doremon.up()
doremon.goto(7, -70)
doremon.down()

for i in range(54):
    doremon.forward(1)
    doremon.right(1)

doremon.up()
doremon.goto(22, -70)
doremon.setheading(0)
doremon.down()
doremon.forward(3)

for i in range(54):
    doremon.forward(1)
    doremon.left(1)

doremon.up()
doremon.goto(-32, -56)
doremon.setheading(-95)
doremon.down()

for i in range(9):
    doremon.forward(7)
    doremon.left(1)

doremon.up()
doremon.goto(66.81, -54.55)
doremon.setheading(-85)
doremon.down()

for i in range(10):
    doremon.forward(7)
    doremon.right(1)

doremon.up()
doremon.goto(-10, -140)
doremon.setheading(180)
doremon.down()

for i in range(24):
    doremon.forward(1)
    doremon.right(1)

for i in range(22):
    doremon.forward(1)
    doremon.right(8)

doremon.setheading(5)
doremon.forward(15)

for i in range(24):
    doremon.forward(1)
    doremon.right(1)

for i in range(22):
    doremon.forward(1)
    doremon.right(8)

doremon.setheading(195)
doremon.forward(1)

for i in range(15):
    doremon.forward(1)
    doremon.right(1)

doremon.up()
doremon.goto(44, -140)
doremon.down()

for i in range(24):
    doremon.forward(1)
    doremon.right(1)


for i in range(22):
    doremon.forward(1)
    doremon.right(8)

doremon.setheading(5)
doremon.forward(15)

for i in range(24):
    doremon.forward(1)
    doremon.right(1)

for i in range(22):
    doremon.forward(1)
    doremon.right(8)

doremon.setheading(195)
doremon.forward(1)

for i in range(15):
    doremon.forward(1)
    doremon.right(1)

"""Chest"""
doremon.up()
doremon.goto(15, -55)
doremon.goto(-20.06, -62.89)
doremon.setheading(240)
doremon.down()

for i in range(27):
    doremon.forward(2)
    doremon.left(4)

doremon.setheading(350)

for i in range(22):
    doremon.forward(1.7)
    doremon.left(0.9)

for i in range(27):
    doremon.forward(2)
    doremon.left(4)

doremon.up()
doremon.goto(-9.75, -80.43)
doremon.setheading(-85)
doremon.down()
for i in range(11):
    doremon.forward(2)
    doremon.left(6)

doremon.setheading(-35)

for i in range(40):
    doremon.forward(1)
    doremon.left(2)

for i in range(8):
    doremon.forward(2)
    doremon.left(6)

doremon.forward(1)
doremon.goto(-9.75, -80.43)

doremon.up()
doremon.goto(-13, -35)
doremon.setheading(-30)
doremon.down()

for i in range(60):
    doremon.forward(1)
    doremon.left(1)

doremon.up()
doremon.forward(100)
doremon.goto(-6, -15)
doremon.setheading(160)
doremon.down()

doremon.forward(45)

doremon.up()
doremon.goto(-6, -20)
doremon.setheading(180)
doremon.down()

doremon.forward(45)

doremon.up()
doremon.goto(-6, -25)
doremon.setheading(200)
doremon.down()

doremon.forward(45)

doremon.up()
doremon.goto(36, -15)
doremon.setheading(20)
doremon.down()

doremon.forward(45)

doremon.up()
doremon.goto(36, -20)
doremon.setheading(0)
doremon.down()

doremon.forward(45)

doremon.up()
doremon.goto(36, -25)
doremon.setheading(-20)
doremon.down()

doremon.forward(45)

doremon.hideturtle()

turtle.done()
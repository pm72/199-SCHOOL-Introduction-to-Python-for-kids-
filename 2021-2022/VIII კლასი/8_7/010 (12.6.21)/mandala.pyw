import turtle

s = turtle.getscreen()
t = turtle.Turtle()
t.speed(5)

for i in range(4):
    t.fd(100)
    t.lt(90)


# პირველი დახრილი კვადრატი
t.goto(50, 50)
t.goto(0, 100)
t.goto(-50, 50)
t.goto(0, 0)

# მეორე დახრილი კვადრატი
t.goto(50, -50)
t.goto(100, 0)
t.goto(50, 50)

# მესამე დახრილი კვადრატი
t.goto(100, 100)
t.goto(50, 150)
t.goto(0, 100)

# მეოთხე დახრილი კვადრატი
t.fd(100)
t.goto(150, 50)
t.goto(100, 0)



# ===============
turtle.ht()
t.ht()

turtle.exitonclick()

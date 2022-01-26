import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("მეთოდები .heading() და .setheading()")
window.setup(1000, 600)

t.pen(pensize=4, pencolor='blue')

# 0 გრადუსი
t.fd(200)
t.write(f"კუთხე გრადუსებში: {t.heading()}", font=('calibri', 12))

t.up()
t.home()
t.down()

# 90 გრადუსი
t.setheading(90)
t.fd(200)
t.write(f"კუთხე გრადუსებში: {t.heading()}", font=('calibri', 12))

t.up()
t.home()
t.down()

# 180 გრადუსი
t.setheading(180)
t.fd(200)
t.write(f"კუთხე გრადუსებში: {t.heading()}", font=('calibri', 12))

t.up()
t.home()
t.down()

# 270 გრადუსი
t.setheading(270)
t.fd(200)
t.write(f"კუთხე გრადუსებში: {t.heading()}", font=('calibri', 12))

t.up()
t.home()
t.down()




# =========================
turtle.exitonclick()
import turtle

window = turtle.getscreen()
t = turtle.Turtle()

window.title("ტექსტი turtle ეკრანზე")
window.setup(1000, 600)

t.up()
t.goto(0, 200)
t.down()

t.pen(pencolor='red')

t.write("გილოცავთ შობას და ახალ წელს!..", font=('Calibri', 40, 'bold italic underline'),
        align='center')



# ===================
t.ht()
turtle.ht()
turtle.exitonclick()
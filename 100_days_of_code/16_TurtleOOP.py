from turtle import Turtle, Screen

def draw_heart():
    timmy.begin_fill()
    timmy.left(50)
    timmy.forward(133)
    timmy.circle(50, 200)
    timmy.right(140)
    timmy.circle(50, 200)
    timmy.forward(133)
    timmy.end_fill()

def draw_cat(color, size):
    timmy.color(color)
    timmy.begin_fill()

    for _ in range(4):
        timmy.forward(size)
        timmy.left(90)

    timmy.end_fill()

# Set up the turtle and screen
timmy = Turtle()
timmy.shape("turtle")
timmy.speed("slowest")

my_screen = Screen()
my_screen.delay(1)

# Draw hearts
timmy.penup()
timmy.goto(-100, 100)
timmy.write("Zak please stop this", align="center", font=("Arial", 16, "normal"))

for _ in range(5):
    timmy.penup()
    timmy.goto(-200, -200)
    timmy.pendown()
    timmy.fillcolor("red")
    draw_heart()

# Draw a black cat
timmy.penup()
timmy.goto(50, -50)
timmy.pendown()
draw_cat("black", 30)

# Draw a Maine Coon cat
timmy.penup()
timmy.goto(-150, -50)
timmy.pendown()
draw_cat("brown", 40)

my_screen.exitonclick()

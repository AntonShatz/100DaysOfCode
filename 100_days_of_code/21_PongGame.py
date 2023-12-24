import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=3, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-250, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=3, stretch_len=1)
paddle_b.penup()
paddle_b.goto(250, 0)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Paddle movement functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 190:
        paddle_a.sety(y + 20)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -190:
        paddle_a.sety(y - 20)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 190:
        paddle_b.sety(y + 20)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -190:
        paddle_b.sety(y - 20)

# Keyboard bindings
screen.listen()
screen.onkey(paddle_a_up, "w")
screen.onkey(paddle_a_down, "s")
screen.onkey(paddle_b_up, "Up")
screen.onkey(paddle_b_down, "Down")

# Score variables
score_a = 0
score_b = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 170)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 14, "normal"))

# Main game loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1

    # Paddle and ball collisions
    if (
        (ball.xcor() > 240 and ball.xcor() < 250)
        and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50)
    ):
        ball.color("blue")
        ball.setx(240)
        ball.dx *= -1

    elif (
        (ball.xcor() < -240 and ball.xcor() > -250)
        and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50)
    ):
        ball.color("red")
        ball.setx(-240)
        ball.dx *= -1

    # Score update
    if ball.xcor() > 290:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score_display.clear()
        score_display.write(
            f"Player A: {score_a}  Player B: {score_b}",
            align="center",
            font=("Courier", 14, "normal"),
        )

    elif ball.xcor() < -290:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score_display.clear()
        score_display.write(
            f"Player A: {score_a}  Player B: {score_b}",
            align="center",
            font=("Courier", 14, "normal"),
        )

    # Update the screen
    screen.update()


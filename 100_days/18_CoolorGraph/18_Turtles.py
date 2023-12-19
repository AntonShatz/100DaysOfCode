import turtle
import math
import random


class SpirographDrawer:
    def __init__(self):
        self.spiro_turtle = turtle.Turtle()
        self.spiro_turtle.speed("fastest")
        self.spiro_turtle.pensize(5)
        self.current_radius = 10

        turtle.onscreenclick(self.on_click)

    def random_color(self):
        return (random.random(), random.random(), random.random())

    def draw_spirograph(self, x, y, radius):
        self.spiro_turtle.penup()
        self.spiro_turtle.goto(x, y)
        self.spiro_turtle.pendown()

        for _ in range(36):
            self.spiro_turtle.color(self.random_color(), self.random_color())
            self.spiro_turtle.circle(radius)
            self.spiro_turtle.left(10)
            self.spiro_turtle.circle(radius)
            self.spiro_turtle.left(10)

    def on_click(self, x, y):
        self.current_radius += 10
        self.draw_spirograph(x, y, self.current_radius)

class TurtleController:

    def __init__(self, turtle_obj):
        self.turtle_obj = turtle_obj
        turtle.onkey(self.move_left, "a")
        turtle.onkey(self.move_right, "d")
        turtle.onkey(self.move_up, "w")
        turtle.onkey(self.move_down, "s")
        self.turtle_obj.pensize(5)
        turtle.listen()

    def move_and_change_color(self, heading):
        self.turtle_obj.color(random.random(), random.random(), random.random())
        self.turtle_obj.setheading(heading)
        self.turtle_obj.forward(50)

    def move_left(self):
        self.move_and_change_color(180)

    def move_right(self):
        self.move_and_change_color(0)

    def move_up(self):
        self.move_and_change_color(90)

    def move_down(self):
        self.move_and_change_color(270)

if __name__ == "__main__":
    turtle_obj = turtle.Turtle()
    turtle_obj.speed("fastest")
    turtle_controller = TurtleController(turtle_obj)
    turtle.mainloop()


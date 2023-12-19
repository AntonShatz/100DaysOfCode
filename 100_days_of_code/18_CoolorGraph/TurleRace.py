import turtle
import random
import tkinter as tk
from tkinter import simpledialog

# Function to create a turtle with a specified color
def create_turtle(color):
    turtle_shape = turtle.Turtle()
    turtle_shape.shape("turtle")
    turtle_shape.color(color)
    turtle_shape.penup()
    return turtle_shape

# Function to move all turtles to the starting position
def reset_turtles(turtles):
    for i, turtle_shape in enumerate(turtles):
        turtle_shape.goto(-230, -100 + i * 60)  # Adjusted starting positions

# Function to check if any turtle has reached the finish line
def check_winner(turtles):
    for turtle_shape in turtles:
        if turtle_shape.xcor() >= 210:  # Adjusted finish line position
            return turtle_shape.color()[0]  # Return the color of the winning turtle
    return None

# Draw starting and finish lines
def draw_lines():
    start_line = turtle.Turtle()
    start_line.penup()
    start_line.goto(-210, -120)
    start_line.pendown()
    start_line.goto(-210, 120)
    start_line.hideturtle()

# Main function
def race():
    screen = turtle.Screen()
    screen.setup(width=500,height=500)
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    colors = ["red", "green", "blue", "orange", "purple"]

    # Prompt user to choose a color for the winning turtle
    chosen_color = simpledialog.askstring("Choose Winning Turtle Color", "Choose a color for the winning turtle:",
                                          initialvalue=random.choice(colors))

    # Create turtles with different colors
    turtles = [create_turtle(color) for color in colors]

    reset_turtles(turtles)
    draw_lines()

    winner_color = None

    while winner_color is None:
        for turtle_shape in turtles:
            turtle_shape.forward(random.randint(0, 5))

        winner_color = check_winner(turtles)

    # Check if the user's chosen color matches the winner's color
    if chosen_color.lower() == winner_color:
        print("Congratulations! You guessed correctly. Your guess:", chosen_color.lower(), "Winner's color:",
              winner_color)
    else:
        print("Sorry, you guessed wrong. Your guess:", chosen_color.lower(), "Winner's color:", winner_color)

    turtle.done()

# Run the race when the script is executed
if __name__ == "__main__":
    race()

import turtle
from colorgram import extract
import random

def extract_colors(image_path, num_colors):
    colors = extract(image_path, num_colors)
    return [(color.rgb.r, color.rgb.g, color.rgb.b, (color.rgb.r/255, color.rgb.g/255, color.rgb.b/255)) for color in colors]

def draw_dots_with_colors(colors, num_dots_per_line, num_lines, spacing):
    turtle.speed(0)  # Set speed to maximum
    turtle.hideturtle()
    turtle.bgcolor("white")
    turtle.title("Dots Drawing")

    # Calculate the total width and height of the grid
    total_width = num_dots_per_line * spacing
    total_height = num_lines * spacing

    # Move the turtle to the starting position outside the visible area
    turtle.penup()
    turtle.goto(-total_width / 2, total_height / 2)
    turtle.pendown()

    for line in range(num_lines):
        for _ in range(num_dots_per_line):
            color = random.choice(colors)
            turtle.pencolor(color[3])

            # Calculate a random position within the grid for each dot
            x_position = random.uniform(-total_width / 2, total_width / 2)
            y_position = random.uniform(-total_height / 2, total_height / 2)

            turtle.penup()
            turtle.goto(x_position, y_position)
            turtle.pendown()

            turtle.dot(20)

    turtle.done()

# Example usage:
image_path = "ColoerPlate.jpg"
num_colors = 1000  # Adjust as needed
num_dots_per_line = 50  # Adjust as needed
num_lines = 50  # Adjust as needed
spacing = 10  # Adjust as needed
colors = extract_colors(image_path, num_colors)
draw_dots_with_colors(colors, num_dots_per_line, num_lines, spacing)

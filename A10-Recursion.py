"""
Initial code written by David Johnson, University of Utah.
This, and all derived works may not be publicly shared.

Assignment completed by Thu Ha
"""
import turtle

def draw_spiral(line_length, turtle):
    """
    Draws a spiral with an initial line of line_length centered
    at the current turtle location.

    :param line_length: The inner part of the spiral length
    :param turtle: A python turtle
    :return: None
    """

    while line_length < 25:
        turtle.forward(line_length)
        turtle.left(15)
        line_length *= 1.02

def draw_spiral_recursive(line_length, turtle):
    """
    Draw spiral recursive based on the while loop version in draw spiral function
    :param line_length: The inner part of the spiral length
    :param turtle: A python turtle
    :return: None
    """
    if line_length > 25:
        return
    turtle.left(15)
    turtle.forward(line_length)
    draw_spiral_recursive(line_length * 1.02, turtle)

def draw_centered_circle(circle_radius, turtle):
    """
    A helper function to make the circle fractal easier to
    draw with turtle. It draws a circle of size circle_radius
    centered at the current turtle location.
    :param circle_radius: The radius of the circle
    :param turtle: The Python turtle to draw the circle.
    :return: None
    """

    turtle.penup()
    turtle.forward(circle_radius)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(circle_radius)
    turtle.penup()
    turtle.right(90)
    turtle.backward(circle_radius)
    turtle.penup()

def draw_circles(circle_radius, turtle):
    """
    Draw a big circle with three half-sized circle left, right, and up
    from the big circle. Return the turtle to its
    original location and heading.

    :param circle_radius: The radius of the center circle
    :param turtle: The Python turtle to draw.
    :return: None.
    """
    draw_centered_circle(circle_radius, turtle)
    turtle.left(90)
    turtle.forward(circle_radius * 1.5)
    draw_centered_circle(circle_radius * 0.5, turtle)
    turtle.backward(circle_radius * 1.5)
    turtle.right(180)
    turtle.forward(circle_radius * 1.5)
    draw_centered_circle(circle_radius * 0.5, turtle)
    turtle.backward(circle_radius * 1.5)
    turtle.left(90)
    turtle.forward(circle_radius * 1.5)
    draw_centered_circle(circle_radius * 0.5, turtle)
    turtle.backward(circle_radius * 1.5)

def draw_fractal_circles(circle_radius, turtle):
    """
    The draw_circles function draws a center circle with half-sized
    circles attached left, right, and forward of the main circle.
    Draw_fractal_circles function, those smaller circles have even smaller
    circles attached with the same pattern, keep adding
    circles while the circle radius more than two
    :param circle_radius: The radius of the center circle
    :param turtle: A python turtle
    :return: None
    """
    #base_case
    if circle_radius <= 2:
        return

    branch_distance = circle_radius * 1.5
    next_circle_radius = circle_radius/2

    draw_centered_circle(circle_radius, turtle)

    turtle.right(90)
    turtle.forward(branch_distance)
    draw_fractal_circles(next_circle_radius, turtle)
    turtle.backward(branch_distance)

    turtle.left(180)
    turtle.forward(branch_distance)
    draw_fractal_circles(next_circle_radius, turtle)
    turtle.backward(branch_distance)

    turtle.right(90)
    turtle.forward(branch_distance)
    draw_fractal_circles(next_circle_radius, turtle)
    turtle.backward(branch_distance)

def main():
    """
    Provide code to setup and test the spiral and circle
    fractal code.
    :return: None.
    """
    # Set up the turtle and window
    recursive_turtle = turtle.Turtle()
    recursive_turtle.speed(0)
    myWin = turtle.Screen()
    recursive_turtle.penup()
    recursive_turtle.left(90)
    recursive_turtle.backward(100)

    # Draw the spiral
    recursive_turtle.pendown()
    #draw_spiral(1, recursive_turtle)
    draw_spiral_recursive(1, recursive_turtle)

    # Draw the circles
    recursive_turtle.penup()
    recursive_turtle.goto(0, 100)
    recursive_turtle.setheading(90)
    # draw_circles(50, recursive_turtle)
    draw_fractal_circles(50, recursive_turtle)

    myWin.exitonclick()

if __name__ == "__main__":
    main()
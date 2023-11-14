import turtle
from turtle import *

window = Screen()
art_turtle = Turtle()
art_turtle.speed(0)


#
# CS 1400 Assignment 2. Written by David Johnson and Thu Ha
# This code, as it is now or after modification, may not be shared or uploaded to any public site.
# It may be uploaded to the course approved assignment submission system.

# Draw a square with a Python turtle.
# Do not modify this.
def draw_square():
    for side in range(4):
        art_turtle.forward(25)
        art_turtle.left(90)

# Draw a wall of ten blocks with a little space between each one.
def draw_wall():
    n = -150
    for count in range(11):
        draw_square()
        art_turtle.penup()
        art_turtle.goto(n, 250)
        art_turtle.pendown()
        n = n+30

# Draw a simple face with a head, a mouth, and two eyes.
def draw_face():
    #draw a face
    art_turtle.circle(50)
    #draw eyes
    for count in range(2):
        art_turtle.penup()
        art_turtle.goto(-20, 150)
        art_turtle.pendown()
        art_turtle.circle(10)
        art_turtle.penup()
        art_turtle.goto(20, 150)
        art_turtle.pendown()
        art_turtle.circle(10)
    #draw mouth
    art_turtle.penup()
    art_turtle.goto(-30, 140)
    art_turtle.pendown()
    art_turtle.forward(60)
    art_turtle.left(90)
    art_turtle.circle(30, -180)

def draw_leaves():
    art_turtle.pensize(7)               #choose leaves pensize
    art_turtle.pencolor("green")        #choose leaves pen color
    for count in range (3):             #create leaves
        art_turtle.forward(40)
        art_turtle.right(120)
def draw_body():
    art_turtle.forward(20)
    art_turtle.right(90)
    art_turtle.forward(50)
    art_turtle.left(180)
    art_turtle.forward(100)
    art_turtle.penup()                  # return to original position
    art_turtle.backward(100)
    art_turtle.right(180)
    art_turtle.backward(50)
    art_turtle.left(90)
    art_turtle.backward(20)
def draw_petal():
    art_turtle.pensize(3)           #choose flower pensize
    art_turtle.pencolor("red")      #choose flower pencolor
    art_turtle.forward(20)
    art_turtle.left(90)
    art_turtle.forward(50)
    art_turtle.pendown()
    for count in range (10):
        art_turtle.forward(30)
        art_turtle.dot(200 / 10)
        art_turtle.forward(-30)
        art_turtle.right(360 / 10)
    art_turtle.penup()                 # return to the original position
    art_turtle.backward(50)
    art_turtle.right(90)
    art_turtle.backward(20)
def draw_flower():
    draw_leaves()
    draw_body()
    draw_petal()

# The following code uses the functions above to draw different things on the screen.
# You should not need to modify this code except to rename the calls to draw_object
# to a more descriptive name.

# Move to the top of the screen and draw a wall
art_turtle.penup()
art_turtle.goto(-150, 250)
art_turtle.pendown()
draw_wall()

# Move to the top middle and draw a face
art_turtle.penup()
art_turtle.goto(0, 100)
art_turtle.pendown()
draw_face()

# Move to the bottom left and draw an object
art_turtle.penup()
art_turtle.goto(-100, -100)
art_turtle.setheading(0)
art_turtle.pendown()
draw_flower()

# Move to the bottom right and draw an object
art_turtle.penup()
art_turtle.forward(200)
art_turtle.pendown()
draw_flower()

# draw_flower()


art_turtle.hideturtle() # Get rid of the arrow showing the turtle location.

window.exitonclick()

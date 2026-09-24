#Programmer: Tyler Cannon
#Program name: Assignment #03
#Date written: 09/20/2026  
#Purpose: Create a multi-dimensional shape using coordinate points and lines with turtle

#Part 1, Python code

import turtle

#turtle configuration
turtle.setup(width=500, height=500)
turtle.title("multi dimension")
turtle.speed(3)
turtle.pensize(3)
turtle.pencolor("black")
turtle.hideturtle()

#draw the main outer shape
turtle.penup()
#top left corner
turtle.goto(-100,100) 
turtle.pendown()
#top center
turtle.goto(0,100) 
#far right center
turtle.goto(100,0)
#bottom right corner
turtle.goto(100,-100)
#bottom center
turtle.goto(0,-100)
#far left corner
turtle.goto(-100,0)
#top left corner, close the shape perimeter
turtle.goto(-100,100)

#draw the interior lines to make it 3d

#vertical line in the center
turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.goto(0,-100)
#horizonal line in the center
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
turtle.goto(100,0)
#diagonal line crossing from the top left to bottom right that creates the multi dimensional look
turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
turtle.goto(100,-100)

turtle.done()



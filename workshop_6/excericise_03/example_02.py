import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle named 'artist'
artist = turtle.Turtle()
artist.speed(5)

# Function to draw a heart
def draw_heart():
    artist.fillcolor("red")
    artist.begin_fill()
    artist.left(140)
    artist.forward(180)
    artist.circle(-90, 200)
    artist.setheading(60)
    artist.circle(-90, 200)
    artist.forward(180)
    artist.end_fill()

# Function to draw an arrow
def draw_arrow():
    artist.penup()
    artist.goto(0, 150)
    artist.pendown()
    artist.setheading(-30)
    artist.pencolor("black")
    artist.pensize(2)
    artist.forward(200)
    artist.setheading(210)
    artist.forward(50)
    artist.speed(10)
    artist.backward(50)
    artist.setheading(-70)
    artist.backward(50)
    artist.forward(50)

# Function to write text
def write_text():
    artist.penup()
    artist.goto(-100, -100)
    artist.pendown()
    artist.pencolor("black")
    artist.write("Made by: ARCE", font=("verdana", 20, "normal"))

# Draw the heart
draw_heart()

# Draw the arrow
draw_arrow()

# Write the text
write_text()

# Hide the turtle
artist.hideturtle()

# Keep the window open
turtle.done()

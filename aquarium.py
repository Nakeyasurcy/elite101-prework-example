import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("My Aquarium")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(0)
t.pensize(2)


# Function 1: Draw a circle
def draw_circle(radius, color):
    t.color("black", color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


# Function 2: Draw an oval
def draw_oval(width, height, color):
    t.color("black", color)
    t.begin_fill()

    # Draw a rounded oval shape
    t.forward(width - height)
    t.circle(height / 2, 180)
    t.forward(width - height)
    t.circle(height / 2, 180)

    t.end_fill()


# Function 3: Draw a triangle
def draw_triangle(size, color):
    t.color("black", color)
    t.begin_fill()

    for i in range(3):
        t.forward(size)
        t.left(120)

    t.end_fill()


# Function 4: Draw an orange clownfish
def draw_clownfish(x, y, size):
    # Draw the tail
    t.penup()
    t.goto(x - size / 2, y)
    t.setheading(180)
    t.pendown()
    draw_triangle(size / 2, "orange")

    # Draw the body
    t.penup()
    t.goto(x - size / 2, y - size / 4)
    t.setheading(0)
    t.pendown()
    draw_oval(size, size / 2, "orange")

    # Draw the eye
    t.penup()
    t.goto(x + size / 4, y)
    t.setheading(0)
    t.pendown()
    draw_circle(size / 15, "black")

    # Draw white stripes
    t.penup()
    t.goto(x - size / 6, y - size / 5)
    t.setheading(90)
    t.pendown()
    t.color("white")
    t.pensize(5)
    t.forward(size / 2)
    t.pensize(2)


# Function 5: Draw a blue fish
def draw_blue_fish(x, y, size, color):
    # Draw the tail
    t.penup()
    t.goto(x + size / 2, y)
    t.setheading(0)
    t.pendown()
    draw_triangle(size / 2, "yellow")

    # Draw the body
    t.penup()
    t.goto(x - size / 2, y - size / 4)
    t.setheading(0)
    t.pendown()
    draw_oval(size, size / 2, color)

    # Draw the eye
    t.penup()
    t.goto(x - size / 4, y)
    t.setheading(0)
    t.pendown()
    draw_circle(size / 15, "black")


# Function 6: Draw seaweed
def draw_seaweed(x, y, height, color):
    for i in range(3):
        t.penup()
        t.goto(x + i * 25, y)
        t.setheading(90)
        t.pendown()
        t.color(color)
        t.pensize(5)

        # Draw a tall seaweed stalk
        for j in range(3):
            t.forward(height / 6)
            t.left(15)
            t.forward(height / 6)
            t.right(30)

        t.pensize(2)


# Function 7: Draw bubbles
def draw_bubbles(x, y, count, color):
    for i in range(count):
        t.penup()
        t.goto(x, y + i * 25)
        t.setheading(0)
        t.pendown()
        draw_circle(5 + i, color)


# Function 8: Draw a starfish
def draw_starfish(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

    t.color("black", color)
    t.begin_fill()

    for i in range(5):
        t.forward(size)
        t.right(144)

    t.end_fill()


# Function 9: Draw a rock
def draw_rock(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    draw_oval(size, size / 2, color)


# Function 10: Draw coral
def draw_coral(x, y, color):
    t.color(color)
    t.pensize(7)

    for i in range(3):
        t.penup()
        t.goto(x + i * 15, y)
        t.setheading(90)
        t.pendown()
        t.forward(35)
        t.left(30)
        t.forward(20)
        t.backward(20)
        t.right(60)
        t.forward(20)

    t.pensize(2)


# Function 11: Draw the aquarium background
def draw_background():
    # Draw the sandy floor
    t.penup()
    t.goto(-380, -220)
    t.setheading(0)
    t.pendown()

    t.color("black", "khaki")
    t.begin_fill()

    for i in range(2):
        t.forward(760)
        t.right(90)
        t.forward(60)
        t.right(90)

    t.end_fill()


# Main program
def draw_aquarium():
    draw_background()

    # Draw two orange clownfish
    draw_clownfish(-130, 150, 100)
    draw_clownfish(30, 70, 65)

    # Draw two blue fish of different sizes and colors
    draw_blue_fish(170, 130, 90, "blue")
    draw_blue_fish(190, 40, 55, "gold")

    # Draw two starfish
    draw_starfish(-130, -170, 45, "hotpink")
    draw_starfish(100, -180, 25, "purple")

    # Draw seaweed on both sides
    draw_seaweed(-330, -210, 100, "green")
    draw_seaweed(260, -210, 80, "green")

    # Draw rocks
    draw_rock(-300, -210, 70, "gray")
    draw_rock(250, -210, 60, "gray")
    draw_rock(300, -210, 45, "gray")

    # Draw coral
    draw_coral(170, -200, "purple")

    # Draw bubbles in different locations
    draw_bubbles(-220, 30, 5, "white")
    draw_bubbles(80, 100, 4, "white")
    draw_bubbles(260, 70, 5, "white")


if __name__ == "__main__":
    draw_aquarium()
    t.hideturtle()
    turtle.done()


import turtle as turtle

done=False

print("Welcome to your drawing app! Select a shape you want to draw. After typing the number and hitting enter, the drawing app will draw the shape you selected.")


turtle.penup()
turtle.left(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(300)

turtle.pendown()

turtle.write("Drawing App!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()


turtle.write("To draw a shape, go to the Console tab and choose an option!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.pendown()


def draw_side(pen_color, length, rotation):
    turtle.pencolor(pen_color)
    turtle.forward(length)
    turtle.right(rotation)


def star(color):
    for i in range (0,5):
        draw_side (color,110,216)

def hexagon(color):
    for i in range (0,6):
        draw_side (color,100, 60)

def square(color):
    for i in range (0,4):
        draw_side (color,100, 90)

while not done:
    shape = input("Choose a shape: 1 for star, 2 for hexagon, 3 for square, 4 for done:  ")
   
    if shape == "4":
        done=True
    else:
        color = input("Enter a color:  ")
        if shape == "1":
            star(color)
        elif shape =="2":
            hexagon(color)
        else:
            square(color)







import turtle
from turtle import Turtle, Screen
import random

# from colors import random_colors

graph = Turtle()
graph.shape("triangle")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# for _ in range(4):
#     tama.forward(100)
#     tama.right(90)
# for _ in range(4):
#     tama.forward(100)
#     tama.left(90)
# for _ in range(4):
#     tama.backward(100)
#     tama.left(90)
# for _ in range(4):
#     tama.backward(100)
#     tama.right(90)

# for _ in range(15):
#     tama.forward(10)
#     tama.penup()
#     tama.forward(10)
#     tama.pendown()


# triangle
# for _ in range(3):
#     tama.forward(100)
#     tama.right(120)
# # square
# for _ in range(4):
#     tama.forward(100)
#     tama.right(90)
# # pentagon
# for _ in range(5):
#     tama.forward(100)
#     tama.right(72)
# # hexagon
# for _ in range(6):
#     tama.forward(100)
#     tama.right(60)
# # heptagon
# for _ in range(7):
#     tama.forward(100)
#     tama.right(51)
# # octagon
# for _ in range(8):
#     tama.forward(100)
#     tama.right(45)
#
# # nonagon
# for _ in range(9):
#     tama.forward(100)
#     tama.right(40)
#
# # decagon
# for _ in range(10):
#     tama.forward(100)
#     tama.right(36)

#
def shape_sides(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        graph.pensize(5)
        graph.speed(1)
        graph.forward(100)
        graph.right(angle)


for shape_side_number in range(3, 11):
    graph.color(random_color())
    shape_sides(shape_side_number)

# dotted line
# for _ in range(15):
#     graph.pensize(10)
#     graph.speed(1)
#     graph.color(random.choice(random_colors))
#     graph.forward(10)
#     graph.penup()
#     graph.forward(10)
#     graph.pendown()

# random movement:


directions = [0, 90, 180, 270]
for _ in range(500):
    graph.pensize(10)
    graph.color(random_color())
    graph.speed(0)
    graph.forward(20)
    graph.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()

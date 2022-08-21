import turtle
from turtle import Turtle, Screen
import random

graph = Turtle()
graph.shape("arrow")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    mixed_color = (r, g, b)
    return mixed_color


# for _ in range(4):
#     graph.forward(100)
#     graph.right(90)
# for _ in range(4):
#     graph.forward(100)
#     graph.left(90)
# for _ in range(4):
#     graph.backward(100)
#     graph.left(90)
# for _ in range(4):
#     graph.backward(100)
#     graph.right(90)
#
# for _ in range(15):
#     graph.forward(10)
#     graph.penup()
#     graph.forward(10)
#     graph.pendown()
#
#
# # triangle
# for _ in range(3):
#     graph.forward(100)
#     graph.right(120)
# # square
# for _ in range(4):
#     graph.forward(100)
#     graph.right(90)
# # pentagon
# for _ in range(5):
#     graph.forward(100)
#     graph.right(72)
# # hexagon
# for _ in range(6):
#     graph.forward(100)
#     graph.right(60)
# # heptagon
# for _ in range(7):
#     graph.forward(100)
#     graph.right(51)
# # octagon
# for _ in range(8):
#     graph.forward(100)
#     graph.right(45)

# Nonagon
# for _ in range(9):
#     graph.forward(100)
#     graph.right(40)
#
# # decagon
# for _ in range(10):
#     graph.forward(100)
#     graph.right(36)

#
# def shape_sides(number_of_sides):
#     angle = 360 / number_of_sides
#     for _ in range(number_of_sides):
#         graph.pensize(5)
#         graph.speed(0)
#         graph.forward(100)
#         graph.right(angle)


# for shape_side_number in range(3, 11):
#     graph.color(random_color())
#     shape_sides(shape_side_number)

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


# directions = [0, 90, 180, 270]
# for _ in range(500):
#     graph.pensize(10)
#     graph.color(random_color())
#     graph.speed(0)
#     graph.forward(20)
#     graph.setheading(random.choice(directions))

graph.speed(0)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        graph.color(random_color())
        graph.circle(100)
        graph.setheading(graph.heading() + size_of_gap)


draw_spirograph(3)

screen = Screen()
screen.exitonclick()

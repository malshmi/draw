#draw
from turtle import *
class Square:
    # to do Ira
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def show(self):
        turtle.up()
        turtle.goto(self.x, self.y)
        turtle.color(self.color)
        turtle.down()
        for _ in range (4):
            turtle.forward(self.size)
            turtle.left(90)
        turtle.begin_fill()

class Triangle:
    # to do Milana
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        
    def show(self):
        turtle.up()
        turtle.goto(self.x, self.y)
        turtle.color(self.color)
        turtle.down()
        for _ in range (3):
            turtle.forward(self.size)
            turtle.left(60)
        turtle.begin_fill()

class Parallelogram:
    def __init__(self, x, y, size, length, color, angle):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.angle = angle
        self.length = length
    def show(self):
        turtle.up()
        turtle.goto(self.x, self.y)
        turtle.color(self.color)
        turtle.down()
        for _ in range (2):
            turtle.forward(self.size)
            turtle.left(self.angle)
            turtle.forward(self.length)
            turtle.left(180-self.angle)
        turtle.begin_fill()
            

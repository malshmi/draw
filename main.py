#draw
import turtle
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
        turtle.down()
        for _ in range (4):
            turtle.forward(self.size)
            turtle.left(90)

class Triangle:
    # to do Milana
    def __init__(self, x, y, size, color,rectangle):
        pass
    def show(self):
        pass


class Diamond:
    # to do Alisa
    def __init__(self, x, y, size, color,rectangle):
        pass
    def show(self):
        pass

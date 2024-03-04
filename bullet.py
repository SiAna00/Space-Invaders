from turtle import *

class Bullet(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.up()
        self.shape("square")
        self.shapesize(stretch_wid=0.3, stretch_len=0.1)
        self.color(color)
        self.goto(x, y)


    def shoot(self, i):
        self.goto(self.xcor(), self.ycor() + i * 2)

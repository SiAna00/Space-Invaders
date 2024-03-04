from turtle import *

class Bullet(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.up()
        self.shape("square")
        self.shapesize(stretch_wid=None, stretch_len=0.1)
        self.color("white")
        self.goto(x, y)

        
    def shoot(self):
        self.goto(self.xcor(), self.ycor() + 20)

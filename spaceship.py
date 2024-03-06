from turtle import *

class SpaceShip(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.goto(0, -270)
        self.shape("square")
        self.shapesize(stretch_wid=None, stretch_len=3)
        self.color("white")


    def move_right(self):
        self.forward(20)

        if self.pos() == (-300.00, -270):
            self.setx(self.xcor() + 20)


    def move_left(self):
        self.backward(20)

        if self.pos() == (300.00, -270):
            self.setx(self.xcor() - 20)

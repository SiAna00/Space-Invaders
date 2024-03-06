from turtle import *
from bullet import Bullet

class SpaceShip(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.goto(0, -270)
        self.shape("square")
        self.shapesize(stretch_wid=None, stretch_len=3)
        self.color("white")
        self.my_bullets = []


    def move_right(self):
        self.forward(20)

        if self.pos() == (-300.00, -270):
            self.setx(self.xcor() + 20)


    def move_left(self):
        self.backward(20)

        if self.pos() == (300.00, -270):
            self.setx(self.xcor() - 20)

    
    def create_bullets(self):
        new_bullet = Bullet(self.xcor(), self.ycor(), "white")
        self.my_bullets.append(new_bullet)

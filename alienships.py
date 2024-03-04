from turtle import *
from bullet import Bullet

class AlienShips():
    def __init__(self):
        self.aliens = []
        start_pos_x = -280
        start_pos_y = 240

        for j in range(2):
            for i in range(19):
                new_alien = Turtle()
                new_alien.up()
                new_alien.right(90)
                new_alien.shape("triangle")
                new_alien.color("green")
                new_alien.goto(start_pos_x + i * 30, start_pos_y + j * 30)
                self.aliens.append(new_alien)


    def move(self):
        for individual in self.aliens:
            individual.forward(0.01)

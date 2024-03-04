from turtle import *

class Barrier():
    def __init__(self):
        self.bariers = []
        start_pos_x = -230
        start_pos_y = -100

        for i in range(4):
            new_barrier = Turtle()
            new_barrier.goto(start_pos_x + i * 150, start_pos_y)
            new_barrier.up()
            new_barrier.shape("square")
            new_barrier.shapesize(stretch_wid=None, stretch_len=4)
            new_barrier.color("white")
            self.bariers.append(new_barrier)
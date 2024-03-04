from turtle import *

class Barrier():
    def __init__(self):
        self.barriers = []
        self.create_barriers(-260, -100)

    def create_barriers(self, start_pos_x, start_pos_y):
        for j in range(4):
            for i in range(4):
                new_piece = Turtle()
                new_piece.up()
                new_piece.shape("square")
                new_piece.color("white")
                new_piece.goto(start_pos_x + i * 20 + j * 150, start_pos_y)
                self.barriers.append(new_piece)
from turtle import *

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.goto(-270, 270)
        self.color("white")
        self.score = 0
        self.write(f"Score: {self.score}", font=("Helvetica", 14, "bold"))

    def update_score(self):
        self.score += 10
        self.clear()
        self.write(f"Score: {self.score}", font=("Helvetica", 14, "bold"))
from turtle import *
from bullet import Bullet
import random

class AlienShips():
    def __init__(self):
        self.aliens = []
        self.create_alienships(-260, 220)
        self.all_alien_bullets = []

    def create_alienships(self, start_pos_x, start_pos_y):
        for j in range(2):
            for i in range(18):
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

    
    def create_bullet(self):
        random_chance = random.randint(1, 200)

        if random_chance == 1:
            random_alien = random.choice(self.aliens)
            new_bullet = Bullet(random_alien.xcor(), random_alien.ycor(), "green")
            self.all_alien_bullets.append(new_bullet)

    
    def shoot(self, i):
        for bullet in self.all_alien_bullets:
            bullet.goto(bullet.xcor(), bullet.ycor() + i * 0.5)

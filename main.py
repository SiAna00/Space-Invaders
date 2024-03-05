import os
from turtle import *
from alienships import AlienShips
from barriers import Barrier
from bullet import Bullet
from spaceship import SpaceShip


def create_my_bullet():
    global my_bullet
    my_bullet = Bullet(my_ship.xcor(), my_ship.ycor(), "white")


def getting_killed(creature, bullet):
    if creature.distance(bullet) <= 20:
        creature.reset()
        bullet.reset()


my_bullet = None

# Create and customize screen
screen = Screen()
screen.title("Space Invaders")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Create ship
my_ship = SpaceShip()

# Create alien army
aliens = AlienShips()

# Create protective barriers
barriers = Barrier()

# Move ship on key press
screen.onkeypress(my_ship.move_right, "Right")
screen.onkeypress(my_ship.move_left, "Left")
screen.onkeypress(create_my_bullet, "space")
screen.listen()

while True:
    screen.update()

    aliens.move()

    aliens.create_bullet()
    aliens.shoot(-2)

    if my_bullet != None:
        my_bullet.shoot(2)

        # Detect when aliens are hit with my_bullet
        for alien in aliens.aliens:
            getting_killed(alien, my_bullet)

        # Detect when my_bullet hits barriers
        for barrier in barriers.barriers:
            if my_bullet.distance(barrier) <= 20:
                barrier.reset()
                my_bullet.reset()

        # detect when my_bullet collides with alien bullets
        for bullet in aliens.all_alien_bullets:
            if bullet.distance(my_bullet) < 1:
                bullet.reset()
                my_bullet.reset()

    # Detect when my_ship is hit with alien bullets
    for bullet in aliens.all_alien_bullets:
        if my_ship.distance(bullet) < 20:
            my_ship.reset()
            bullet.reset()

    # Detect when alien bullets hit barriers
    for bullet in aliens.all_alien_bullets:
        for barrier in barriers.barriers:
            if bullet.distance(barrier) < 20:
                barrier.reset()
                bullet.reset()

screen.exitonclick()

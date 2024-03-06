import os
from turtle import *
from alienships import AlienShips
from barriers import Barrier
from bullet import Bullet
from spaceship import SpaceShip


def create_my_bullet():
    global my_bullets
    new_bullet = Bullet(my_ship.xcor(), my_ship.ycor(), "white")
    my_bullets.append(new_bullet)


def getting_killed(creature, bullet):
    if creature.distance(bullet) <= 20:
        creature.reset()
        bullet.reset()


my_bullets = [ ]

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

    if my_bullets != None:
        for bullet in my_bullets:
            bullet.shoot(2)

        # Detect when aliens are hit with my_bullet
        for alien in aliens.aliens:
            for bullet in my_bullets:
                getting_killed(alien, bullet)

        # Detect when my_bullet hits barriers
        for barrier in barriers.barriers:
            for bullet in my_bullets:
                if bullet.distance(barrier) <= 20:
                    barrier.reset()
                    bullet.reset()

        # Detect when my_bullet collides with alien bullets
        for bullet in aliens.all_alien_bullets:
            for my_bullet in my_bullets:
                if bullet.distance(my_bullet) < 2:
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

import os
from turtle import *
from alienships import AlienShips
from barriers import Barrier
from bullet import Bullet
from scoreboard import ScoreBoard
from spaceship import SpaceShip


def getting_killed(creature, bullet):
    if creature.distance(bullet) <= 20:
        creature.reset()
        bullet.reset()


# Create and customize screen
screen = Screen()
screen.title("Space Invaders")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Create scoreboard
scoreboard = ScoreBoard()

# Create ship
my_ship = SpaceShip()
my_bullets = my_ship.my_bullets

# Create alien army
aliens = AlienShips()

# Create protective barriers
barriers = Barrier()

# Move ship on key press
screen.onkeypress(my_ship.move_right, "Right")
screen.onkeypress(my_ship.move_left, "Left")
screen.onkeypress(my_ship.create_bullets, "space")
screen.listen()

while True:
    screen.update()

    aliens.move()
    aliens.create_bullet()
    aliens.shoot(-1)

    # Detect when my_ship is hit with alien bullets
    for bullet in aliens.all_alien_bullets:
        getting_killed(my_ship, bullet)

    # Detect when alien bullets hit barriers
    for bullet in aliens.all_alien_bullets:
        for barrier in barriers.barriers:
            if bullet.distance(barrier) < 20:
                barrier.reset()
                bullet.reset()

    if my_bullets != None:
        for bullet in my_bullets:
            bullet.shoot(2)

        # Detect when aliens are hit with my_bullet
        for alien in aliens.aliens:
            for bullet in my_bullets:
                """ getting_killed(alien, bullet) """
                if alien.distance(bullet) <= 20:
                    scoreboard.update_score()
                    alien.reset()
                    aliens.aliens.remove(alien)
                    bullet.reset()
                    

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

screen.exitonclick()

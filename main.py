from turtle import *
from alienships import AlienShips
from barriers import Barrier
from bullet import Bullet
from spaceship import SpaceShip


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

# Create my_bullet
def create_bullet():
    global my_bullet
    my_bullet = Bullet(my_ship.xcor(), my_ship.ycor())

# Create alien army
aliens = AlienShips()

# Create protective barriers
barriers = Barrier()

# Move ship on key press
screen.onkeypress(my_ship.move_right, "Right")
screen.onkeypress(my_ship.move_left, "Left")
screen.onkeypress(create_bullet, "Up")
screen.listen()

while True:
    screen.update()

    aliens.move()

    if my_bullet != None:
        my_bullet.shoot()

        # Detect when aliens are hit with my_bullet
        for alien in aliens.aliens:
            getting_killed(alien, my_bullet)

screen.exitonclick()

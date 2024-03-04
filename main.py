from turtle import *
from alienships import AlienShips
from barriers import Barrier
from bullet import Bullet
from spaceship import SpaceShip

# Create and customize screen
screen = Screen()
screen.title("Space Invaders")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Create ship
my_ship = SpaceShip()

# Create bullet
my_bullet = Bullet(my_ship.xcor(), my_ship.ycor())

# Create alien army
aliens = AlienShips()

# Create protective barriers
barriers = Barrier()

# Move ship on key press
screen.onkeypress(my_ship.move_right, "Right")
screen.onkeypress(my_ship.move_left, "Left")
screen.onkeypress(my_bullet.shoot, "Up")
screen.listen()

while True:
    screen.update()

    my_bullet.shoot()

screen.exitonclick()

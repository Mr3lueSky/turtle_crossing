import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
NUMBER_OF_CARS = 6

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
cars = [CarManager() for i in range(NUMBER_OF_CARS)]

screen.listen()
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_backward, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    obj = random.choice(cars)
    obj.move_fwd()
    if player.ycor() > 280:
        scoreboard.level_up()
        player.reset()
        obj.inc_speed()

    if obj.xcor() < -280:
        obj.reset_position()
    screen.update()

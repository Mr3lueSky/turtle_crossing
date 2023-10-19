from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.rt(-180)
        self.goto(320, random.randint(-250,250))

    def move_fwd(self):
        self.fd(STARTING_MOVE_DISTANCE)

from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, i=0):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.rt(-180)
        self.reset_position()
        self.color(random.choice(COLORS))
        self.speed = STARTING_MOVE_DISTANCE


    def move_fwd(self):
        self.fd(self.speed)

    def inc_speed(self):
        self.speed += 10

    def reset_position(self):
        self.goto(320, random.randint(-250,250))



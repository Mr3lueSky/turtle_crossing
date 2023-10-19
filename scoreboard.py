from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.ht()
        self.goto(-280,250)
        self.color("black")
        self.write(arg="Level: " + str(self.level), font=FONT)

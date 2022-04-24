from turtle import Turtle
import random as r

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = r.randint(-280, 280)
        random_y = r.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()
    def refresh(self):
        random_x = r.randint(-280, 280)
        random_y = r.randint(-280, 280)
        self.goto(random_x, random_y)
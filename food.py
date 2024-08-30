import imp
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.8,stretch_wid=0.8)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.rand_x=random.randint(-250,250)
        self.rand_y=random.randint(-250,250)
        self.goto(self.rand_x,self.rand_y)
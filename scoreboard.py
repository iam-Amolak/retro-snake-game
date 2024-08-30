from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Scoreboard:{self.score}",align="center",font=("Comic Sans MS",18,"bold"))

    def pt(self):
        self.score+=1
        self.clear()
        self.update()
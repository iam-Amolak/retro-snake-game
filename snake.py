import imp
from turtle import Turtle
positions=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snakes=[]
        self.createsnake()
        
    def createsnake(self):
        for pos in positions:
            self.add_snake(pos)
            

    def add_snake(self,position):
        snake=Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snakes.append(snake)

    def extend(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for seg in range(len(self.snakes)-1,0,-1):
            newx=self.snakes[seg-1].xcor()
            newy=self.snakes[seg-1].ycor()
            self.snakes[seg].goto(newx,newy)

        self.snakes[0].forward(20)
        # self.snakes[0].left(90)

    def up(self):
        if self.snakes[0].heading()!=DOWN:
            self.snakes[0].setheading(UP)

    def right(self):
        if self.snakes[0].heading()!=LEFT:
            self.snakes[0].setheading(0)

    def left(self):
        if self.snakes[0].heading()!=RIGHT:
            self.snakes[0].setheading(180)

    def down(self):
        if self.snakes[0].heading()!=UP:
            self.snakes[0].setheading(270)
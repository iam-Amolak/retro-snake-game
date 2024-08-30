from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake=Snake()
food=Food()
scores=Scoreboard()
# snake.createsnake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.down,"Down")

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.5)
    snake.move()  

    if snake.snakes[0].distance(food.rand_x,food.rand_y)<15:
        food.refresh()
        snake.extend()
        scores.pt()

    if snake.snakes[0].xcor()>280 or snake.snakes[0].xcor()<-290 or snake.snakes[0].ycor()>280 or snake.snakes[0].ycor()<-280:
        game_is_on=False
        snake.color("white")
        snake.write("Game Over!!",align="center",font=("Courier",18,"bold"))

    for seg in snake.snakes[1:]:
        if snake.snakes[0].distance(seg)<10:
            game_is_on=False
            snake.color("white")
            snake.write("Game Over!!",align="center",font=("Courier",18,"bold"))


screen.exitonclick()
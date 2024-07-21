from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)

is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    #testing collision with the food
    if snake.head.distance(food)<15:
        food.move_to_random()
        scoreboard.increase_score()
        snake.extend()
    #testing collision with the wall
    if snake.head.xcor()>295 or snake.head.xcor()<-295 or snake.head.ycor()>295 or snake.head.ycor()<-295:
        scoreboard.reset()
        snake.reset()
        
    #testing collision with the tail
    for seg in snake.segment[1:]:
        if snake.head.distance(seg)<10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
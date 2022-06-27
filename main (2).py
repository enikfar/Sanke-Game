from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from socreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
screen.listen()
snake = Snake()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")
speed = 0.2
food = Food()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()
        speed = speed / 1.1
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor(
    ) > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    for se in snake.segments[1:]:

        if snake.head.distance(se) < 10:
            scoreboard.reset()
      
            snake.reset()
            
            

screen.exitonclick

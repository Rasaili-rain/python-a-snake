from turtle import Screen, Turtle, textinput
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # turns of tracer

food = Food()
snake = Snake()
scoreboard = Scoreboard()

continue_playing = True

while continue_playing:
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # detect collison with food
        if snake.head.distance(food) < 20:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # detect colloision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.reset_score()
            snake.kill_snake()
            snake.create_snake()

        # detect collision with tail
        # if head collides with any segment
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.reset_score()
                snake.kill_snake()
                snake.create_snake()
    scoreboard.update_highscore()

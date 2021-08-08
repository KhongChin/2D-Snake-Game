from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    scoreboard.display_scoreboard()
    time.sleep(0.1)
    snake.move()
    scoreboard.clear()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() < -390 or snake.head.xcor() > 380 or snake.head.ycor() < -380 or snake.head.ycor() > 380:
        snake.reset()
        scoreboard.reset()
        scoreboard.display_scoreboard()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()
            scoreboard.display_scoreboard()

screen.exitonclick()

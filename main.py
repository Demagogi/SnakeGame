# # # # # # # # # # # # # # #  # # # #
#     giorgis  first game(snake)     #
#                                    #
# # # # # # # # # # # # # # # # # #  #
from turtle import Screen  # import Screen class from turtle module
from snake import Snake  # import Snake class from snake.py
from food import Food  # import Food class from food.py
from score import Score  # import Score class from score.py
import time  # import time module

screen = Screen()  # create screen object from Screen class and set it
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("kind of a Snake")
screen.tracer(0)

snake = Snake()  # create objects from classes
food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.score_update()
    # detect collision with wall
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290\
            or snake.snake_head.ycor() < -290:
        score.reset()
        snake.reset()
    # detect collision with the tail of the snake
    for segment in snake.segments[1:]:  # slicing
        if snake.snake_head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()

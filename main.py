####The project is divided into 7 steps
#### in the Day-20 we do first 3 steps of this projects and in this lesson we are doing the remaining 4 steps
import time      
from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()

# Detecting keys on Keyboard
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # to make the snake speed faster
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extends()
        score.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


    

screen.exitonclick()
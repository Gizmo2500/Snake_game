from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snakey the snake game!")

width = screen.window_width() / 2
height = screen.window_height() / 2
x = width - width
y = height - height
screen.tracer(0)
print(x)
print(y)

snakey = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()
screen.onkey(key="Up", fun=snakey.up)
screen.onkey(key="Down", fun=snakey.down)
screen.onkey(key="Left", fun=snakey.left)
screen.onkey(key="Right", fun=snakey.right)


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snakey.move()

    # Detect  collision with food
    if snakey.body[0].distance(food) < 15:
        # print("nom nom nom")
        score_board.update_score()
        snakey.extend()
        food.refresh()
    # Detect collision with wall
    if snakey.body[0].xcor() >= width or snakey.body[0].xcor() <= -width:
        score_board.reset_score()
        snakey.reset_snake()

    if snakey.body[0].ycor() >= height or snakey.body[0].ycor() <= -height:
        score_board.reset_score()
        snakey.reset_snake()

    # Detect collision with the tail with a list slice [1:]
    for segment in snakey.body[1:]:

        if snakey.body[0].distance(segment) < 5:
            score_board.reset_score()
            snakey.reset_snake()


screen.exitonclick()

from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_SPEED = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):

        snake = Turtle(shape='square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.body.append(snake)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):

        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)

        self.body[0].forward(MOVING_SPEED)

    def reset_snake(self):
        for part in self.body:
            part.goto(1000, 1000)
        self.body.clear()
        self.create_snake()

    def up(self):

        if self.body[0].heading() != DOWN:
            self.body[0].setheading(UP)

    def down(self):

        if self.body[0].heading() != UP:
            self.body[0].setheading(DOWN)

    def left(self):

        if self.body[0].heading() != RIGHT:
            self.body[0].setheading(LEFT)

    def right(self):

        if self.body[0].heading() != LEFT:
            self.body[0].setheading(RIGHT)

from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.score = 0
        with open('data.txt') as rfile:
            self.high_score = rfile.read()
        self.color("white")
        self.goto(0, 270)
        self.board()

    def board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > int(self.high_score):
            with open('data.txt', mode="w") as wfile:
                wfile.write(str(self.score))
            with open('data.txt') as rfile:
                self.high_score = rfile.read()
        self.score = 0
        self.board()

    def update_score(self):
        self.score += 1
        self.board()



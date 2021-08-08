from turtle import Turtle
Y = 370
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as high_score:
            self.high_score = int(high_score.read())

    def display_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.sety(Y)
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as high_score:
                high_score.write(f"{self.high_score}")
        self.score = 0

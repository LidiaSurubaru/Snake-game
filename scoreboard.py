from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.number = 0
        self.track_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
    def track_score(self):
        self.goto(x=0, y=270)
        self.clear()
        self.write(f"Score: {self.number}", move=False, align=ALIGNMENT, font=FONT)
        self.number += 1


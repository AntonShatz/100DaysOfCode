from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        if self.score == 0:
            self.write(F"Score : {self.score} חרושקה ", align=ALIGNMENT, font=FONT)
        elif self.score == 1:
            self.write(f"Score : {self.score} מאיה ", align=ALIGNMENT, font=FONT)
        elif self.score == 2:
            self.write(f"Score : {self.score} יא טיבה לובלו ", align=ALIGNMENT, font=FONT)




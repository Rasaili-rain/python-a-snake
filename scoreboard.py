from turtle import Turtle
ALIGNMENT ="center"
FONT = ('Arial', 16, 'normal')
FILE_NAME = "highscore.txt"


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score=0
        with open(FILE_NAME,"r") as file:
            self.high_score = int (file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE = {self.score}\t HIGH SCORE ={self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard() 

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        
    def update_highscore(self):
        with open(FILE_NAME,"w") as file:
            file.write(str(self.high_score))
    
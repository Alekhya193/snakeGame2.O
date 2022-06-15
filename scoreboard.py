from turtle import Turtle
Alignment="center"
Font=("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):

        super().__init__()
        self.score=0
        with open("data.txt") as data:
         self.highscore=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} ,Highscore={self.highscore}", False, Alignment, Font)

    def increase_score(self):
        self.score+=1
        self.update_score()


    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_score()



    # def game_over(self):
    #     self.goto(0, 0)
    #     # self.clear()
    #     self.write("Game over!!!", False, Alignment, Font)
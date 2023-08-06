from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./Score\highscore.txt") as file:
            self.high_score = int(file.read())
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}Highscore: {self.high_score}", align = "center", font = ("Arial", 24, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.color("#EE4B2B")
        self.write(f"Game over!" , align = "center" , font = ("Arial" , 24 , "normal"))

        
    def reset(self):
            if self.score > self.high_score:
                self.high_score = self.score
            self.score = 0
            self.color("red")
            self.hideturtle()
            self.penup()
            self.goto(0, 260)
            self.update_score()
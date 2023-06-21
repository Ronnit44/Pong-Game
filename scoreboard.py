from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_1 = 0
        self.player_2 = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.player_1,align="center", font=("Courier", 50, "normal"))
        self.goto(100,200)
        self.write(self.player_2,align="center", font=("Courier", 50, "normal"))

    def player1_point(self):
        self.player_1 += 1
        self.update_scoreboard()

    def player2_point(self):
        self.player_2 += 1
        self.update_scoreboard()

    def game_over1(self):
        self.goto(0,0)
        self.write("Player1 Won", align="center",font=("Arial", 24, "normal"))

    def game_over2(self):
        self.goto(0, 0)
        self.write("Player2 Won", align="center", font=("Arial", 24, "normal"))
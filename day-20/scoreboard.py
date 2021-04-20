from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")
SCORE_HEIGHT = 220
SCORE_WEIGHT = 0


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(SCORE_WEIGHT, SCORE_HEIGHT)
        self.update_scoreboard()
        print("Scoreboardのinit")

    def update_scoreboard(self):
        self.clear()
        print(self.position())
        self.penup()    # 質問：なんで私のはこの二行がないと、scoreboardのscoreが右にずれていく？⭐️
        self.goto(SCORE_WEIGHT, SCORE_HEIGHT)
        self.write(f" {self.l_score} : {self.r_score}", True, align=ALIGNMENT, font=FONT)

    def increase_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_r_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", True, align=ALIGNMENT, font=FONT)




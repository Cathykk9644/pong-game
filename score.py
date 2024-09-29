from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.left_score = 0
    self.right_score = 0
    self.score_limit = 10
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.goto(-100, 200)
    self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
    self.goto(100, 200)
    self.write(self.right_score, align="center", font=("Courier", 80, "normal"))
  
  def increase_left_score(self):
    self.left_score += 1
    self.update_scoreboard()
    self.check_game_over()
  
  def increase_right_score(self):
    self.right_score += 1
    self.update_scoreboard()
    self.check_game_over()
  
  def check_game_over(self):
        if self.left_score >= self.score_limit or self.right_score >= self.score_limit:
            self.game_over()

  def game_over(self):
        self.goto(0, 0)
        winner = "Player Left" if self.left_score >= self.score_limit else "Player Right"
        self.write(f"Game Over! {winner} wins!", align="center", font=("Courier", 24, "normal"))
        global game_running
        print("Game Over! Setting game_running to False.")
        game_running = False
     

  
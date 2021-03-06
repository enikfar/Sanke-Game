from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.penup()
    with open("data.txt") as file:

      self.high_score = int(file.read())
    
    self.goto(0,265)
    
    self.update_scoreboard()
    self.hideturtle()
  def update_scoreboard(self):
    self.write(f"Score:{self.score} High Score: {self.high_score}",align="center",font=("Arial",24,"normal"))



  # def game_over(self):
  #   self.goto(0,0)
  #   self.write(f"Game Over",align="center",font=("Arial",24,"normal"))



  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open("data.txt",mode = "w") as file:
        file.write(str(self.high_score))
      self.score = 0
      self.clear()
      self.update_scoreboard()

      
  def increase_score(self):
      self.score += 1
      self.clear()
      self.update_scoreboard()
      
      
   

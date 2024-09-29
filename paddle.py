from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, position):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.penup()
    self.goto(position)

  def move_up(self):
     # Check if the new y position is less than 250 (the upper limit)
     if self.ycor() < 250:
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

  def move_down(self):
      # Check if the new y position is greater than -250 (the lower limit)
      if self.ycor() > -250:
          new_y = self.ycor() - 30
          self.goto(self.xcor(), new_y)
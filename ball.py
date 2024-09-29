from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.penup()

  def move(self, dx, dy):
    new_x = self.xcor() + dx
    new_y = self.ycor() + dy
    self.goto(new_x, new_y)

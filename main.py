from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0) # turn off animations

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_running = True
while game_running:
  time.sleep(0.1)
  screen.update()
  ball.move()

  # Detect collision with wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  # Detect collision with paddles
  if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()

  # Detect Right Paddle misses
  if ball.xcor() > 380:
    ball.reset_position()
    scoreboard.increase_left_score()
  
  # Detect left Paddle misses
  if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.increase_right_score()
  
screen.exitonclick()


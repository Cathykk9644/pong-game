from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0) # turn off animations

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

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
    ball.bounce()

  # Detect collision with paddles
  if ball.distance(right_paddle) < 50 and (ball.xcor() > 330 and ball.xcor() < 350):
    ball.x_move *= -1

  if ball.distance(left_paddle) < 50 and (ball.xcor() < -330 and ball.xcor() > -350):
    ball.x_move *= -1

screen.exitonclick()


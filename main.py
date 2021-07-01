from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.title("Beast Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
screen.listen()

game_playing = True

screen.onkeypress(key="Up", fun=r_paddle.up)
screen.onkeypress(key="Down", fun=r_paddle.down)
screen.onkeypress(key="w", fun=l_paddle.up)
screen.onkeypress(key="s", fun=l_paddle.down)

while game_playing:
    screen.update()
    ball.add_movement()

    # detect collision with top and bottom of the screen
    if ball.ycor() > 275 or ball.ycor() < -275:
        # this means the ball has hit either top or bottom
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # if one of the players misses the ball reset the ball to the center
    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.l_point()
    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.r_point()

    time.sleep(ball.move_speed)

screen.exitonclick()

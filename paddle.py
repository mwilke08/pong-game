from turtle import Turtle

PADDLE_SPEED = 20

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.goto(x_pos, y_pos)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_y_pos = self.ycor() + PADDLE_SPEED
        self.sety(new_y_pos)

    def down(self):
        new_y_pos = self.ycor() - PADDLE_SPEED
        self.sety(new_y_pos)

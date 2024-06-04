from turtle import Turtle,Screen
from ball import Ball
import time
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)
scoreboard = Scoreboard()


right_block = Turtle()
left_block  = Turtle()
right_block.shape("square")
right_block.color("red")
right_block.shapesize(stretch_len=1,stretch_wid=5)
right_block.penup()
right_block.goto(x=370,y=0)
ball = Ball()
left_block.shape("square")
left_block.color("blue")
left_block.shapesize(stretch_len=1,stretch_wid=5)
left_block.penup()
left_block.goto(x=-370,y=0)

def move_up():
    new_y_posi = right_block.ycor() + 60
    if new_y_posi <= UPPER_LIMIT:
        right_block.goto(right_block.xcor(), new_y_posi)


def move_down():
    new_y_posi = right_block.ycor() - 60
    if new_y_posi >= LOWER_LIMIT:
        right_block.goto(right_block.xcor(), new_y_posi)


def go_up():
    new_y_posi = left_block.ycor() + 60
    if new_y_posi <= UPPER_LIMIT:
        left_block.goto(left_block.xcor(), new_y_posi)


def go_down():
    new_y_posi = left_block.ycor() - 60
    if new_y_posi >= LOWER_LIMIT:
        left_block.goto(left_block.xcor(), new_y_posi)





screen.listen()
screen.onkeypress(move_up,"Up")
screen.onkeypress(move_down,"Down")
screen.onkeypress(go_up,"w")
screen.onkeypress(go_down,"s")

game_running = True
while game_running:
    screen.update()
    time.sleep(ball.moving_speed)
    ball.move()
    #detecting collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y_axis()

    #detecting collisions with the blocks
    if ball.distance(right_block) < 50 and ball.xcor() > 340 or ball.distance(left_block) < 50 and ball.xcor() < -340:
        ball.bounce_x_axis()


    #if ball misses the block
    if ball.xcor() > 380:
        scoreboard.player1_point()
        ball.restart()
    if ball.xcor() < -380:
        scoreboard.player2_point()
        ball.restart()

    if scoreboard.player_1 == 5:
        game_running = False
        scoreboard.game_over1()

    if scoreboard.player_2 == 5     :
        game_running = False
        scoreboard.game_over2()




screen.exitonclick()

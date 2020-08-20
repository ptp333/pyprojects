import turtle   # allows us to use the turtles(graphics) library 
import winsound     # for sound

# backgroud
win = turtle.Screen()   #create a graphical window
win.title("Pong by Rahul Pundir")   # title of screen
win.bgcolor("black")   # set background color as black
win.setup(width = 800, height = 600)   # dimensions of graphical window
win.tracer(0)   # it's for speed optimization so that the user doesn't have to see every drawing step in a complicated image      

# Score
score1 = 0      # player A initial score
score2 = 0      # player B initial score

# Left Side Paddle
paddle1 = turtle.Turtle()   #using method
paddle1.speed(0)    # to run a max speed
paddle1.shape("square")     # shape of paddle
paddle1.color("white")      # color of paddle
paddle1.shapesize(stretch_wid = 5, stretch_len = 1)     # for size
paddle1.penup()     #so the turtle will not draw a line as it moves
paddle1.goto(-350,0)    # for position(x,y)

# Right Side Paddle
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid = 5, stretch_len = 1)
paddle2.penup()
paddle2.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = -0.1

# Score Board
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()    
pen.goto(0, 260)
pen.write("Player A: {} Player B: {}".format(score1,score2),align="center",font=("Courier", 24, "normal"))

# Left Side Paddle Movement
def paddle1_up():   # for up
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1_down():   # for down
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)


# Right Side Paddle Movement
def paddle2_up():   # for up
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle2_down():   # for down
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)


# Keyboard button functionaity for paddles movement
win.listen()
win.onkeypress(paddle1_up,"w")
win.onkeypress(paddle1_down,"s")
win.onkeypress(paddle2_up,"Up")
win.onkeypress(paddle2_down,"Down")


# Main Game loop
while True:
    win.update()   # to update screen everytime
    # for ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball Border functionality
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("jump.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("jump.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score1,score2),align="center",font=("Courier", 24, "normal"))
        winsound.PlaySound("drop.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score1,score2),align="center",font=("Courier", 24, "normal"))
        winsound.PlaySound("drop.wav", winsound.SND_ASYNC)
        
    # paddle and ball collision functionality
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("catch.wav", winsound.SND_ASYNC)
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("catch.wav", winsound.SND_ASYNC)

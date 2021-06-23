#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
canvas=turtle.Screen()
canvas.title("#Playing Ping Pong#Having Fun")
canvas.bgcolor("black")
canvas.setup(width=800,height=600)
leftscore=0
rightscore=0
a=turtle.Turtle()
a.goto(-350,0)
a.speed(10)
a.shape("square")
a.shapesize(stretch_wid=5,stretch_len=1)
a.color("white")
a.penup()

b=turtle.Turtle()
b.goto(350,0)
b.speed(10)
b.shape("square")
b.shapesize(stretch_wid=5,stretch_len=1)
b.color("white")
b.penup()

c=turtle.Turtle()
c.speed(10)
c.shape("circle")
c.color("white")
c.write("Welcome to Ping Pong \n\n Press anywhere to start \n",False,align="center",font=("Arial",15,"bold"))
c.penup()
c.dx=0
c.dy=0
d=turtle.Turtle()
d.shape("square")
d.shapesize(stretch_wid=1000,stretch_len=0.1)
d.pencolor("white")
d.clear()
d.goto(0,280)
d.write("Press e for easy mode, m for normal mode and h for hard mode",False,align="center")
d.goto(0,-300)
d.goto(0,-250)
d.write("Score",False,align="center",font=("Arial",15,"bold"))
d.goto(0,-280)
d.write("Paddle A:{}  Paddle B:{}".format(leftscore,rightscore),False,align="center",font=("Arial",15,"bold"))
canvas.delay(1)
def start():
    c.clear()
    d.clear()
    d.write("Paddle A:{}  Paddle B:{}".format(leftscore,rightscore),False,align="center",font=("Arial",15,"bold"))
    c.dx=5
    c.dy=5
def easy():
    c.dx=3
    c.dy=3
def medium():
    c.dx=5
    c.dy=5
def hard():
    c.dx=7
    c.dy=7
def a_mov_up():
    y=a.ycor()
    y=y+20
    a.sety(y)

def b_mov_up():
    y=b.ycor()
    y=y+20
    b.sety(y)
def a_mov_down():
    y=a.ycor()
    y=y-20
    a.sety(y)
def b_mov_down():
    y=b.ycor()
    y=y-20
    b.sety(y)
#keyboard operations
canvas.listen()
canvas.onkeypress(b_mov_up,"8")
canvas.onkeypress(b_mov_down,"2")
canvas.onkeypress(a_mov_up,"Up")
canvas.onkeypress(a_mov_down,"Down")
canvas.onkeypress(easy,"e")
canvas.onkeypress(medium,"m")
canvas.onkeypress(hard,"h")
canvas.onkeypress(start,"space")
while True:
    canvas.update()
    c.setx(c.xcor() + c.dx)
    c.sety(c.ycor() + c.dy)
   
   
    if c.xcor()<-350:
        c.goto(0,0)
        c.dx*=-1
        rightscore+=1
        d.clear()
        d.write("Paddle A:{}  Paddle B:{}".format(leftscore,rightscore),False,align="center",font=("Arial",15,"bold"))
    elif c.xcor()>350:
        c.goto(0,0)
        c.dx*=-1
        leftscore+=1
        d.clear()
        d.write("Paddle A:{}  Paddle B:{}".format(leftscore,rightscore),False,align="center",font=("Arial",15,"bold"))
    elif c.ycor()>290:
        c.sety(290)
        c.dy*=-1
    elif c.ycor()<-290:
        c.sety(-290)
        c.dy*=-1
    #if c.xcor()==a.xcor() and c.ycor()==a.ycor()
    if c.xcor() < -340 and c.ycor() < a.ycor() + 50 and c.ycor() > a.ycor() - 50:
        c.dx *= -1 
        


    
    elif c.xcor() > 340 and c.ycor() < b.ycor() + 50 and c.ycor() > b.ycor() - 50:
        c.dx *= -1

turtle.done()


# In[1]:


import turtle
import playsound  # pip install playsound
score_a = 0
score_b = 0
canvas = turtle.Screen()
canvas.title("The Greatest Pong Game Ever")
canvas.bgcolor("#0B5345")
canvas.screensize(600,400)
pa = turtle.Turtle()
pa.color('#48C9B0')
pa.penup()
pa.goto(-250,0)
pa.pendown()
pa.shape('square')
pa.shapesize(stretch_wid=5, stretch_len=1)
pb = turtle.Turtle()
pb.color('#48C9B0')
pb.penup()
pb.goto(250,0)
pb.pendown()
pb.shape('square')
pb.shapesize(stretch_wid=5, stretch_len=1)
ball=turtle.Turtle()
ball.color('#abc123')
ball.penup()
ball.goto(0,0)
ball.pendown()
ball.shape('circle')
ball.penup()
text = turtle.Turtle()
text.penup()
text.goto(0,150)
text.pendown()
text.color("blue")
text.write("READY",align="center",font=("Arial",24,"normal"))
text.hideturtle()
canvas.delay(1000)
text.clear()
text.write("GO!",align="center",font=("Arial",24,"normal"))
canvas.delay(1000)
text.clear()
text.write("Paddle A: {}  Paddle B: {}".format(score_a,score_b),align="center",font=("Arial",24,"normal"))
canvas.delay(1)
speedx=4
speedy=4
def pa_mov_up():
    pa.sety(pa.ycor()+20)
def pa_mov_down():
    pa.sety(pa.ycor()-20)
def pb_mov_up():
    pb.sety(pb.ycor()+20)
def pb_mov_down():
    pb.sety(pb.ycor()-20)
canvas.listen() ## screen will start listening to the keyboard
canvas.onkeypress(pa_mov_up,"w")
canvas.onkeypress(pa_mov_down,"e")
canvas.onkeypress(pb_mov_up,"i")
canvas.onkeypress(pb_mov_down,"o")
while True:
    ball.setx(ball.xcor()+speedx)  #take the current x cor of ball and add 2 pixels to it
    ball.sety(ball.ycor()+speedy)
    if ball.xcor() > 300:
        ball.goto(0,0)
        speedx *= -1
        score_a+=1
        text.clear()
        text.write("Paddle A: {}  Paddle B: {}".format(score_a,score_b),align="center",font=("Arial",24,"normal"))
    elif ball.xcor()< -300:
        ball.goto(0,0)
        speedx *= -1
        score_b+=1
        text.clear()
        text.write("Paddle A: {}  Paddle B: {}".format(score_a,score_b),align="center",font=("Arial",24,"normal"))
    
    if ball.ycor() > 200:
        speedy *= -1
    
    elif ball.ycor() <-200:
        speedy *= -1
    
    if ball.xcor()>240 and (pb.ycor()+50> ball.ycor()> pb.ycor()-50):
        ball.setx(240)
        speedx *= -1
        playsound.playsound("bounce.wav")
    elif ball.xcor()<-240 and (pa.ycor()+50> ball.ycor() > pa.ycor()-50):
        ball.setx(-240)
        speedx *= -1
        playsound.playsound("bounce.wav")
turtle.done()


# In[ ]:





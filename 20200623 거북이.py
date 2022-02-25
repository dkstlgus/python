#거북이
import turtle as t
import random as r
import time as i

playing = True
time1 = int(i.time())

def up():
    t.setheading(90)
    t.forward(10)
    
def down():
    t.setheading(270)
    t.forward(10)
    
def right():
    t.setheading(0)
    t.forward(10)
    
def left():
    t.setheading(180)
    t.forward(10)
    
def space():
    t.clear()
    
def play():
    if playing:
        t.ontimer(play,100)
    if t.distance(ts) < 15:
        x = r.randint(-230,230)
        y = r.randint(-230,230)
        ts.goto(x,y)

    time = int(i.time())
    
def message(m1):
    t.clear()
    t.write(m1,False,"center",("",20))
    t.goto(0,200) 
    t.home()
    

        
t.setup(500,500)
t.bgcolor("black")
t.shape()
t.color("cyan")



ts = t.Turtle()
ts.shape("circle")
ts.up()
ts.goto(-100,150)
ts.color("green")



t.onkeypress(up,"Up")
t.onkeypress(down,"Down")
t.onkeypress(right,"Right")
t.onkeypress(left,"Left")
t.onkeypress(space,"space")
t.listen()
play()






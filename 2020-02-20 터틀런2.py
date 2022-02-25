#터틀런2
import turtle as t
import random

    
score = 0   #점수 저장 변수
playing = False     #현제 게임 플레이 하고 있는지 확인 변수

#적 거북이
te = t.Turtle() #새 거북이 생성코드
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0 , 200)

#먹이
ts = t.Turtle()
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0 ,-200)

def turn_right():
    t.setheading(0)
def turn_up():
    t.setheading(90)
def turn_left():
    t.setheading(180)
def turn_down():
    t.setheading(270)
 
def d():
    te.setheading(0)
def w():
    te.setheading(90)
def a():
    te.setheading(180)
def s():
    te.setheading(270)
def start():
    global playing
    if playing== False:
        playing = True
        t.clear()
        play()
def play():
    global score
    global playing
    t.forward(10)   #내 거북이 속도
    te.forward(10)   #적 거북이 속도
    if t.distance(te) <12: #주인공과 적과의 거리가 12보다 작으면
        text = "Score:" + str(score)    #str - 문자열
        message("Game Over",text)
        playing = False
        score = 0
    if t.distance(ts) <12:
        score = score + 1
        t.write(score)
        x = random.randint(-230,230)
        y = random.randint(-230,230)
        ts.goto(x,y)
    if playing:
        t.ontimer(play,100)
    if te.distance(ts) <12:
        te.forward(-250)
        
def fire():
    t.forward(20)

def message(m1,m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1,False,"center",("",20))
    t.goto(0,-100)
    t.write(m2,False,"center",("",20))
    t.home()        #내거북이 처음위치로 이동하는 함수
    
    
#내 자신 거북이

t.title("Turtle Run")   #t.title 윈도우 창 이름
t.bgcolor("orange")
t.setup(500,500)
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(d, "d")
t.onkeypress(w, "w")
t.onkeypress(s, "s")
t.onkeypress(a, "a")
t.onkeypress(start, "space")
t.onkeypress(fire, "Tab")

t.listen()  # onkeypress 사용하려면 listen()를 써야 작동
message("Turtle Run", "[Space]")





#두더지게임
import pygame as p
import time as t
import random as r

p.init()    #파이게임 초기화
w = (255,255,255)   #빛의3원색(RGB)
size = (1000,700)    #(가로,세로)
sc = p.display.set_mode(size)   #해상도
p.display.set_caption("마우스 연타")
playing = True
#글씨 화면 업로드
font = p.font.SysFont("malgungothic",30)
s = 0
#시작시간
st = t.time()
#게임오버 글씨
font1 = p.font.SysFont("malgungothic",70)
#두더지 이미지불러오기
do =  p.image.load("mole.png")
d_rect = do.get_rect(left = 450 , top = 325)
#복제하기

while playing:  #while Ture - 계속 반복하기
    
    for event in p.event.get(): #사용자가 뭘 누르는지 감지
        if event.type == p.QUIT: #게임창 x버튼을 누르면
            playing = False #계속반복 종료
            p.quit()    #게임창 종료
            quit() #sell창 종료
        if event.type == p.MOUSEBUTTONDOWN:
            if d_rect.collidepoint(event.pos[0],event.pos[1]):  #두더지와 마우스 충돌
                d_rect = do.get_rect(left = r.randint(0,900) , top = r.randint(0,600))
                s = s + 1
                print(s)


                
    sc.fill(w)#배경색
    sc.blit(do,d_rect)
    #흐르는 시간
    af = t.time()
    second = 60 - (af - st)


    
    text = font.render("점수: {}".format(s),True,(0,0,0))
    text1 = font.render("남은시간: {}".format(int(second)),True,(0,0,0))
    text2 = font1.render("Game Over",True,(255,0,0))
    if second <= 0:
        playing = False
    
    sc.blit(text,(850,5))
    sc.blit(text1,(370,10))
    p.display.flip()  #화면 업데이트

#60초 클릭게임
import pygame as p
import time as t

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



while playing:  #while Ture - 계속 반복하기
    
    for event in p.event.get(): #사용자가 뭘 누르는지 감지
        if event.type == p.QUIT: #게임창 x버튼을 누르면
            playing = False #계속반복 종료
            p.quit()    #게임창 종료
            quit() #sell창 종료
        if event.type == p.MOUSEBUTTONDOWN:
            s = s + 1
            print(s)
        if event.type == p.MOUSEBUTTONUP:
            print("")

        if event.type == p.KEYDOWN:
            s = s + 1
            print(s)
        
    sc.fill(w)#화면 업데이트 기능
    #흐르는 시간
    af = t.time()
    second = 60 - (af - st)
    print(int(second))

    
    text = font.render("클릿횟수: {}".format(s),True,(0,0,0))
    text1 = font.render("남은시간: {}".format(int(second)),True,(0,0,0))
    text2 = font1.render("Game Over",True,(255,0,0))
    
    sc.blit(text,(370,250))
    sc.blit(text1,(370,50))
    if int(second) <= 0:
        sc.blit(text2,(370,250))
        playing = False #계속반복 종료
    p.display.flip()  #화면 업데이트

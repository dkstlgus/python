import pygame as p

p.init()    #파이게임 초기화
w = (255,255,255)   #빛의3원색(RGB)
size = (800,600)    #(가로,세로)
sc = p.display.set_mode(size)   #해상도
p.display.set_caption("두더지")
playing = True

#두더지
do = p.image.load("mole.png")
d_rect = do.get_rect(left = 370 , top = 250)   #left = x , top = y
#임시
s = 0




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
            print("연타!")


        
    sc.fill(w)
    sc.blit(do,d_rect)
    p.display.flip()  #화면 업데이트

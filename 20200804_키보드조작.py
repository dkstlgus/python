import pygame as p

p.init  #라이브러리 초기화
white = (255,255,255)   #rgb빛의 3원색
size = (600,800)    #가로,세로
sc = p.display.set_mode(size)   #해상도크기설정
p.display.set_caption("키보드조작")    #게임창제목 display:해상도설정
playing = True

a = 0

while playing: #while True - 계속 반복하기

    for event in p.event.get():  #사용자가 뭘 누르는지 감지
        if event.type == p.QUIT:    #게임창x버튼을누르면
            playing = False
            p.quit()    #게임창 종료
            quit()  #shell 창 종료


                #a += 1 #a = a + 1
                #print(a)

        if event.type == p.KEYDOWN: #키보드를 눌렀을때
            if event.key == p.K_UP: #윗 방향키를 눌렀을때
                print("윗 방향키를 눌렀습니다.")
                a += 1 #a = a + 1
                print(a)
            if event.key == p.K_DOWN: #아래 방향키를 눌렀을때
                print("아래  방향키를 눌렀습니다.")
            if event.key == p.K_LEFT: #왼쪽 방향키를 눌렀을때
                print("왼쪽 방향키를 눌렀습니다.")
            if event.key == p.K_RIGHT: #오른쪽 방향키를 눌렀을때
                print("오른쪽 방향키를 눌렀습니다.")

        if event.type == p.KEYUP: #키보드를 때었을때
            if event.key == p.K_UP: #윗 방향키를 때었을때
                print("윗 방향키를 때었습니다.")
            if event.key == p.K_DOWN: #아래 방향키를 때었을때
                print("아래  방향키를 때었습니다.")
            if event.key == p.K_LEFT: #왼쪽 방향키를 때었을때
                print("왼쪽 방향키를 때었습니다.")
            if event.key == p.K_RIGHT: #오른쪽 방향키를 때었을때
                print("오른쪽 방향키를 때었습니다.")









            
    sc.fill(white)  #배경화면색 설정
    p.display.flip()    #화면업데이트

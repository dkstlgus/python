import pygame as p

p.init()    #파이게임 초기화
w = (255,255,255)   #빛의3원색(RGB)
size = (1250,750)    #(가로,세로)
sc = p.display.set_mode(size)   #해상도
p.display.set_caption("게임판")
playing = True
fps = p.time.Clock()
#공 이미지 불러오기
ball = p.image.load("rhd2.png")
b_rect = ball.get_rect(left = 0 , top = 250)
b_y = 0 #중력관련 변수
b_x = 0 #공 움직임 관련 변수
#벽돌 생성
block = p.image.load("qur.png")
bl_list = []
bl_rect = block.get_rect(left = 0 , top = 500)
bl_list.append(bl_rect)
bl_rect = block.get_rect(left = 175 , top = 450)
bl_list.append(bl_rect)
bl_rect = block.get_rect(left = 350 , top = 400)
bl_list.append(bl_rect)
while playing:
    fps.tick(60)    #초당 120개 사진이 지나간다 프레임
    for event in p.event.get(): #사용자가 뭘 누르는지 감지
        if event.type == p.QUIT: #게임창 x버튼을 누르면
            playing = False #계속반복 종료
            p.quit()    #게임창 종료
            quit() #sell창 종료
        if event.type == p.KEYDOWN:
            if event.key == p.K_RIGHT:
                b_x = 3
            if event.key == p.K_LEFT:
                b_x = -3
        if event.type == p.KEYUP:
            if event.key == p.K_RIGHT:
                b_x = 0
            if event.key == p.K_LEFT:
                b_x = 0



                
    #공 좌우 움직이는 코드
    b_rect.left += b_x
                
    sc.fill(w)
    sc.blit(ball,b_rect)
    #공튕기기
    b_rect.top += b_y
    b_y += 0.4
    #만약에 땅에 닿았으면
    if b_rect.top >= 730:
        b_y = -12

    if b_rect.left <= 5:
        b_rect.left = 5
    if b_rect.left >= 1210:
        b_rect.left = 1210
    #벽돌 화면 업로드
    for bl_rect in bl_list:
        sc.blit(block,bl_rect)
    #공,발판 충돌
    for bl_rect in bl_list:
        if b_rect.colliderect(bl_rect):
            b_y = -7.5







    
    p.display.flip()  #화면 업데이트

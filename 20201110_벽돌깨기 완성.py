#벽돌깨기
import pygame as p

p.init()    #파이게임 초기화
w = (255,255,255)   #빛의3원색(RGB)
size = (500,900)    #(가로,세로)
sc = p.display.set_mode(size)   #해상도
p.display.set_caption("게임판")
playing = True
play = True
#판 이미지 변수에 넣기
pan = p.image.load("판2.png")
p_rect = pan.get_rect(left = 200 , top = 825)
p_x = 0 #판 움직임 관련 변수
#fps
clock = p.time.Clock()
#공
ball = p.image.load("pow.png")
b_rect = ball.get_rect (left = 200 , top = 450)
#공 속도 관련 변수
b_x = 5
b_y = 5
t = 0
#벽돌 이미지 업로드
block = p.image.load("벽돌2.png")
b_list = []
for x in range(10):
    for y in range(5):
        bl_rect = block.get_rect(left= x*50 , top = 50*y)
        b_list.append(bl_rect)
#점수
font = p.font.SysFont("malgungothic",20)
score = 0
    
while playing:
    clock.tick(60)  #초당 프레임 60
    for event in p.event.get(): #사용자가 뭘 누르는지 감지
        if event.type == p.QUIT: #게임창 x버튼을 누르면
            playing = False #계속반복 종료
            p.quit()    #게임창 종료
            quit() #sell창 종료
        if event.type == p.KEYDOWN:
            if event.key == p.K_LEFT:
                p_x = -5
            if event.key == p.K_RIGHT:
                p_x = 5
        if event.type == p.KEYUP:
            if event.key == p.K_LEFT:
                p_x = 0
            if event.key == p.K_RIGHT:
                p_x = 0






    p_rect.left += p_x #판 움직이는 코드
    #("+="뜻) p_rect.left = p_rect.left + p_x
    if p_rect.left <= -101:
        p_rect.left = 500
    if p_rect.left >= 501:
        p_rect.left = -100
    sc.fill(w)  #배경화면 색깔
    #공 이미지 업로드
    sc.blit(p.transform.rotate(ball,t),b_rect)
    t += 5
    #공 움직이기
    b_rect.top += b_y
    b_rect.left += b_x
    if b_rect.left >= 475:
        b_x = -b_x
    if b_rect.left <= 0:
        b_x = -b_x
    if b_rect.top <= 0:
        b_y = -b_y
    if b_rect.top >= 875:
        playing = False
    #공 , 판 충돌
    if b_rect.colliderect(p_rect):
        b_y = -b_y
    #벽돌
    for bl_rect in b_list:
        sc.blit(block,bl_rect)
    #벽돌 깨기
    for bl_rect in b_list:
        if bl_rect.colliderect(b_rect):
            b_list.remove(bl_rect)
            b_y = 5
            score += 1
    #점수
    text = font.render("점수: {}".format(score),True,(0,0,0))
    sc.blit(text,(425,860))


    #판 이미지 업로드
    sc.blit(pan,p_rect)
    p.display.flip()  #화면 업데이트

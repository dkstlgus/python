#슈팅게임
import pygame as p#파이게임생성
import random as r

p.init()  #라이브러리 초기화
white = (255,255,255)   #rgb빛의 3원색
size = (500,800)    #가로,세로
sc = p.display.set_mode(size)   #해상도크기설정
p.display.set_caption("슈팅게임")    #게임창제목 display:해상도설정
playing = True
#비행기 이미지 변수에 넣기
plane = p.image.load("우주선.png")
p_rect = plane.get_rect(left = 200 , top = 700)
p_x = 0
#배경 변수넣기
bg = p.image.load("우주.png")
#미사일 변수 넣기
bullet = p.image.load("미사일.png")
b_list =  []
#적군등장
en = p.image.load("공.png")
en_list =  []
for x in range(5):
    en_rect = en.get_rect(left = r.randint(0,400), top = 0)
    en_list.append(en_rect) #리스트에 추가
#점수 시스템
score = 0
font = p.font.SysFont("malgungothic",25)    #(폰트 종류,글씨크기)
#스킬 이미지
skill = p.image.load("ㅋ.png")
s_rect = skill.get_rect(left = 0 , top = 0)
skill_list = []
skillpoint = 3
while playing: #while True - 계속 반복하기

    for event in p.event.get():  #사용자가 뭘 누르는지 감지
        if event.type == p.QUIT:    #게임창x버튼을누르면
            playing = False
            p.quit()    #게임창 종료
            quit()  #shell 창 종료
        if event.type == p.KEYDOWN:
            if event.key == p.K_LEFT:
                p_x = -10
            if event.key == p.K_RIGHT:
                p_x = 10
            if event.key == p.K_SPACE:
                b_rect = bullet.get_rect(left = p_rect.left + 38 , top = p_rect.top)
                b_list.append(b_rect)
            if event.key == p.K_z:
                if skillpoint > 0:
                    s_rect = skill.get_rect(left = p_rect.left -75 , top = p_rect.top)
                    skill_list.append(s_rect)
                    skillpoint = skillpoint - 1
                
        if event.type == p.KEYUP:
            if event.key == p.K_LEFT:
                p_x = 0
            if event.key == p.K_RIGHT:
                p_x = 0






    p_rect.left += p_x    
    sc.fill(white)

    #배경화면색 설정
    sc.blit(bg,(0,0))
    #비행기 화면 업로드
    sc.blit(plane,(p_rect))
    if p_rect.left <= -100: #비행기가 오른쪽벽에 닿으면
        p_rect.left = 499 #비행기 좌표를 499으로 위치시키기 
    if p_rect.left >= 500:
        p_rect.left = -99  #비행기 좌표를 -99으로 위치시키기 

    #미사일 화면 업로드
    for b_rect in b_list:
        sc.blit(bullet,b_rect)  #미사일 화면 업로드
        b_rect.top -= 10
        if b_rect.top <= 0: #총알이 위쪽벽에 닿으면
            b_list.remove(b_rect)
    #적군 화면 업로드
    for en_rect in en_list:
        sc.blit(en,en_rect)
        en_rect.top += 4
        if en_rect.top >= 800:
            en_rect.left =  r.randint(0,400)    #적군 x좌표를 랜덤으로
            en_rect.top = 0   #적군 y좌표를 0으로 (위쪽으로 이동)
            score -= 5
    #미사일 적군 충돌
  
    for en_rect in en_list:
        for b_rect in b_list:
                 if b_rect.colliderect(en_rect):    #미사일과 적군이 충돌한다면
                    en_list.remove(en_rect) #적군삭제
                    b_list.remove(b_rect)   #미사일 삭제
                    en_rect = en.get_rect(left = r.randint(0,400), top = 0)
                    en_list.append(en_rect) #리스트에 추가
                    score += 1

    text = font.render("점수 : {}".format(score),True,(255,255,255))
    sc.blit(text,(0,0))
                        
    for s_rect in skill_list:
        sc.blit(skill,s_rect)
        s_rect.top -= 5
        if s_rect.top <= -200:
            skill_list.remove(s_rect)

    for en_rect in en_list:
        for s_rect in skill_list:
                if s_rect.colliderect(en_rect):    #미사일과 적군이 충돌한다면
                    en_list.remove(en_rect) #적군삭제
                    en_rect = en.get_rect(left = r.randint(0,400), top = 0)
                    en_list.append(en_rect) #리스트에 추가
                    score += 1

        
    p.display.flip()    #화면 업데이트 기능

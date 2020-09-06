import pygame
pygame.init()
gray=(119,118,110)
black=(0,0,0)
red=(255,0,0)
green=(3,92,13)
bright_green=(40,252,3)
blue=(3,19,252)
bright_blue=(3,190,252)
bright_red=(252,69,3)
display_width=800
display_height=600
import time
gamedisplays=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("CAR GAME")
clock=pygame.time.Clock()
carimg=pygame.image.load('car1.png')
backgroundpic=pygame.image.load("grass.jpg")
yellow_strip=pygame.image.load("yellow strip.jpg")
strip=pygame.image.load("strip.jpg")
intro_background=pygame.image.load("gameb.jpg")
instruction_background=pygame.image.load("x.png")
car_width=60
import random
pause=False


def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(intro_background,(0,0))
        largetext=pygame.font.Font("freesansbold.ttf",115)
        textsurf,textrect=text_objects("CAR GAME",largetext)
        textrect.center=(350,100)
        gamedisplays.blit(textsurf,textrect)
        button("START",150,520,100,50,green,bright_green,"play")
        button("QUIT",550,520,100,50,red,bright_red,"quit")
        button("INSTRUCTION",300,520,200,50,blue,bright_blue,"intro")
        pygame.display.update()
        clock.tick(50)


def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==quit:
                pygame.quit()
                quit()

        gamedisplays.blit(instruction_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        htextsurf,htextrect=text_objects("This is a car game in which you need to dodge the coming cars.",smalltext)
        htextrect.center=((350),(200))
        textsurf,textrect=text_objects("INTRODUCTION",largetext)
        textrect.center=((400),(100))
        gamedisplays.blit(htextsurf,htextrect)
        gamedisplays.blit(textsurf,textrect)
        btextsurf,btextrect=text_objects("ARROW LEFT : LEFT TURN",smalltext)
        btextrect.center=((150),(400))
        htextsurf, htextrect = text_objects("ARROW RIGHT : RIGHT TURN", smalltext)
        htextrect.center = ((150), (450))
        ptextsurf, ptextrect = text_objects("PAUSE : P", smalltext)
        ptextrect.center = ((150), (350))
        stextsurf, stextrect = text_objects("CONTROLS", mediumtext)
        stextrect.center = ((350), (300))
        gamedisplays.blit(btextsurf,btextrect)
        gamedisplays.blit(stextsurf, stextrect)
        gamedisplays.blit(htextsurf, htextrect)
        gamedisplays.blit(ptextsurf, ptextrect)
        button("BACK",600,450,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)

def unpaused():
    global pause
    pause =False

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gamedisplays, ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                countdown()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
            elif action=="unpause":
                unpaused()
            elif action=="pause":
                paused()


    else:
        pygame.draw.rect(gamedisplays, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textsurf, textrect = text_objects(msg, smallText)
    textrect.center = ( (x+(w/2)), (y+(h/2)) )
    gamedisplays.blit(textsurf, textrect)


def paused():
    global pause

    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background,(0,0))
        largetext=pygame.font.Font("freesansbold.ttf",115)
        textsurf,textrect=text_objects("PAUSED",largetext)
        textrect.center=((display_width/2),(display_height/2))
        gamedisplays.blit(textsurf,textrect)
        button("CONTINUE",150,450,150,50,green,bright_green,"unpause")
        button("RESTART",350,450,150,50,blue,bright_blue,"play")
        button("MAIN MENU",550,450,150,50,red,bright_red,"menu")
        pygame.display.update()
        clock.tick(30)


def countdown_background():
    font=pygame.font.SysFont(None,25)
    x=(display_width*0.45)
    y=(display_height*0.8)
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic,(700,0))
    gamedisplays.blit(backgroundpic,(700,200))
    gamedisplays.blit(backgroundpic,(700,400))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,200))
    gamedisplays.blit(yellow_strip,(400,300))
    gamedisplays.blit(yellow_strip,(400,400))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,500))
    gamedisplays.blit(yellow_strip,(400,0))
    gamedisplays.blit(yellow_strip,(400,600))
    gamedisplays.blit(strip,(163,200))
    gamedisplays.blit(strip,(163,0))
    gamedisplays.blit(strip,(163,100))
    gamedisplays.blit(strip,(680,100))
    gamedisplays.blit(strip,(680,0))
    gamedisplays.blit(strip,(680,200))
    gamedisplays.blit(carimg,(x,y))
    text=font.render("DODGED: 0",True, black)
    score=font.render("SCORE: 0",True,red)
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))
    button("PAUSE",650,0,150,50,blue,bright_blue,"pause")

def countdown():
    countdown=True

    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("3",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("2",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("1",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("GO!!!",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()


def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load("car.jpg")
    elif obs==1:
        obs_pic=pygame.image.load("e3.png")
    elif obs==2:
        obs_pic=pygame.image.load("car1.png")
    elif obs==3:
        obs_pic=pygame.image.load("CAR6.jpg")
    elif obs==4:
        obs_pic=pygame.image.load("CAR7.jpg")
    elif obs==5:
        obs_pic=pygame.image.load("CAR4.jpg")
    elif obs==6:
        obs_pic=pygame.image.load("CAR5.jpg")
    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))


def score_system(passed,score):
    font=pygame.font.SysFont(None,25)
    text=font.render("passed"+str(passed),True,red)
    score=font.render("Score"+str(score),True,red)
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))



def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()


def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    message_display("YOU CRASHED")


def background():
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic,(700,0))
    gamedisplays.blit(backgroundpic,(700,200))
    gamedisplays.blit(backgroundpic,(700,400))
    gamedisplays.blit(yellow_strip,(400,0))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,200))
    gamedisplays.blit(yellow_strip,(400,300))
    gamedisplays.blit(yellow_strip,(400,400))
    gamedisplays.blit(yellow_strip,(400,500))
    gamedisplays.blit(strip,(163,0))
    gamedisplays.blit(strip,(163,100))
    gamedisplays.blit(strip,(163,200))
    gamedisplays.blit(strip,(163,300))
    gamedisplays.blit(strip,(680,0))
    gamedisplays.blit(strip,(680,100))
    gamedisplays.blit(strip,(680,200))
    gamedisplays.blit(strip,(680,300))


def car(x,y):
    gamedisplays.blit(carimg,(x,y))


def game_loop():
    global pause
    pause=True
    x=(display_width*0.45)
    y=(display_height*0.8)
    x_change=0
    obstacle_speed=11
    obs=0
    x_change=0
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-750
    obs_width=60
    obs_height=126
    passed=0
    level=0
    score=0

    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_a:
                    obstacle_speed+=2
                if event.key==pygame.K_b:
                    obstacle_speed-=2
                if event.key==pygame.K_p:
                    pause=True
                    paused()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0


        x+=x_change

        gamedisplays.fill(gray)
        background()
        obs_starty-=(obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        car(x,y)
        score_system(passed,score)
        if x>680-car_width or x<175:
            crash()
        if x>display_width-(car_width+110) or x<175:
            crash()
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(0,7)
            passed=passed+1
            score=passed*10
            if int(passed)%10==0:
                level=level+1
                obstacle_speed+2
                largetext = pygame.font.Font("freesansbold.ttf",80)
                textsurf,textrect = text_objects("LEVEL"+str(level),largetext)
                textrect.center = ((display_width/2),(display_height/2))
                gamedisplays.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(2)

        if y<obs_starty+obs_height:
             if x>obs_startx and x<obs_startx+obs_width or x+car_width>obs_startx and x+car_width<obs_startx+obs_width:
                    crash()
        button("Pause",650,0,150,50,blue,bright_blue,"pause")
        
        pygame.display.update()
        clock.tick(60)
intro_loop()
game_loop()
pygame.quit()
quit()

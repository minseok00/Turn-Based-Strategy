import pygame

import char
import button

#pygame 초기화
pygame.init()

#RGB
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

#실행창
size = (800, 600)
screen = pygame.display.set_mode(size)

background = pygame.image.load('background.png')

#게임 이름, 아이콘
pygame.display.set_caption("Iron Man Vs Hulk")

icon = pygame.image.load('avengers_.png')
pygame.display.set_icon(icon)


#플레이어
font = pygame.font.SysFont("notosanscjkkr",30)
text_ironman = font.render('Iron Man', True, black)

player = char.player_char()

playerImg = pygame.image.load('superhero_ironman.png')
playerX = 80
playerY = 270

def player_pos():
    screen.blit(playerImg, (playerX, playerY))

#컴퓨터
text_hulk = font.render('Hulk', True, black)

computer = char.computer_char()

comImg = pygame.image.load('superhero_hulk.png')
comX = 660
comY = 270

def computer_pos():
    screen.blit(comImg, (comX, comY))

#Versus_Img
VersusImg = pygame.image.load('versus_.png')

VersusX = 370
VersusY = 35

def Versus_pos():
    screen.blit(VersusImg, (VersusX, VersusY))

#버튼 설정

move_right_key = button.button(40, 475, 70, 100)
move_left_key = button.button(150, 475, 70, 100)
move_up_key = button.button(260, 475, 70, 100)
move_down_key = button.button(370, 475, 70, 100)

att_side_key = button.button(480, 475, 70, 100)
att_cross_key = button.button(590, 475, 70, 100)
att_circle_key = button.button(700, 475, 70, 100)

rightImg = pygame.image.load('right_arrow64.png')
rightX = 45
rightY = 490
def right_pos():
    screen.blit(rightImg, (rightX, rightY))

leftImg = pygame.image.load('left_arrow64.png')
leftX = 150
leftY = 490
def left_pos():
    screen.blit(leftImg, (leftX, leftY))

upImg = pygame.image.load('up_arrow64.png')
upX = 263
upY = 490
def up_pos():
    screen.blit(upImg, (upX, upY))

downImg = pygame.image.load('down_arrow64.png')
downX = 373
downY = 495
def down_pos():
    screen.blit(downImg, (downX, downY))

sideattImg = pygame.image.load('side_att.png')
sideX = 483
sideY = 490
def sideatt_pos():
    screen.blit(sideattImg,(sideX, sideY))

crossattImg = pygame.image.load('cross_att.png')
crossX = 595
crossY = 490
def crossatt_pos():
    screen.blit(crossattImg,(crossX, crossY))

circleattImg = pygame.image.load('circle_att.png')
cirX = 703
cirY = 490
def circleatt_pos():
    screen.blit(circleattImg,(cirX, cirY))

#게임 판
x_move = 180
y_move = 90
def boundary():
    global x_move
    global y_move
    if playerX < 45 or playerX > 765 or comX < 45 or comX > 765:
        x_move = 0
    elif playerY < 150 or playerY > 450 or comY < 150 or comY > 450:
        y_move = 0


#게임 루프
def RunGame():

    running = True
    clock = pygame.time.Clock()

    while running:
        global playerX
        global playerY

        #FPS
        clock.tick(100)

        #pygame 화면설정
        screen.blit(background, (0, 0))

        pygame.draw.rect(screen, black, [45, 150, 180, 100], 1)
        pygame.draw.rect(screen, black, [45, 250, 180, 100], 1)
        pygame.draw.rect(screen, black, [45, 350, 180, 100], 1)
        pygame.draw.rect(screen, black, [225, 150, 180, 100], 1)
        pygame.draw.rect(screen, black, [225, 250, 180, 100], 1)
        pygame.draw.rect(screen, black, [225, 350, 180, 100], 1)
        pygame.draw.rect(screen, black, [405, 150, 180, 100], 1)
        pygame.draw.rect(screen, black, [405, 250, 180, 100], 1)
        pygame.draw.rect(screen, black, [405, 350, 180, 100], 1)
        pygame.draw.rect(screen, black, [585, 150, 180, 100], 1)
        pygame.draw.rect(screen, black, [585, 250, 180, 100], 1)
        pygame.draw.rect(screen, black, [585, 350, 180, 100], 1)

        pygame.draw.rect(screen, black, [40, 475, 70, 100], 3)
        pygame.draw.rect(screen, black, [150, 475, 70, 100], 3)
        pygame.draw.rect(screen, black, [260, 475, 70, 100], 3)
        pygame.draw.rect(screen, black, [370, 475, 70, 100], 3)
        pygame.draw.rect(screen, black, [480, 475, 70, 100], 3)
        pygame.draw.rect(screen, black, [590, 475, 70, 100], 3)
        pygame.draw.rect(screen, black, [700, 475, 70, 100], 3)

        right_pos()
        left_pos()
        up_pos()
        down_pos()
        sideatt_pos()
        crossatt_pos()
        circleatt_pos()

        screen.blit(text_ironman, (45, 10))
        screen.blit(text_hulk, (460, 10))

        pygame.draw.rect(screen, red, [45, 35, 300, 30])
        pygame.draw.rect(screen, blue, [45, 75, 300, 30])
        pygame.draw.rect(screen, red, [460, 35, 300, 30])
        pygame.draw.rect(screen, blue, [460, 75, 300, 30])

        Versus_pos()
        player_pos()
        computer_pos()

        # pygame 이벤트 설정
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if move_right_key.isOver(pos):
                    player.move_right()
                    boundary()
                    screen.blit(playerImg, (playerX + x_move, playerY))
                    playerX = playerX + x_move
                elif move_left_key.isOver(pos):
                    player.move_left()
                    boundary()
                    screen.blit(playerImg, (playerX - x_move, playerY))
                    playerX = playerX - x_move
                elif move_up_key.isOver(pos):
                    player.move_up()
                    boundary()
                    screen.blit(playerImg, (playerX, playerY - y_move))
                    playerY = playerY - y_move
                elif move_down_key.isOver(pos):
                    player.move_down()
                    boundary()
                    screen.blit(playerImg, (playerX, playerY + y_move))
                    playerY = playerY + y_move

                elif att_side_key.isOver(pos):
                    player.att_side()
                elif att_cross_key.isOver(pos):
                    player.att_cross()
                elif att_circle_key.isOver(pos):
                    player.att_circle()

        pygame.display.flip()

RunGame()

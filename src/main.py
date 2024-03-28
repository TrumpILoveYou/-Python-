"""
游戏运行入口，包含必要的交互
"""
import sys
from pygame.locals import *
from GameRunner import *
from ConstGameParameter import GAME_SIZE
import pygame
import time
pygame.init()
icon = pygame.image.load("picture\other\icon.png")
pygame.display.set_caption("植物大战僵尸")
pygame.display.set_icon(icon)
DS = pygame.display.set_mode(GAME_SIZE)
background_image = Image(r"picture\other\MainMenu.png", (0, 0), size=GAME_SIZE)
button_image = Image(r"picture\other\Adventure_1.png", (0, 0), pos=(670, 80), size=(450, 200))
darkbutton_image = Image(r"picture\other\Adventure_0.png", (0, 0), pos=(672, 78), size=(450, 200))
victory_image=Image(r"picture\other\victory.png", (0, 0), pos=(GAME_SIZE[0]/10,GAME_SIZE[1]/10), size=(GAME_SIZE[0]*8/10,GAME_SIZE[1]*8/10))
lose_image=Image(r"picture\other\lose.png", (0, 0), pos=(GAME_SIZE[0]/10,GAME_SIZE[1]/10), size=(GAME_SIZE[0]*8/10,GAME_SIZE[1]*8/10))

#开场动画
def OpeningDisplay():
    background_image.draw(DS)
    button_image.draw(DS)
    pygame.display.update()
    button_clicked = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 670 <= x <= 1120 and 80 <= y <= 280:  # 如果点击按钮区域
                    button_clicked = True
                    break
        if button_clicked:
            # 进入游戏的代码
            print("进入游戏")
            break

#画面切换
def smoothSwitch():
    pretime = 0
    dex = 0
    case = 1
    while dex < 8:
        if time.time() - pretime > 0.2 and case == 1:
            pretime = time.time()
            button_image.draw(DS)
            pygame.display.update()
            dex += 1
            case = 2
        if time.time() - pretime > 0.2 and case == 2:
            pretime = time.time()
            darkbutton_image.draw(DS)
            pygame.display.update()
            dex += 1
            case = 1

#失败显示
def showLose():
    pretime = time.time()
    lose_image.draw(DS)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if time.time() - pretime > 5:
            break

#胜利显示
def showVictory():
    pretime = time.time()
    victory_image.draw(DS)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if time.time() - pretime > 5:
           break

#新的一局游戏启动器
def newGame():
    game = Game(DS)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.mouseClickHandler(event.button)
        game.update()
        game.draw()
        pygame.display.update()
        if game.leftzombie<=0:
            showVictory()
            pygame.quit()
            sys.exit()
        for zombie in game.zombies:
            if zombie.pos[0]<30:
                showLose()



OpeningDisplay()
smoothSwitch()
newGame()









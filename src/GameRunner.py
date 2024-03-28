"""
游戏运行的主要文件
"""
import random
import time
import pygame.mouse
from ImageProcessor import Image
from ConstGameParameter import *
from Characters import ZombieBase
from Characters import *
from Items import Shovel

# id_class:由id索引到类
id_class = {
    "SUNFLOWER": SunFlower,
    "PEASHOOTER": PeaShooter,
    "REPEATERPEA": RepeaterPea,
    "THREEPEASHOOTER": ThreePeaShooter,
    "SHOVEL": Shovel,
    "ZOMBIEEATING": ZombieEating
}


# 游戏类，本游戏的主要类
class Game(object):
    def __init__(self, ds):

        self.pretime = time.time()
        self.bombShowRemain = []
        self.ds = ds
        self.background = Image(GAME_BACKGROUND_PATH, (0, 0), size=GAME_SIZE)
        self.chooserbackground = Image(CHOOSER_BACKGROUND_PATH, pos=(250, 0), size=CHOOSER_SIZE)
        self.shovelBox = Image(SHOVELBOX_PATH, pos=(890, 10), size=SHOVELBOX_SIZE)
        self.bulletbombs = []
        self.planttrackimages = []

        for id in ObjectParameter:
            cardPath = ObjectParameter[id]["CARD_PATH"]
            if not cardPath == None:
                self.planttrackimages.append(
                    Image(ObjectParameter[id]["CARD_PATH"],
                          pos=(CARD_POS[0] + ObjectParameter[id]["CARD_BIAS"] * (CARD_SIZE[0] + CARD_GAP), CARD_POS[1]),
                          size=CARD_SIZE))
        self.plants = {}  # 位置坐标与植物
        self.summons = []
        self.hasPlant = []
        self.zombies = []
        self.nextclick = False
        self.needMoveWithMouse = False
        self.nextId = None
        self.totalGold = ORIGIN_GOLD
        self.leftzombie = ZOMBIE_NUM
        self.leftzombieToAdd = ZOMBIE_NUM

        self.goldFont = pygame.font.SysFont('Times New Roman', 14)
        self.instruct = pygame.font.Font(None, 30)
        self.zombieGenerateTime = 0
        for i in range(GRID_SIZE[0]):
            tempt = []
            for j in range(GRID_SIZE[1]):
                tempt.append(0)
            self.hasPlant.append(tempt)

    # 文字类信息显示
    def renderFont(self):
        for gold_limit, color in gold_textcolor.items():
            if gold_limit[1] >= self.totalGold and self.totalGold >= gold_limit[0]:
                lenth = -len(str(gold_limit[0])) + 3
                textImage = self.goldFont.render("%s%d" % (lenth * " ", self.totalGold), True, color)
                self.ds.blit(textImage, GOLD_DISPLAY_POS)
                break
        textImage = self.instruct.render("Right-click to select a card", True, INSTRUCT_COLOR)
        self.ds.blit(textImage, (1000, 15))
        textImage = self.instruct.render("Left-click to plant", True, INSTRUCT_COLOR)
        self.ds.blit(textImage, (1000, 35))

    # 将图片展示到画布
    def draw(self):
        self.background.draw(self.ds)
        self.chooserbackground.draw(self.ds)
        self.shovelBox.draw(self.ds)
        for bulletbomb in self.bombShowRemain:
            bulletbomb.draw(self.ds)

        for planttrack in self.planttrackimages:
            planttrack.draw(self.ds)
        if self.needMoveWithMouse:
            self.tracePlant.draw(self.ds)
        for plant in self.plants.values():
            plant.draw(self.ds)
        for zombie in self.zombies:
            zombie.draw(self.ds)
        for summon in self.summons:
            summon.draw(self.ds)
        self.renderFont()

    # 更新图片
    def update(self):
        if self.needMoveWithMouse:
            self.tracePlant.update(pos=(pygame.mouse.get_pos()[0] - 35, pygame.mouse.get_pos()[1] - 35))
        self.background.update()
        self.chooserbackground.update()
        self.shovelBox.update()
        while len(self.bulletbombs):
            bulletbomb = self.bulletbombs.pop()
            self.bombShowRemain.append(bulletbomb)
            bulletbomb.update()
        if time.time() - self.pretime > 1:
            self.pretime = time.time()
            if len(self.bombShowRemain):
                del self.bombShowRemain[0]
        for planttrack in self.planttrackimages:
            planttrack.update()
        for plant in self.plants.values():
            plant.update()
            if plant.hasSummon():
                summon = plant.doSummon()
                if isinstance(summon, tuple):
                    self.summons.extend(list(summon))
                else:
                    self.summons.append(summon)
        for summon in self.summons:
            summon.update()
        for zombie in self.zombies:
            zombie.update()
        if time.time() - self.zombieGenerateTime > ZOMBIE_BORN_CD:
            self.zombieGenerateTime = time.time()
            self.addZombie(ZOMBIE_BORN_POS, random.randint(0, GRID_COUNT[1] - 1))
        self.checkSummonVSZombie()
        self.checkPlantVSZombie()

    # 检验植物和僵尸的战斗
    def checkPlantVSZombie(self):
        for plant in self.plants:
            for zombie in self.zombies:
                if self.plants[plant].isCollide(zombie) and isinstance(zombie,
                                                                       ZombieEating) and time.time() - zombie.timeOfEat >= 1:
                    self.plants[plant].hp -= 1
                    zombie.timeOfEat = time.time()
                if self.plants[plant].isCollide(zombie) and isinstance(zombie, ZombieEating) and self.plants[
                    plant].hp <= 0:
                    x, y = self.getCoordinateByPos(self.plants[plant].pos)
                    del self.plants[plant]
                    self.hasPlant[x][y] = 0
                    self.zombies.remove(zombie)
                    newzombie = ZombieBase("ZOMBIE", pos=zombie.pos)
                    newzombie.hp = zombie.getHP()
                    self.zombies.append(newzombie)
                    return
                if self.plants[plant].isCollide(zombie) and not isinstance(zombie, ZombieEating):
                    eatingzombie = ZombieEating("ZOMBIEEATING", pos=zombie.pos)
                    eatingzombie.hp = zombie.getHP()
                    self.zombies.remove(zombie)
                    self.zombies.append(eatingzombie)
                    eatingzombie.timeOfEat = time.time()
        for zombie in self.zombies:
            if isinstance(zombie, ZombieEating):
                hasPlantNear = False
                for plant in self.plants:
                    if self.plants[plant].isCollide(zombie):
                        hasPlantNear = True
                if hasPlantNear == False:
                    self.zombies.remove(zombie)
                    newzombie = ZombieBase("ZOMBIE", pos=zombie.pos)
                    newzombie.hp = zombie.getHP()
                    self.zombies.append(newzombie)

    # 检验召唤物和僵尸的战斗
    def checkSummonVSZombie(self):
        for summon in self.summons:
            for zombie in self.zombies:
                if summon.isCollide(zombie):
                    self.fight(summon, zombie)
                    if zombie.hp <= 0:
                        self.leftzombie -= 1
                        self.zombies.remove(zombie)
                    if summon.hp <= 0:
                        self.summons.remove(summon)
                        if summon.id == "PEABULLET":
                            self.bulletbombs.append(
                                Image(BULLET_BOMB_PATH, pos=(summon.pos[0] + BULLET_BOMB_BIAS, summon.pos[1]),
                                      size=(52, 46)))
                    return

    # 增加僵尸
    def addZombie(self, x, y):
        pos = self.FromCoordinateToGetPos(x, y, "ZOMBIE")
        if self.leftzombieToAdd > 0:
            self.zombies.append(ZombieBase("ZOMBIE", pos))
            self.leftzombieToAdd -= 1

    # 战斗
    def fight(self, a, b):
        while True:
            a.hp -= b.attack
            b.hp -= a.attack
            if b.hp <= 0:
                return True
            if a.hp <= 0:
                return False

    # 鼠标点击处理器
    def mouseClickHandler(self, button):
        mousePos = pygame.mouse.get_pos()
        for id in ObjectParameter:
            if self.clickOnTheCard(mousePos, id):
                if self.totalGold < ObjectParameter[id]["VALUE"]:
                    return
                self.tracePlant = id_class[id](id, mousePos)
                self.needMoveWithMouse = True
                self.nextclick = True
                self.nextId = id
                return True
        if self.checkLoot(mousePos):
            return
        if self.nextclick and button == 1:
            self.checkAddPlant(mousePos, self.nextId)
            self.nextclick = False
            self.needMoveWithMouse = False
        return

    # 检测是否拾取
    def checkLoot(self, mousePos):
        for summon in self.summons:
            if not getParameter(summon.id, "CAN_LOOT"):
                continue
            rect = summon.getRect()
            if rect.collidepoint(mousePos):
                self.summons.remove(summon)
                self.totalGold += getParameter(summon.id, "VALUE")
                return True
        return False

    # 检测是否增加植物
    def checkAddPlant(self, mousePos, objID):
        x, y = self.getCoordinateByPos(mousePos)
        if not (0 <= x < GRID_COUNT[0] and 0 <= y < GRID_COUNT[1]):
            return
        if self.hasPlant[x][y] == 1:
            if objID == "SHOVEL":
                del self.plants[(x, y)]
                self.hasPlant[x][y] = 0
            return
        if self.totalGold < ObjectParameter[objID]["VALUE"]:
            return
        self.hasPlant[x][y] = 1
        self.totalGold -= ObjectParameter[objID]["VALUE"]
        self.addPlant(x, y, objID)

    # 增加植物
    def addPlant(self, x, y, id):
        if id == "SHOVEL":
            return
        pos = self.FromCoordinateToGetPos(x, y, id)
        self.plants.update({(x, y): id_class[id](id, pos)})

    # 根据位置获得坐标
    def getCoordinateByPos(self, pos):
        x = (pos[0] - LEFT_TOP[0]) // GRID_SIZE[0]
        y = (pos[1] - LEFT_TOP[1]) // GRID_SIZE[1]
        return x, y

    # 有坐标获得位置
    def FromCoordinateToGetPos(self, x, y, id):
        return LEFT_TOP[0] + x * GRID_SIZE[0] + ObjectParameter[id]["BIAS"][0], LEFT_TOP[1] + y * GRID_SIZE[1] + \
               ObjectParameter[id]["BIAS"][1]

    # 判断是否鼠标点击到了卡片
    def clickOnTheCard(self, mousePos, id):
        cardbias = ObjectParameter[id]["CARD_BIAS"]
        if (CARD_POS[0] + (CARD_SIZE[0] + CARD_GAP) * cardbias < mousePos[0] < CARD_POS[0] + (
                CARD_SIZE[0] + CARD_GAP) * (cardbias + 1) and CARD_POS[1] < mousePos[1] < CARD_POS[1] + CARD_SIZE[1]):
            return True
        return False

"""
本文件存放了所有角色类，每个角色类继承自ObjectBase,再根据角色属性行为去丰富其类
"""
import time

from ObjectBase import ObjectBase
from ConstGameParameter import *
from Items import *


# 豌豆射手（可作为其他射手类的父类）
class PeaShooter(ObjectBase):
    def __init__(self, id, pos):
        super(PeaShooter, self).__init__(id, pos)
        self.canShoot = False  # 能否射击
        self.hasBullet = False  # 是否有子弹

    def preSummon(self):
        self.canShoot = True
        self.pathIndex = 0

    def hasSummon(self):
        return self.hasBullet

    def doSummon(self):
        if self.hasSummon():
            self.hasBullet = False
            return PeaBullet("PEABULLET", (self.pos[0] + 60, self.pos[1] + 10))

    def checkImageIndex(self):
        if time.time() - self.preIndexTime <= getParameter(self.id, "IMAGE_INDEX_CD"):
            return
        self.preIndexTime = time.time()

        index = self.pathIndex + 1
        if index == 8 and self.canShoot:
            self.hasBullet = True
        if index >= self.pathIndexCount:
            index = 9
        self.update(index=index)


# 双线射手
class RepeaterPea(PeaShooter):
    def doSummon(self):
        if self.hasSummon():
            self.hasBullet = False
            return PeaBullet("PEABULLET", (self.pos[0] + 70, self.pos[1] + 10)), PeaBullet("PEABULLET", (
                self.pos[0] + 45, self.pos[1] + 10))


# 向日葵
class SunFlower(ObjectBase):
    def __init__(self, id, pos):
        super(SunFlower, self).__init__(id, pos)
        self.hasSunLight = False

    def preSummon(self):
        self.hasSunLight = True

    def hasSummon(self):
        return self.hasSunLight

    def doSummon(self):
        if self.hasSummon():
            self.hasSunLight = False
            return Sun("SUN", (self.pos[0] + 20, self.pos[1] - 10))


# 三线射手
class ThreePeaShooter(PeaShooter):
    def doSummon(self):
        if self.hasSummon():
            self.hasBullet = False
            return PeaBullet("PEABULLET", (self.pos[0] + 60, self.pos[1] + 10 +
                                           GRID_SIZE[1])), PeaBullet("PEABULLET", (
                self.pos[0] + 60, self.pos[1] + 10)), PeaBullet("PEABULLET", (
                self.pos[0] + 60, self.pos[1] + 10 - GRID_SIZE[1]))


# 僵尸
class ZombieBase(ObjectBase):
    def getHP(self):
        return self.hp


# 吃植物中的僵尸
class ZombieEating(ObjectBase):
    def __init__(self, id, pos):
        super(ZombieEating, self).__init__(id, pos)
        self.timeOfEat = 0

    def getHP(self):
        return self.hp

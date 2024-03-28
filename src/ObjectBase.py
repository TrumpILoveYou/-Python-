"""
这个文件构建了所有游戏成员的父类——ObjectBase
"""
import time

from ImageProcessor import Image
from ConstGameParameter import getParameter


class ObjectBase(Image):
    def __init__(self, id, pos):
        self.id = id
        self.hp = getParameter(self.id,"HP")
        self.attack = getParameter(self.id,"ATT")
        super(ObjectBase, self).__init__(getParameter(self.id,"PATH"), 0, pos, getParameter(self.id,"SIZE"),
                                         getParameter(self.id,"IMAGE_INDEX_MAX"))
        self.preIndexTime = 0
        self.prePositionTime = 0
        self.preSummonTime = 0

    #判断是否两个对象碰到了一起
    def isCollide(self, other):
        return self.getRect().colliderect(other.getRect())

    #更新对象
    def update(self, pos=None, index=None):
        self.checkSummon()
        self.checkPos()
        self.checkImageIndex()
        if pos:
            self.updateImage(pos=pos)
        if not index==None:
            self.updateImage(index=index)

    #检测召唤物
    def checkSummon(self):
        if time.time() - self.preSummonTime <= getParameter(self.id, "SUMMON_CD"):
            return False
        self.preSummonTime = time.time()
        self.preSummon()
        return True

    #检测位置
    def checkPos(self):
        if time.time() - self.prePositionTime <= getParameter(self.id, "POSITION_CHANGE_CD"):
            return False
        self.prePositionTime = time.time()
        self.pos = (self.pos[0] + getParameter(self.id, "SPEED")[0], self.pos[1] + getParameter(self.id, "SPEED")[1])
        return True

    #检测图片序号
    def checkImageIndex(self):
        if time.time() - self.preIndexTime <= getParameter(self.id, "IMAGE_INDEX_CD"):
            return
        self.preIndexTime = time.time()
        index = self.pathIndex + 1
        if index >= self.pathIndexCount:
            index = 0
        self.update(index=index)

    #三个未实现的方法交由子类实现
    def preSummon(self):
        pass

    def hasSummon(self):
        pass

    def doSummon(self):
        pass

"""
自定义的、针对本游戏设计需要的图片处理器：

图片属性：路径（可能含%d版,序数，图片数），大小，位置
图片操作：更新图片（直接更新、位置改变更新、序数改变更新）、取得图片矩形、图片展示到画布
"""
import pygame

class Image(pygame.sprite.Sprite, object):
    def __init__(self, pathFmt, pathIndex=0, pos=(0, 0), size=None, pathIndexCount=0):
        super(Image, self).__init__()
        self.pathFmt = pathFmt  # 图片路径（含%d版）
        self.pathIndex = pathIndex  # 图片序数
        self.size = size  # 图片大小
        self.pos = list(pos)  # 图片位置
        self.pathIndexCount = pathIndexCount  # 动画的图片数
        self.updateImage()  # 更新图片
        if self.size:    #图片初始化需要重塑形状
            self.image = pygame.transform.scale(self.image, self.size)

    # 更新图片(由于位置改变或者图片序数改变）
    def updateImage(self, pos=None, index=None):
        if pos:
            self.pos = pos
        if not index==None:
            self.pathIndex = index
        path = self.pathFmt
        if self.pathIndexCount != 0:
            path = path % self.pathIndex
        self.image = pygame.image.load(path)


    # 取得图片矩形
    def getRect(self):
        rect = self.image.get_rect()
        rect.x, rect.y = self.pos
        return rect

    # 图片展示到画布
    def draw(self, ds):
        ds.blit(self.image, self.getRect())

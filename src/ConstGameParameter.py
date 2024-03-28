"""
本文档定义了游戏相关的所有常量参数，可以根据需要进行修改
"""


# 本数据库的取得方法
def getParameter(ID, choice=None):
    data = ObjectParameter[ID]
    if choice:
        data = data[choice]
    return data


# ObjectParameter字典记录了每个游戏对象的一些基本属性,每个条目格式见第一个条目:
ObjectParameter = {

    # 铲子
    "SHOVEL": {
        "CARD_PATH": r"picture\other\shovel.png",  # 卡牌图片路径
        "PATH": r"picture\other\shovel.png",  # 游戏对象图片路径
        "IMAGE_INDEX_MAX": 0,  # 动画图片数目
        "IMAGE_INDEX_CD": 0.0,  # 动画图片帧率
        "POSITION_CHANGE_CD": 0.000,  # 位置变化CD
        "SIZE": (71, 67),  # 图片大小
        "SPEED": (0, 0),  # 对象运动速度
        "SUMMON_CD": -1,  # 召唤产物CD
        "CAN_LOOT": False,  # 拾取判断
        "VALUE": 0,  # 价格
        "BIAS": (0, 0),  # 位置偏置值
        "CARD_BIAS": 11,  # 卡牌位置偏置序数值
        "HP": 10000,  # 血量
        "ATT": 0,  # 攻击力
    },

    # 豌豆子弹
    "PEABULLET": {
        "CARD_PATH": None,
        "PATH": r"picture\other\PeaNormal\PeaNormal_0.png",
        "IMAGE_INDEX_MAX": 0,
        "IMAGE_INDEX_CD": 0.0,
        "POSITION_CHANGE_CD": 0.008,
        "SIZE": (56, 34),
        "SPEED": (3, 0),
        "SUMMON_CD": -1,
        "CAN_LOOT": False,
        "VALUE": 0,
        "BIAS": (15, 20),
        "CARD_BIAS": -10,
        "HP": 1,
        "ATT": 1,
    },

    # 僵尸
    "ZOMBIE": {
        "CARD_PATH": None,
        "PATH": r"picture\NormalZombie\Zombie\Zombie_%d.png",
        "IMAGE_INDEX_MAX": 22,
        "IMAGE_INDEX_CD": 0.1,
        "POSITION_CHANGE_CD": 0.02,
        "SIZE": (110, 125),
        "SPEED": (-0.5, 0),
        "SUMMON_CD": -1,
        "CAN_LOOT": False,
        "VALUE": 0,
        "BIAS": (0, -55),
        "CARD_BIAS": -10,
        "HP": 6,
        "ATT": 1,
    },

    # 吃植物中的僵尸
    "ZOMBIEEATING": {
        "CARD_PATH": None,
        "PATH": r"picture\NormalZombie\ZombieAttack\ZombieAttack_%d.png",
        "IMAGE_INDEX_MAX": 21,
        "IMAGE_INDEX_CD": 0.12,
        "POSITION_CHANGE_CD": 0.01,
        "SIZE": (110, 125),
        "SPEED": (0, 0),
        "SUMMON_CD": -1,
        "CAN_LOOT": False,
        "VALUE": 0,
        "BIAS": (0, -55),
        "CARD_BIAS": -10,
        "HP": 6,
        "ATT": 1,
    },

    # 阳光
    "SUN": {
        "CARD_PATH": None,
        "PATH": r"picture\other\Sun\Sun_%d.png",
        "IMAGE_INDEX_MAX": 22,
        "IMAGE_INDEX_CD": 0.02,
        "POSITION_CHANGE_CD": 0.015,
        "SIZE": (100, 100),
        "SPEED": (0, 0.2),
        "SUMMON_CD": -1,
        "CAN_LOOT": True,
        "VALUE": 15,
        "BIAS": (0, 0),
        "CARD_BIAS": -10,
        "HP": 100000,
        "ATT": 0,
    },

    # 向日葵
    "SUNFLOWER": {
        "CARD_PATH": r"picture\cards\card_sunflower.png",
        "PATH": r"picture\plant\SunFlower\SunFlower_%d.png",
        "IMAGE_INDEX_MAX": 18,
        "IMAGE_INDEX_CD": 0.10,
        "POSITION_CHANGE_CD": 1,
        "SIZE": (80, 80),
        "SPEED": (0, 0),
        "SUMMON_CD": 5,
        "CAN_LOOT": False,
        "VALUE": 30,
        "BIAS": (0, 0),
        "CARD_BIAS": 2,
        "HP": 10,
        "ATT": 0,
    },

    # 豌豆射手
    "PEASHOOTER": {
        "CARD_PATH": r"picture\cards\card_peashooter.png",
        "PATH": r"picture\plant\peashooter\Peashooter_%d.png",
        "IMAGE_INDEX_MAX": 13,
        "IMAGE_INDEX_CD": 0.15,
        "POSITION_CHANGE_CD": 1000,
        "SIZE": (80, 80),
        "SPEED": (0, 0),
        "SUMMON_CD": 5,
        "CAN_LOOT": False,
        "VALUE": 50,
        "BIAS": (0, 0),
        "CARD_BIAS": 1,
        "HP": 8,
        "ATT": 0,
    },

    # 双线射手
    "REPEATERPEA": {
        "CARD_PATH": r"picture\cards\card_repeaterpea.png",
        "PATH": r"picture\plant\RepeaterPea\RepeaterPea_%d.png",
        "IMAGE_INDEX_MAX": 15,
        "IMAGE_INDEX_CD": 0.15,
        "POSITION_CHANGE_CD": 1000,
        "SIZE": (80, 80),
        "SPEED": (0, 0),
        "SUMMON_CD": 2,
        "CAN_LOOT": False,
        "VALUE": 100,
        "BIAS": (0, 0),
        "CARD_BIAS": 4,
        "HP": 8,
        "ATT": 0,
    },

    # 三线射手
    "THREEPEASHOOTER": {
        "CARD_PATH": r"picture\cards\card_threepeashooter.png",
        "PATH": r"picture\plant\Threepeater\Threepeater_%d.png",
        "IMAGE_INDEX_MAX": 15,
        "IMAGE_INDEX_CD": 0.15,
        "POSITION_CHANGE_CD": 1000,
        "SIZE": (80, 80),
        "SPEED": (0, 0),
        "SUMMON_CD": 4,
        "CAN_LOOT": False,
        "VALUE": 100,
        "BIAS": (0, 0),
        "CARD_BIAS": 0,
        "HP": 8,
        "ATT": 0,
    },
}

# gold_textcolor:在不同金币区间，金币数字颜色RGB不同
gold_textcolor = {
    (100, 999): (20, 50, 100),
    (10, 99): (230, 28, 100),
    (0, 9): (230, 28, 50),
}

# 游戏界面大小
GAME_SIZE = (1280, 600)

# 僵尸总数
ZOMBIE_NUM = 20

# 初始金币
ORIGIN_GOLD = 200

# 游戏指导文字颜色
INSTRUCT_COLOR = (65, 138, 180)

# 植物卡牌大小
CARD_SIZE = (47, 66)

# 卡牌位置
CARD_POS = (328, 6)

# 僵尸出生位置
ZOMBIE_BORN_POS = 14

# 卡片位置间隔
CARD_GAP = 5

# 游戏地图路径
GAME_BACKGROUND_PATH = r"picture\other\back.png"

# 植物卡片放置板路径
CHOOSER_BACKGROUND_PATH = r"picture\other\ChooserBackground.png"

# 铲子放置板路径
SHOVELBOX_PATH = r"picture\other\shovelBox.png"

# 植物卡片放置板大小
CHOOSER_SIZE = (600, 80)

# 铲子放置板大小
SHOVELBOX_SIZE = (71, 67)

# 金币展示位置
GOLD_DISPLAY_POS = (280, 59)

# 田块数目
GRID_COUNT = (9, 5)

# 田块大小
GRID_SIZE = (74, 100)

# 田的最左上角坐标
LEFT_TOP = (230, 60)

# 僵尸出生CD
ZOMBIE_BORN_CD = 6

# 子弹偏置
BULLET_BOMB_BIAS = 40

# 子弹碎片残余时间
REMAIN_TIME = 1

# 爆炸子弹图片
BULLET_BOMB_PATH = r"picture\other\PeaNormalExplode\PeaNormalExplode_0.png"

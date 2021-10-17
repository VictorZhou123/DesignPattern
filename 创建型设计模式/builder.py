from abc import ABCMeta, abstractclassmethod


# 产品
class Player:
    def __init__(self=None, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg
    
    def __str__(self):
        return "%s, %s, %s, %s" %(self.face, self.body, self.arm, self.leg)


# 抽象建造者
class PlayerBuilder(metaclass=ABCMeta):
    @abstractclassmethod
    def build_face(self):
        pass

    @abstractclassmethod
    def build_body(self):
        pass

    @abstractclassmethod
    def build_arm(self):
        pass

    @abstractclassmethod
    def build_leg(self):
        pass


# 具体建造者
class SexyGirl(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "漂亮脸蛋"

    def build_body(self):
        self.player.body = "苗条"

    def build_arm(self):
        self.player.arm = "纤细"

    def build_leg(self):
        self.player.leg = "大长腿"


class Monster(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "怪兽脸"

    def build_body(self):
        self.player.body = "怪兽身材"

    def build_arm(self):
        self.player.arm = "长毛的手"

    def build_leg(self):
        self.player.leg = "长毛的腿"


# 指挥者
class PlayerDirector:
    '''
    控制组装顺序
    '''
    def build_player(self, builder):
        builder.build_face()
        builder.build_body()
        builder.build_arm()
        builder.build_leg()
        return builder.player


# client
builder = SexyGirl()
director = PlayerDirector()
p = director.build_player(builder)
print(p)
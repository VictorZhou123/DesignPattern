from abc import ABCMeta, abstractclassmethod

# 抽象组件 Componet

class Graphic(metaclass=ABCMeta):
    @abstractclassmethod
    def draw(self):
        pass


class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "点(%s, %s)" %(self.x, self.y)

    def draw(self):
        print("-----叶子组件Leaf-----")
        print(str(self))
        print("-----叶子组件Leaf-----")

    
class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self) -> str:
        return "%s到%s" %(self.p1, self.p2)

    def draw(self):
        print("-----叶子组件Leaf-----")
        print(str(self))
        print("-----叶子组件Leaf-----")


class Picture(Graphic):
    def __init__(self, interable):
        self.children = []
        if interable:
            for _ in interable:
                self.children.append(_)
    
    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print("-----复合组件Composite-----")
        for _ in self.children:
            print(_)
        print("-----复合组件Composite-----")


# client

p1 = Point(1, 2)
p2 = Point(2, 3)
l1 = Line(Point(1,1), Point(2,2))
l2 = Line(Point(1,5), Point(2,6))
pic1 = Picture([p1, p2, l1])
pic2 = Picture([p1, l1, l2])
pic1.draw()
pic2.draw()


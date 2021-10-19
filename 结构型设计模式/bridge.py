from abc import ABCMeta, abstractclassmethod


# 实现者
class Color(metaclass=ABCMeta):
    @abstractclassmethod
    def paint(self):
        pass


# 抽象
class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractclassmethod
    def draw(self):
        pass


# 具体实现者
class Red(Color):
    def paint(self, shape):
        print("红色的%s" % shape.name)


class Black(Color):
    def paint(self, shape):
        print("黑色的%s" % shape.name)


# 细化抽象
class Rectangle(Shape):
    name = "长方形"

    def draw(self):
        self.color.paint(self)


class Circle(Shape):
    name = "圆形"

    def draw(self):
        self.color.paint(self)


# client
p = Circle(Red())
p.draw()

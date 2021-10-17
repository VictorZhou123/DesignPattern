from abc import ABCMeta, abstractclassmethod

# 错误的接口，将所有的接口放在一个类里面，造成了一个单一的总接口
'''
class Animal(ABCMeta):
    @abstractclassmethod
    def swim(self):
        pass

    @abstractclassmethod
    def walk(self):
        pass

    @abstractclassmethod
    def fly(self):
        pass
'''

# 正确的接口，使用多个专门的接口，而不使用单一的总接口
class WaterAnimal(ABCMeta):
    @abstractclassmethod
    def swim(self):
        pass

class LandAnimal(ABCMeta):
    @abstractclassmethod
    def walk(self):
        pass

class SkyAnimal(ABCMeta):
    @abstractclassmethod
    def fly(self):
        pass

# 高层模块
class Tiger(LandAnimal):
    def walk(self):
        print("老虎走路")

class Frog(LandAnimal, WaterAnimal):
    def walk(self):
        print("青蛙走路")

    def swim(self):
        print("青蛙游泳")

'''
接口隔离原则：使用多个专门的接口，而不使用单一的总接口，即客户端（高层模块）不应该依赖那些它不需要的接口
在这里如果我们使用第一个接口（总接口），那么高层模块在调用接口时无论是Tiger还是Frog模块，都需要实现
swim，walk，fly的三个方法，这样是不合理的。我们可以使用多个专用接口，再调用时我们再调用多个专用接口即可。
'''
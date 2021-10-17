# 单例类
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# 继承单例类
class MyClass(Singleton):
    def __init__(self, a):
        self.a = a 
    
a = MyClass(10)
b = MyClass(20)

print(a.a)
print(b.a)
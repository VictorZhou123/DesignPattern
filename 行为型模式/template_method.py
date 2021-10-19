from abc import ABCMeta, abstractclassmethod
from time import sleep


# 抽象类
class Window(metaclass=ABCMeta):
    @abstractclassmethod
    def start(self): # 原子方法
        pass

    @abstractclassmethod
    def repaint(self):
        pass

    @abstractclassmethod
    def stop(self):
        pass

    def run(self):   # 模板方法（钩子操作）
        self.start()
        while True:
            try:
                self.repaint()
                sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()



# 具体类
class MyWindow(Window):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print("窗口开始运行")

    def repaint(self):
        print(self.msg)

    def stop(self):
        print("窗口结束运行")


# client
window = MyWindow("视频加载中.....")
window.run()

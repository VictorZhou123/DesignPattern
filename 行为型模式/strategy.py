from abc import ABCMeta, abstractclassmethod


# 抽象策略
class Strategy(metaclass=ABCMeta):
    @abstractclassmethod
    def execute(self, data):
        pass


# 具体策略
class FastStrategy(Strategy):
    def execute(self, data):
        print("用较快的算法来处理:%s" %data)


class SlowStrategy(Strategy):
    def execute(self, data):
        print("用较慢的算法来处理:%s" %data) 


# 上下文
class Context:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)


# client

data = "我想从上海去深圳"
s_slow = SlowStrategy()
s_fast = FastStrategy()
context = Context(s_slow, data)
context.do_strategy()
print("-----更换算法-----")
context.set_strategy(s_fast)
context.do_strategy()
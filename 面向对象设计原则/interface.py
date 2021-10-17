from abc import ABCMeta, abstractclassmethod

# 接口
class Payment(metaclass=ABCMeta):
    '''
    创造一个抽象类
    '''
    # abstract class
    @abstractclassmethod
    def pay(self, money):
        pass


# 低层模块
class Alipay(Payment):
    '''
    实现接口Payment
    '''
    def pay(self, money):
        print("支付宝支付%d元." %money)


class WechatPay(Payment):
    '''
    实现接口Payment
    '''
    def pay(self, money):
        print("微信支付%d元." %money)


# 高层模块
p = Alipay()
p.pay(100)
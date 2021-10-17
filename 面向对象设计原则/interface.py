from abc import ABCMeta, abstractclassmethod

# 接口的实现方法

# 创造一个抽象类
class Payment(metaclass=ABCMeta):
    # abstract class
    def pay(self, money):
        pass

# 实现接口Payment
class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%d元." %money)

# 实现接口Payment
class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元." %money)

p = Alipay()
p.pay(100)
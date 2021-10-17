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
class PaymentFactory:
    '''
    创建简单工厂，生成Alipay和WechatPay的类
    '''
    def create_payment(self, method):
        if method == 'alipay':
            return Alipay()
        elif method == 'wechat':
            return WechatPay()
        else:
            raise TypeError("No such payment named %s" %method)


# client
pf = PaymentFactory()
p = pf.create_payment("alipay") # 根据alipay生成了Alipay的类
p.pay(100)
from abc import ABCMeta, abstractclassmethod

# 产品角色接口
class Payment(metaclass=ABCMeta):
    '''
    创造一个抽象类（抽象产品）
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
        print("支付宝余额支付%d元." %money)


class WechatPay(Payment):
    '''
    实现接口Payment
    '''
    def pay(self, money):
        print("微信支付%d元." %money)

class HuabeiPay(Payment):
    def pay(self, money):
        print("花呗支付%d元." %money)


# 高层模块

# 工厂角色接口
class PaymentFactory(metaclass=ABCMeta):
    '''
    抽象工厂角色
    '''
    @abstractclassmethod
    def create_payment(self):
        pass


# 具体工厂角色
class AlipayFactory(PaymentFactory):
    '''
    创建AlipayFactory，生产Alipay的类
    '''
    def create_payment(self):
        return Alipay()


class WechatPayFactory(PaymentFactory):
    '''
    创建WechatPayFactory，生产WechatPay的类
    '''
    def create_payment(self):
        return WechatPay()


class HuabeiPayFactory(PaymentFactory):
    '''
    创建HuabeiPayFactory，生产HuabeiPay的类
    '''
    def create_payment(self):
        return HuabeiPay()


# client
pf = HuabeiPayFactory()
p = pf.create_payment() # 根据alipay生成了Alipay的类
p.pay(100)
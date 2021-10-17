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


class BankPay:
    '''
    假设这里有一段其他系统复用过来的代码，与现有接口不匹配
    '''
    def cost(self, cash):
        print("银行卡支付%d元." %cash)


class ApplePay:
    '''
    假设这里有一段其他系统复用过来的代码，与现有接口不匹配
    '''
    def cost(self, cash):
        print("苹果手机支付%d元." %cash)


# 类适配器（通过继承）
# class NewBankPay(BankPay):
#     def pay(self, money):
#         self.cost(money)

# 对象适配器（通过组合）
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)



# 高层模块
# p = NewBankPay()

p = PaymentAdapter(ApplePay())
p.pay(100)
# 父类，用户名显示
class User:
    # 普通显示用户名
    def show_username(self):
        pass

# 子类，VIP用户名显示
class VIPUser(User):
    # 特殊显示VIP用户名
    def show_username(self):
        pass

# 实现
def show_user(u):
    u.show_username()

'''
里氏替换原则要求，子类改写的方法的实现内容要与父类保持一致
这样在调用时就能保证子类和父类的实现的一致性了
'''

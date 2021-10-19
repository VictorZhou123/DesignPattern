from abc import ABCMeta, abstractclassmethod



# 抽象订阅者
class Observer(metaclass=ABCMeta):
    @abstractclassmethod
    def update(self, notice): # notice是一个Notice类对象
        pass


# 抽象发布者
class Notice:
    def __init__(self) -> None:
        self.observer = []  # 订阅者列表

    def attach(self, obs):
        self.observer.append(obs)

    def detach(self, obs):
        self.observer.remove(obs)

    def notify(self): # 推送
        for obs in self.observer:
            obs.update(self)


# 具体订阅者
class Staff(Observer):
    def __init__(self) -> None:
        self.company_info = None

    # 更新company_info内容
    def update(self, notice):
        self.company_info = notice.company_info


# 具体发布者
class StaffNotice(Notice):
    def __init__(self):
        super().__init__()
        self.__company_info = None

    # 读company_info内容
    @property
    def company_info(self):
        return self.__company_info

    # 写company_info内容
    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()


# client

staff1 = Staff()
staff2 = Staff()
notice = StaffNotice()
notice.attach(staff1)
notice.attach(staff2)
notice.company_info = "今年发三倍年终奖"
print(notice.company_info)
print(staff1.company_info)
print(staff2.company_info)
notice.detach(staff1)
notice.company_info = "明天放假"
print("-----staff1取消订阅后-----")
print(notice.company_info)
print(staff1.company_info)
print(staff2.company_info)
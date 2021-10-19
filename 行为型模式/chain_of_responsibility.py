from abc import ABCMeta, abstractclassmethod



# 抽象处理者
class Handler(metaclass=ABCMeta):
    @abstractclassmethod
    def handle_leave(self, day):
        pass


# 具体处理者
class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 10:
            print("总经理批假%d天" %day)
        else:
            print("你还是辞职吧")


class DepartmentManager(Handler):
    def __init__(self) -> None:
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 5:
            print("部门经理批假%d天" %day)
        else:
            print("部门经理权限不足")
            self.next.handle_leave(day)


class ProjectDirector(Handler):
    def __init__(self) -> None:
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 3:
            print("项目主管批假%d天" %day)
        else:
            print("项目主管权限不足")
            self.next.handle_leave(day)


# client
day = 7
h = ProjectDirector()
h.handle_leave(day)
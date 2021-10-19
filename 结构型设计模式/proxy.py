from abc import ABCMeta, abstractclassmethod



# 抽象实体
class Subject(metaclass=ABCMeta):
    @abstractclassmethod
    def get_content(self):
        pass

    @abstractclassmethod
    def set_content(self):
        pass


# 实体
class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, 'r', encoding='utf-8')
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w', encoding='utf-8')
        f.write(content)
        f.close()

# 代理

# 1.虚代理
class Proxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content(content)


# 2.保护代理
class ProtectProxy(Subject):
    '''
    只读权限
    '''
    def __init__(self, filename) -> None:
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError("没有写入权限.")
        



# client

# subj = Proxy("结构型设计模式/test.txt")
# print(subj.get_content())

subj = ProtectProxy("结构型设计模式/test.txt")
print(subj.set_content("input..."))


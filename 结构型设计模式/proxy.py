from _typeshed import OpenTextMode
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
    def __init__(self, filename) -> None:
        self.filename = filename
        f = open(self.filename, 'r', 'utf-8')
        self.content = f.read()
        f.close

    def read_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'r', 'utf-8')
        f.write(content)
        f.close()
        return f

# 代理
class Proxy(Subject):
    def __init__(self, filename) -> None:
        self.filename = filename
        self.subj = None

    def read_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        self.subj.read_content()

    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        self.subj.set_content(content)


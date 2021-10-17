from abc import ABCMeta, abstractclassmethod


# ----------抽象产品----------

class PhoneShell(metaclass=ABCMeta):
    @abstractclassmethod
    def show_shell(self):
        pass


class CPU(metaclass=ABCMeta):
    @abstractclassmethod
    def show_cpu(self):
        pass


class OS(metaclass=ABCMeta):
    @abstractclassmethod
    def show_os(self):
        pass


# ----------抽象工厂----------

class PhoneFactory(metaclass=ABCMeta):
    @abstractclassmethod
    def make_shell(self):
        pass

    @abstractclassmethod
    def make_cpu(self):
        pass

    @abstractclassmethod
    def make_os(self):
        pass

# ----------具体产品----------

class SmallShell(PhoneShell):
    def show_shell(self):
        print("普通手机小手机壳")


class BigShell(PhoneShell):
    def show_shell(self):
        print("普通手机大手机壳")


class AppleShell(PhoneShell):
    def show_shell(self):
        print("苹果手机壳")


class SnapDragonCPU(CPU):
    def show_cpu(self):
        print("骁龙CPU")


class KirinCPU(CPU):
    def show_cpu(self):
        print("麒麟CPU")


class AppleCPU(CPU):
    def show_cpu(self):
        print("苹果CPU")


class Android(OS):
    def show_os(self):
        print("安卓操作系统")


class IOS(OS):
    def show_os(self):
        print("IOS操作系统")


# ----------具体工厂----------

class MiFactory(PhoneFactory):
    def make_shell(self):
        return BigShell()

    def make_cpu(self):
        return SnapDragonCPU()

    def make_os(self):
        return Android()


class HuaWeiFactory(PhoneFactory):
    def make_shell(self):
        return BigShell()

    def make_cpu(self):
        return KirinCPU()

    def make_os(self):
        return Android()


class AppleFactory(PhoneFactory):
    def make_shell(self):
        return AppleShell()

    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return IOS()


# ----------客户端----------

class Phone:
    def __init__(self, shell, cpu, os):
        self.shell = shell
        self.cpu = cpu
        self.os = os

    def show_info(self):
        print("手机信息:")
        self.shell.show_shell()
        self.cpu.show_cpu()
        self.os.show_os()

def make_phone(factory):
    shell = factory.make_shell()
    cpu = factory.make_cpu()
    os = factory.make_os()
    return Phone(shell, cpu, os)

p1 = make_phone(AppleFactory())
p1.show_info()
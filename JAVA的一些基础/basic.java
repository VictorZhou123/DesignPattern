/*
extends 继承
abstract 抽象

interface 接口
implements 实现

1.抽象类不一定有抽象方法
  有抽象方法的一定是抽象类

2.抽象类不能实例化
  抽象方法没有方法体

3.继承了抽象类 一定要重写抽象类里面的抽象方法

4.接口里的方法其实都是抽象方法，也就是没有方法体的。但是它不用写关键字abstract

*/


// 接口与实现
interface C {

}

class D implements C {

}


abstract class A {
    public abstract void func1();
    public void func2() {};
} 

class B extends A {
    public func1() {};
}
class Base:
    def __init__(self, A):
        self.m_A = A

    def func(self):
        print("Base的func调用")


# 继承语法（派生类无法继承基类的私有属性）
class Son(Base):
    def __init__(self, A, B):
        super().__init__(A)  # 借用Base的构造函数为m_A赋值
        self.m_B = B

    # func重写
    def func(self):
        print("Son的func调用")


class GrandSon(Son):
    def __init__(self, A, B, C):
        super().__init__(A, B)
        self.m_C = C

    def func(self):
        print("GrandSon的func调用")


# 注意：当一个类继承了多个父类时，默认优先使用第一个父类中的同名属性或方法，可以使用 类名.mro 属性 或 类名.mro() 方法查看调用顺序。
class example(GrandSon, Son):
    def func(self):
        GrandSon.func(self)


GrandSon(1, 2, 3).func()
print(example.mro())

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


class Example:
    def func(self) -> None:
        print("Example的func调用")


# 多态的实现（甚至不需要有继承关系的类都可以实现，比如Example类）
def polymorphism(people):
    people.func()


polymorphism(Base(1))
polymorphism(Son(1, 2))
polymorphism(GrandSon(1, 2, 3))
polymorphism(Example())

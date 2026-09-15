class Person:
    # 类属性（同一个类中所有对象共有的，对于一个对象单独修改其类属性并不会影响其共有属性）
    School = "Central Sount University"

    # __init__：类构造函数
    def __init__(self, name, age, id) -> None:
        # 实例属性（属于每个类对象自己的属性）
        self.m_name = name
        self.m_age = age
        self.m_id = id

    # 普通方法
    def ShowPerson(self) -> None:
        print(f"Name:{self.m_name}  Age:{self.m_age}    ID:{self.m_id}")

    # 魔法方法

    # __str__：输出该对象时可当作字符串输出，类似于c++中的<<运算符重载
    def __str__(self) -> str:
        return f"Name:{self.m_name}  Age:{self.m_age}    ID:{self.m_id}"

    # __eq__：类似于c++中的==逻辑运算符重载
    def __eq__(self, ohter) -> bool:
        return self.m_id == ohter.m_id

    # def __le__(self, other):小于等于

    # def __lt__(self, other):小于

    # def __gt__(self, other):大于

    # def __ge__(self, other):大于等于


p1 = Person("Jackson", 12, 1)

print(p1)  # 输出对象的内存地址
print(p1.__dict__)  # person对象中自带dict可用来显示类的信息

p1.ShowPerson()
print(p1)  # 运算符重载
print(p1 == Person("Alice", 11, 2))

# 通过实例查找属性时，会先查找实例属性，如果实例属性不存在，再查找类属性
p1.School = "11111"  # p1的School变成了自己的实例属性
print(p1.School)
print(Person.School)
print(Person("Alice", 11, 2).School)

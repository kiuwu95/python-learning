class Person:
    def __init__(self, name, age, id):
        # 在成员变量前面加上__表该变量为私有属性，这只是种约定，并不是强制的，在外部依旧可以更改
        self.__m_name = name
        self.__m_age = age
        self.__m_id = id

    def ShowPerson(self):
        print(f"Name: {self.__m_name} Age: {self.__m_age} ID:{self.__m_id}")


p1 = Person("Alice", 12, 1)
p1.ShowPerson()
p1.__m_age = 1
p1.ShowPerson()

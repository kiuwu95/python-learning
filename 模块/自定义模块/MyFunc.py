__all__ = [
    "add",
    "minu",
    "muti",
]  # 当使用__all__时，在main文件中使用from Myfunc import *时导入的就是["add", "minu", "muti"]的内容
Pi = 3.1415926535
Location = "Yizhou"


def add(a, b):
    return a + b


def muti(a, b):
    return a * b


def minu(a, b):
    return a - b


# if __name__ == "__main__":用于在模块中测试函数，在模块中运行该.py文件时__name__等于"__main__"
if __name__ == "__main__":
    print(add(1, 1))

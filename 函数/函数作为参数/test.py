def add(a, b):
    return a + b


def func(a, b, f):
    return f(a, b)  # 函数作为参数


print(func(1, 1, add))

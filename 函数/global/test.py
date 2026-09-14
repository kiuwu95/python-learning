num = 100  # 全局域


def func():
    # 函数局部域
    global num  # 给全局域中的参数在函数中赋予global使其在函数中可更改该参数的值
    num = 200


print(num)

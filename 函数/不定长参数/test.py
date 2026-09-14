# 不定长参数可传入多个参数，其不定长参数的类型为元组
def func1(*args):
    """
    传入一个数组
    第一个值返回的是最大值
    第二个值返回的是最小值
    第三个值返回的是平均值
    """
    return max(args), min(args), sum(args) / len(args)


# 在参数前面加上*表示不定长位置参数，加上**表示不定长关键字参数,其类型为dict
def func2(*args, **kwargs):
    """
    传入一个数组
    第一个值返回的是最大值
    第二个值返回的是最小值
    第三个值返回的是平均值

    如果要指明保留n位小数则设置一个round = n
    """
    avr = sum(args) / len(args)

    if kwargs["round"] is not None:
        avr = round(avr, kwargs["round"])

    return max(args), min(args), avr


print(1, 2, 3, 4, 5)
print(func2(123, 12, 32, 11, 55, round=3))

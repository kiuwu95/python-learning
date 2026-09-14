def CalculateCircle(r):
    # 使用三个双引号括起函数的说明文档以告诉使用者该函数传入的变量以及返回的结果
    """
    args:r为圆的半径；
    return:第一个返回的值为圆的面积，第二个返回的值为圆的周长。
    """
    return 3.1415926535 * r * r, 2 * 3.1415926535 * r  # 可返回多个值


val = CalculateCircle(2)  # val的类型是tuple
a, b = CalculateCircle(1)  # a和b的类型都是float
print(CalculateCircle(3))

# 可指明参数类型以及函数的返回类型
def add(a: int, b: int) -> int:
    return a + b


def CalculateCircle(r: int) -> tuple[float, float]:
    return 3.1415926535 * r * r, 2 * 3.1415926535 * r


def func() -> None:
    print("Hello,world!")

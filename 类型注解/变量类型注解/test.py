# python是动态类型语言，添加的类型注解只是提示，并不是强制转换
a: int = 1
b: float = 2
c: bool = True
d: str = "hello"
e: list[str] = ["hello", "world"]
f: tuple[int] = (
    1,
    2,
    3,
    4,
    5,
)
g: dict[str:int] = {"Alice": 1, "Bob": 2}
h: tuple[str:int:int] = ["hello", 1, 2]

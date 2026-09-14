# tuple即为元组，不可以修改，只读
tup = (1, 2, 3, "hello")
for i in tup:
    print(i)
print("3有", tup.count(3), "个")
print("hello的下标为 ", tup.index("hello"))
# 定义单元素元组，加逗号即可
tup2 = (1,)

# while
i = 0
while i < 10:
    i += 1
    print(i)
else:  # 如果while条件不满足则直接跳转到else部分，不论while内部的代码是否执行或从未被执行
    print("end")

# for
str1 = "hello,world"
for i in str1:  # i遍历in后面的待处理数据集
    print(i)

# range
# 默认从0到9
for i in range(10):
    print(i, end=" ")
print()  # print()作换行
# 从1到4
for i in range(1, 5):
    print(i, end=" ")
print()
# 从0到9并以2跳跃
for i in range(0, 10, 2):
    print(i, end=" ")
print()
# 嵌套循环
for i in range(8):
    for j in range(7):
        print("*", end="")
    print()

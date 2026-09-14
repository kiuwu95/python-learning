s1 = {1, 2, 3, 4, 5}  # set使用大括号
s2 = set()  # 初始化一个空set
# add()添加元素
s2.add(3)
# remove()删除元素
s1.remove(4)
# pop()随机删除一个元素并返回
print(s1.pop())
print(s1, s2)
print(s1.intersection(s2))  # 输出交集
print(s1.union(s2))  # 输出并集
print(s1.difference(s2))  # 输出差集

s1.clear()  # 清空

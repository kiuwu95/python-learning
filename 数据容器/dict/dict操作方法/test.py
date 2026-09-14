d1 = {"Alice": 1, "Bob": 2, "Cat": 3, "Dick": 4, "Eric": 5}
# 在d1中添加键值对
d1["Frank"] = 6

# 删除元素
# pop(key)将dict中的key以及它的value删除并返回它的value
d1.pop("Cat")
# 通过del也可以删除
del d1["Frank"]
print(d1)

print(d1.keys())  # 返回所有的key
print(d1.values())  # 返回所有的value
print(d1.items())  # 返回所有的键值对

l = [1, "hello", 3.14]
# append()：在尾部添加元素
l.append(4)
# insert(num,val)：在num下标前面添加val元素
l.insert(1, 2)
# pop(num)删除下标为num的元素，如果不填默认为末尾元素
l.pop()
# remove(val)在list中删除第一个值为val的元素
l.remove("hello")
# sort()排序
l.sort()

print(l)

# reverse()反转列表
l.reverse()

print(l)

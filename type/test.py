# type()用于查看数据的类型是什么，isinstance()用来查看数据的类型是否为某种指定的类型
a = 1
b = 3.14
c = "hello,world"
print(type(a), type(b), type(c))
print(isinstance(c, str))
print(isinstance(c, int))
print(isinstance(c, float))

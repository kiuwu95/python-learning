def print_information(name, age, id):
    print(f"name:{name}     age:{age}\tid:{id}")


# 位置参数
print_information("Alice", 12, 1)
# 关键字参数（可读性强）
print_information(name="Bob", age=22, id=2)
# 位置+关键字参数（位置参数必须在前面，关键字参数在后面）
print_information("Frank", age=33, id=3)

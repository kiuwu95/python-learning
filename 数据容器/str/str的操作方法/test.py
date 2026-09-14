str1 = "hello,world"
# count(s)：统计该字符串中的s子串数量
print(str1.count("l"))
# find(s)：返回s子串的位置
print(str1.find("w"))
# upper()返回该字符串的大写
str1_upper = str1.upper()
print(str1_upper)
# lower()返回该字符串的小写
str1_lower = str1_upper.lower()
print(str1_lower)
# replace(s1,s2)将字符串中的所有s1字串替换为s2并返回一个新的字符串
print(str1.replace(",", "."))
# startwith(s)：如果该字符串以s子串开头则返回true，反之返回false。endwith(s)同理
print(str1.startswith("hel"))
# split(s)以该字符串中的所有s字串为分割点将该字符串切分并返回一个list
print(str1.split("l"))
# strip(s)去除该字符两端的s子串并返回一个新的字符串
print(str1.strip("d"))

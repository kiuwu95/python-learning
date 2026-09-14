#match等价于switch，_等价于default
num = int(input())
match num:
    case 1:
        print("星期一")#一定要缩进
    case 2:
        print("星期二")
    case 3:
        print("星期三")
    case 4 if 100==100:#可加if
        print("error1")
    case 5|6:#代表5或6
        print("error2")    
    case _:
        print("error")
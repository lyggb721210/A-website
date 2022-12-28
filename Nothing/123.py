#coding:"utf-8"
print("欢迎使用-版本V2.145_yxr") 
while 1 == 1:    
    print("\n1.加法运算") 
    print("2.减法运算")
    print("3.乘法运算")
    print("4.除法运算")
    print("5.退出")
    a = input("请数入前面序号")
    if a == "1":
        b = int(input("请输入一个加数"))
        c = int(input("请输入另一个加数"))  
        print("结果为：")
        print(b + c)
    elif a == "2":
        b = int(input("请输入被减数"))
        c = int(input("请输入减数"))  
        print(b - c)
    elif a == "3":
         b = int(input("请输入一个乘数"))
         c = int(input("请输入另一个乘数"))
         print(b * c)
    elif a == "4":
        print("1.不带余数的除法运算")
        print("2.带余数的除法运算")
        d = input("请数入前面序号")
        if d == "1":
            b = int(input("请输入被除数"))
            c = int(input("请输入除数数"))
            print(b / c)
        elif d == "2":
            b = int(input("请输入被除数"))
            c = int(input("请输入除数"))
            e = b % c
            if e == 0:
                print(b / c)
            elif e >= 0:
                print("结果为:")
                print((b - e) / c)
                print("余数为:")
                print(e)
        else:
            print("错误,请输入正确的数字")
    elif a == "5":
        print("按Enter退出")
        exit()
    else:
        print("错误,请输入正确的数字")
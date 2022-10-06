#coding=utf-8
"""
这是作者的第2个python程序若有问题请见谅
有BUG可联系作者
邮箱：lyggb721210@163.com
作者：yxrlyg / 栗子味东方
当前版本：V1.23.pre432 测试版
"""
print("欢迎使用")
import map
nmber = 0
inmap = map.inmap[nmber]
#特殊字符（□，■）
print("1.新游戏\n2.帮助")
lastprint = "  "
print("请输入前面序号")
a = input("")
if a == "1":
    while 1 == 1:
        c = 0
        outmap = ""
        while c != len(inmap):
            outmap = outmap + inmap[c]
            c = c + 1
        print(outmap)
        print(lastprint)
        print("请输入w,a,s,d")
        b = input("")
        if b == "w":
            add = inmap.index("😊")
            acd = add - inmap.index("\n") - 1
        elif b == "a":
            add = inmap.index("😊")
            acd = add - 1
        elif b == "d":
            add = inmap.index("😊")
            acd = add + 1
        elif b == "s":
            add = inmap.index("😊")
            acd = add + inmap.index("\n") + 1
        else:
            lastprint = "请输入w,a,s,d(上,左,下,右)"
            continue
        if acd <= 0:
            lastprint = "啊，碰墙了"
        elif acd > 0:
            if inmap[acd] == "■":
                lastprint = "啊，碰墙了"
            elif inmap[acd] == "□":
                lastprint = "  "
                inmap[add] = "□"
                inmap[acd] = "😊"
            elif inmap[acd] == "🚪":
                print("成功通关")
                print("1.下一关")
                print("2.退出")
                print("请输入前面序号")
                a = input()
                if a == "1":
                    if nmber < len(inmap)-1:
                        nmber = nmber + 1
                        inmap = map.inmap[nmber]
                    elif nmber >= len(inmap)-1:
                        print("关卡已结束")
                        exit()
                elif a == "2":
                    exit()
elif a == "2":
    print("这是一个迷宫闯关游戏,目前有2关")
    print("在游戏中可以输入w,a,s,d来控制😊的移动")
    print("(输入后要按enter表示确定)")
    print("祝您游玩愉快")
else:
    print("请输入正确的数字")
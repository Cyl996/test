""" money = input("请输入金额：")
print("输入的金额为：",money)


num = money.count(".")
if num ==0 or num == 1:
    hstr = "0123456789."
    for i in money:
        if i not in hstr:
            print("输入的值不合法。请输入数字！")
            exit() # 退出程序
    money = float(money) #强制转换数据类型为float 
    if money >= 0.01 and money <= 200:
        print("红包发送成功！")
    else:
        print("金额超出范围！")  #缩进，四个空格
else:
    print("输入的金额不合法，只能输入数字！") """




""" x = range(9) # 数列生成器
print(list(x)) """

""" 
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"x",j,"=",i*j,end="  ")
    print()
 """






for i in range(1,10):
    for j in range(1,i+1):
        print(i,"x",j,"=",i*j,end = "  ") #end 不换行
    print()
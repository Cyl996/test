hlist = [111,222,333,"哈哈","hehe",111]
hlist.append("嘻嘻") #往数组里添加新增值
hlist2 = hlist.copy() # copy复制原来的数组，赋值给另外一个值
num = hlist.count(111) #统计
hlist.extend("hehe") #吧字符串拆分为单个值，添加到数组中
num1 = hlist.index(222) #计算下标
hlist.insert(0,"000") #控制数据深入数组的位置
value = hlist.pop(0) #移走某个值
hlist.remove(111) #删除某个值
print(num1)
print(hlist)
print(num)
hlist.clear()

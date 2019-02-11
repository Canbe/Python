# Python3 列表

#知识点1：python 使用[]来表示一个列表，元素之间使用“，”分割开

bikes = ["trek","cannondale","redline","specailize"]
print(bikes)

##知识点2：使用下标访问列表元素,下标从0开始

print(bikes[0])
print(bikes[1].title())
##知识点3：下标-1表示最后一个元素，以此推类，下标-2为倒数第二的元素
print(bikes[-1])
print(bikes[-2])

##知识点3：列表是动态的，可以动态的增加，删除，修改列表里面的元素

motocycles = ["honda","yamaha","suzuki"]
print(motocycles)
#添加列表元素
motocycles.append("newone")
#删除列表元素
del motocycles[0]
#修改列表元素
motocycles[0] = "modifyone"

print(motocycles)

##知识点4：常用的列表方法

#弹出元素，默认弹出列表尾的元素，并返回
motocycles.pop()

#根据元素的值移除元素,remove只能删除第一次出现的值，要删除多个重复的值，需要重复调用
motocycles.remove("modifyone")

##知识点5：永久性排序方法sort

test = ["abc","bca","bac","cab"]

print(test)
test.sort()
print(test)

#字典逆序排序
test.sort(reverse=True)
print(test)

#知识点6：使用sorted函数临时排序

print(sorted(test))
print(sorted(test,reverse=True))


#知识点7：反转列表
test.reverse()
print(test)


#知识点8：获取列表长度
print(len(test))

#知识点9：不可改变的列表称为元组，用圆括号进行标识

test9_group = (1,2,3,4)
print(test9_group)




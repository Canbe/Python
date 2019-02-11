## 使用for循环 操作列表


##知识点1：遍历列表

list = ["a","b","c"]

for i in list:
    print(i)

##知识点2：使用range()来生成一组数字

#range[1,5)
for i in range(1,5):
    print(i)

test1_list = range(1,5)
print(test1_list)

#range第三个参数可以指定range的步长,打印1-10的偶数
for i in range(2,11,2):
    print(i)

##知识点3：处理数字列表的常用函数

test3_list = [1,2,3,4,5,6,7]

#求最大值
print(max(test3_list))
#求最小值
print(min(test3_list))
#求总和
print(sum(test3_list))


##知识点4：列表解析,下面两种方法都是生成同一个列表

test4_list1 = []
for i in range(1,11):
    test4_list1.append(i**2)

test4_list2 = [i**2 for i in range(1,11) ]

print(test4_list1)
print(test4_list2)

##知识点5：列表切片

test5_list = range(1,11)

#取出列表中的2到6的数字
for i in test5_list[1:6]:
    print(i)

#如果没有指定第一个索引，将从第一个参数开始
for i in test5_list[:6]:
    print(i)
#如果没有指定第二个索引，将遍历到尾
for i in test5_list[1:]:
    print(i)


##知识点6：复制列表
print("知识点6---------")

test6_list = [i for i in range(1,11)]



#直接赋值不可以，这是一个引用！！！
test6_list_copy1 = test6_list
test6_list[5] = 100
print(test6_list_copy1)

#复制整个列表
test6_list_copy2 = test6_list[:]
test6_list[5] = 6
print(test6_list_copy2)


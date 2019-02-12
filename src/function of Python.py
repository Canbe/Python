##python3 函数

##知识点1：定义函数
def test1_func():
    print("hello, python3")

test1_func()

##知识点2：函数传参,位置实参
def test2_func(para1,para2):
    print(para1,para2)

test2_func("1","2")

##知识点3：函数传参，关键字实参
def test3_func(para1,para2):
    print(para1,para2)

test3_func(para2="1",para1="2")

##知识点4：默认参数
def test4_func(para1,para2="2"):
    print(para1,para2)

test4_func("1")

##知识点5：返回值
def test5_func():
    return []

test5_return = test5_func()
print(test5_return)

##知识点6：传递列表,函数中对列表的修改将是永久的
test6_list = ["a","b","c"]
def test6_func(para1_list):
    para1_list[0] = "z"

#直接传递，函数将可以修改列表
test6_func(test6_list)
#将列表的切片副本传入，函数则不能修改外部的列表内容
test6_func(test6_list[:])
print(test6_list)


##知识点7：任意数量实参的函数,将接受到的参数封装在元组当中
def test7_func(*group):
    print(group)

test7_func("a","b","c")
test7_func("a")
test7_func()

##知识点8：结合位置实参和任意数量的实参

def test8_func(para1="",para2="",*gourp):
    print(para1,para2,gourp)

test8_func("1","2")
test8_func("1","2","3","4")
test8_func()


##知识点9：任意数量的关键字实参
def test9_func(**dict):
    print(dict)

test9_func()
test9_func(a=1,b=2)



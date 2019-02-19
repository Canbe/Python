##python3 字典

##知识点1：定义字典
dict = {}

##知识点2：字典的常用操作

test2_dict = {"a":1,"b":2,"c":3}

#访问
print(test2_dict["a"])

#修改
test2_dict["b"] = 100

#删除
del test2_dict["c"]

#添加
test2_dict["d"] = 4

print(test2_dict)

##知识点3：遍历字典

test3_dict = {"a":1,"b":2,"d":3}
test3_dict["c"] = 4
for key,value in test3_dict.items():
    print(key+":"+str(value))
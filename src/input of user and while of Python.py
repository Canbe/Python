#用户输入和while循环

##知识点1：获取用户输入
#test1_input = input()
#test2_input = input("用户输入:")


##知识点2：输入的都是文本信息，可以使用int函数将获得的文本信息转换为数字

age = "23"
test2_age = int(age)
print(age)


##知识点3：while循环
i=1
while i<=5:
    print(i)
    i+=1

##知识点4：删除包含特点值的列表元素

cats = ["a","b","a","c"]

while "a" in cats:
    cats.remove("a")

print(cats)
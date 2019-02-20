#python3 文件操作

file_name = "..//..//res//test"

#打开文件,读取整个文件
with open("..//..//res//test") as test:
    content = test.read()
    print(content)


#打开文件，逐行读取
with open("..//..//res//test") as test:
    for a in test:
        print(a)

with open(file_name,"w") as test:
    test.write("message")

with open(file_name+"a","a") as test:
    test.write("message")



##python3 if语句



##知识点1：使用if
test1_list = [i for i in range(1,11)]

#输出列表中的偶数
for i in test1_list:
    if i%2==0:
        print(i)
    else:
        print("跳过")


##知识点2：True 和 False
print(1==1)
print(1==2)

#知识点3：检查值是否在列表中
test3_list = [i for i in range(1,11)]

print(100 in test3_list)
print(5 in test3_list)
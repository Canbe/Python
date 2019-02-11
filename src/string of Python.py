#python3 字符串操作

##知识点1：字符串用引号括起来，引号都可以，双引号可以括住单引号

##知识点2：常见字符串方法
name = "ada lovelace"

#title：把每个单词首字母变大写
print(name.title())
#upper：把每个字母都变大写
print(name.upper())
#lower：把每个字母都变小写
print(name.lower())

##知识点3：字符串拼接

first_name = "ada"
last_name = "lovelace"

#字符串拼接用"+"号
print(first_name+last_name)
#两个引号之间可以省略"+"号
print("hello,"+first_name.title()+last_name.title()+" ""!")

##知识点4：字符串使用制表符

print("hello\n\thello")


##知识点4：删除空白 strip rstrip lstrip

favorite_language = " Python "

#删除字符串末尾的空白
print(favorite_language.lstrip())
#删除字符串前面的空白
print(favorite_language.rstrip())
#删除字符串两端的空白
print(favorite_language.strip())


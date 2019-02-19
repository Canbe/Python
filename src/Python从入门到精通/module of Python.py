##python3 模块

##知识点1：模块是拓展名为py的文件,py3中已经不支持隐式导入
#import src
#src.test_module.test1_func(1,2)

##知识点2：导入特定的函数
#from src.test_module import test1_func

#test1_func(1,2)

##知识点3：指定别名

#from src.test_module import test1_func as func

#func(1,2)

##知识点4：导入所有函数
from src.Python从入门到精通.test_module import *


test1_func(1,2)

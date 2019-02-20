#python3 处理json数据

import json

data = [1,2,3,4,5,6]

with open("test.json",'r') as f_obj:
    data_copy = json.load(f_obj)
    data_copy[1] = 100
    print(data_copy)
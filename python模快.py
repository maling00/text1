import random

# 返回随机小数
# ret = random.random()
# print(ret)

# 返回大于1小于100的随机小数
# ret = random.uniform(1,100)
# print(ret)

# 返回随机整数
# ret = random.randint(1, 5)
# 返回大于等于1并且小于5之间的整数
# print(ret)
# 返回大于等于1小于10之间的奇数
# ret = random.randrange(1, 10, 2)
# print(ret)

# 随机选择一个返回
# ret = random.choice([1, 2, 3, 4, 5, [2, 1], 6])
# print(ret)
# 随机选择多个返回，返回的个数为函数的第二个参数
# ret = random.sample([1,2,4,[2,1,12],"ffasd"],2)
# print(ret) # 返回的是个列表，列表里面有两个元素
# 打乱列表顺序
# item = [1,2,4,7,3,6]
# random.shuffle(item)
# print(item)


# 生成随机验证码
# code = ""
# for i in range(6):
#     num = str(random.randint(0,9))
#     num1 = random.randint(97,122)
#     num2 = random.randint(65,90)
#     num1_chr = chr(num1)
#     num2_chr = chr(num2)
#     code_c = random.choice([num,num1_chr,num2_chr])
#     code += code_c
# print(code)
#

import sys

# sys模块是与python解释器交互的一个接口

# sys.argv： 命令行参数list，第一个元素是程序本身路径
# sys.exit(n)： 退出程序，正常退出时exti(0)，错误退出sys.exit（1）
# sys.version : 获取python解释程序的版本信息
# sys.path: 返回模块的搜索路径，初始化的时候使用PYTHONPATH环境变量的值
# sys.platform： 返回操作系统平台名称

import time

# ret = time.time()    #产生时间戳
# print(ret)
# ret = time.strftime("%Y-%m-%d %H:%M:%S")  # 产生格式化的字符串时间
# print(ret, type(ret))
# ret = time.localtime()
# print(ret)
# 时间戳-------->结构化时间，用localtime或者是gmtime
# res = time.localtime(ret)
# print(res)
# res1 = time.gmtime(ret)
# print(res1)
# res2 = time.gmtime(123458943)
# print(res2)
# 结构化时间------->时间戳
# res = time.mktime(res2)
# print(res)
# 结构化时间---->字符串时间
# res = time.strftime("%Y-%m-%d %H:%M:%S", res2)  # 传入字符串的格式和结构化时间，如果不传入结构化时间的话，默认当前时间
# print(res)
# 字符串时间------>结构化时间
# res = time.strptime("1973-11-29 22:09:03", "%Y-%m-%d %H:%M:%S")  # 传入字符串时间和字符串时间的格式
# print(res)

# res1 = time.ctime(129929)  # 传入的参数是时间戳，不传入的话就是按照现在的时间来
# print(res1)

# res1 = time.asctime(time.localtime(123434444))
# print(res1)
# print(time.time()) #时间戳 -->方便机器去计算
# time.sleep(1)
# print(123)
# 格式化时间能够看得懂的时间---->字符串
# print(time.strftime("%Y/%m/%d"))
# print(time.strftime("%c"))
# print(time.localtime(40))
# print(time.struct_time())

# 2018-5-22 11:02:50
# 2018-5-21 12:59:30
# time_now = time.mktime((2018-5-22 11:02:50))
# time_old = time.mktime((2018-5-21 12:59:30")
# time_now = time.strptime("2018-5-22 11:02:50", "%Y-%m-%d %H:%M:%S")
# time_now1 = time.mktime(time_now)
# print(time_now1)
# time_old = time.strptime("2018-5-21 12:59:30", "%Y-%m-%d %H:%M:%S")
# time_old1 = time.mktime(time_old)
# print(time_old1)
# c_time = time_now1 - time_old1
# print(c_time)
# c1_time = time.localtime(c_time)
# print(c1_time)
# import os
# print(os.getcwd())
# import sys
# print(sys.platform)
# print(sys.version)
# print(sys.exit())

# 序列化模块
import json

# 其他特定的的数据类型转换成str 序列化 dumps
# str转换成其他特定的数据类型的过程叫反序列化 loads
# dumps方法
# dic = {"k": "v"}
# print(dic, type(dic))
# ret = json.dumps(dic)  # 序列化 把字典转化成字符串，在控制台显示的就是双引号（str）
# print(ret, type(ret))
# 反序列化 str--->dict/list/tuple
# res = json.loads(ret)
# print(res, type(res))

# li = [1,2,3,4,5]
# li1 = json.dumps(li)
# print(li1,type(li1))
# li2 = json.loads(li1)
# print(li2,type(li2))

# 在元组中，序列化一个元组是变成了列表的形式
# tu = (1, 2, 3, 4, 5)
# tu1 = json.dumps(tu)
# print(tu1, type(tu1))
# tu2 = json.loads(tu1)
# print(tu2, type(tu2))

# 所有语言都通用的一种数据结构
# 支持：list
#      dict
#      字符串
#      数字

# 元组和list非常像
# 元组是作为一个列表被序列化的，所有在转回来的过程中也只能转成一个list
# 在字典中 json的key 必须是一个字符串，否则转换之后会由int --->str，所有key必须是一个字符串
# json能处理的数据类型有限
# 不能连续load
# dic = {"k": "v"}
# ret = json.dumps(dic)
# with open("json_demo", encoding="utf-8", mode="w")as f:
#     f.write(ret)
# with open("json_demo", encoding="utf-8", mode="r")as f:
#     res = f.read()
# res1 = json.loads(res)
# print(res1)

# dump方法 和 load方法
# dic = {"k": "v"}
# with open("json_demo1", encoding="utf-8", mode="w")as f:
#     json.dump(dic, f)
#     json.dump(dic, f)
# with open("json_demo1", encoding="utf-8")as f1:
#     print(json.load(f1))
# dumps和loads方法：
# 内存中的转换  数据类型<-------->str
# dump和load方法：
#   文件和内存之间在文件中操作  数据类型<------>str

# int_a = 123
# ret = json.dumps(int_a)
# print(ret, type(ret))
# res = json.loads(ret)
# print(res, type(res))


import pickle

# 优势：几乎可以处理所有的数据类型
# 可以连续的向文件中dump和load
# 只能python中用

# shelve --- 简单不全面


# pickle的dumps


dic = {"k": "v", (1, 2, 3): {"a", "b", "c"}}
# res = pickle.dumps(dic)
# print(res)  # 序列化的结果是bytes类型
# d = pickle.loads(res)
# print(d)

# with open("pickle_demo2", "wb")as f:
#     pickle.dump(dic, f)
# with open("pickle_demo2", "rb")as f:
#     print(pickle.load(f))
# 可以多次dump和load

import shelve

import os
# os.makedirs('dirname1/dirname2')    可生成多层递归目录
# os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
# os.remove()  删除一个文件
# os.rename("oldname","newname")  重命名文件/目录
# os.popen("bash command).read()  运行shell命令，获取执行结果
# os.path.abspath(path) 返回path规范化的绝对路径 os.path.split(path) 将path分割成目录和文件名二元组返回 os.path.dirname(path) 返回path的目录。其实就是os.path.split(path)的第一个元素 os.path.basename(path) 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。
#                         即os.path.split(path)的第二个元素
# os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
# os.path.isabs(path)  如果path是绝对路径，返回True
# os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
# os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
# os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.getatime(path)  返回path所指向的文件或者目录的最后访问时间
# os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
# os.path.getsize(path) 返回path的大小

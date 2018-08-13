# 1.请写出[元祖，列表，字典，集合]的定义方法、新增方法、更改方法、删除方法(4分)
"""
tuple:  只读列表，不能增删改 只能查询 （儿子不能改，孙子可能能改）
list: 容器类    append insert extend    remove clear del  索引改查  切片改查
dic: 字典的key   必须是不可变数据类型，是唯一的
    字典的value 可以是任意数据类型
    setdefault()   pop clear  del   update   直接通过键找 值

set:集合是一个可变的数据类型，他是以{}形式存在的，空集合用 set（）表示，
        但是它要求它里面的元素是不可变的，集合是无序的，不重复的。



"""




# 2. 解释生成器（generator）与函数的不同，并实现且使用简单generator（3分）
"""
 生成器内部有eyeld  
 一个next或send 对应一个eyeld 
def func():
    a=1
    yield a
b=func()
for i in b:
    print(i)


"""

#3. 如何理解lambda函数 / 表达式（2分）

"""
匿名函数
 lambdai  参数x   对参数进行操作

"""
# 4.利用python打印前一天的本地时间，格式为"2018-01-30"（面试题）(3分)
"""
import time
time1=time.time()
time2=time1-(60*60*24)
time3=time.localtime(time2)
time4=time.strftime("%Y-%m-%d",time3)
print(time4)

"""

# 5.python中search()和match()的区别(面试题)(3分)

"""
 相同: 都是找一个符合的项  都有两个参数  一个是正则表达式 另一个是待匹配的
不同:search 找到符合的第一个     match  相当于正则表达式的开头有一个^   代表只找开头的

"""
# 6.描述一下 @ property是做什么用的，简单写一个实例并执行（4分）
"""
将方法伪装成属性
class Foo:
    def __init__(self, age):
        self.__age = age
    @property
    def age(self):
        return self.__age-10
l1 = Foo(18)
print(l1.age)


"""

# 7.说明__init__和__new__的作用(2分)
"""
__new__:  创建一个属性  
__init__ :  进行初始化


"""
# 8.用最简洁的方式生成这样一个列表[4，16，32，64，128](3分)
"""
print([2**i for i in range(2,8) if i !=3])

"""



# 9.
# d = {'k1': 'v1', 'k2’:[1,2,3],(‘k’,’3’):{1，2，3}}请用程序实现：
# 1）输出上述字典中value为列表的key（2分）
# 2）如果字典中的key是一个元祖，请输出对应的value值。（2分）
"""
d = {'k1': 'v1', "k2":[1,2,3],("k","3"):{1,2,3}}
for i in d:
    if type(d[i])==list:
        print(i)
    if type(i)== tuple:
        print(d[i])


"""





# 10.
# 如果不使用 @ wrapper装饰器，请在a()之前加入一句代码，达到相同的效果（2分）
#
# def wrapper(func):
#     def inner(*arg, **kwargs):
#         func(*arg, **kwargs)
#
#     return inner
#
#
# def a(arg):
#     print(arg)
#
#
# a()
"""
a=wrapper(a)

"""
# 11.请处理文件7th_questions, 输出所有以'T'开头的行（5分）
"""
with open ("7th_questions",encoding="utf-8")as f:
    for i in f: #每一行
        j=i.strip()
        for k in j:
            if k[0]=="T":
                print(i)

"""





# 12.读登陆文件夹中的代码，请为这段代码画流程图（8分）

"""
纸上"""


# 13新式类和金典类(旧式类)的区别(一种一分)(2分)
"""
新式类: 在py3中  默认继承object 
经典类:  需要手动继承object的是新式类,  不继承object的是经典类

"""


# 14
# 装饰器是什么时候被执行的(3
# 分)
"""
    def inner()
        ret=f()
        
        被执行
        return ret
    return inner

"""


# 15
# 什么是粘包，如何避免？(3分)

"""
黏包  是tcp协议会发生的,tcp是面向字节流的 发送send 和recv的时候可能会发生黏包
   自定义协议 struct模块

"""
# 16
# 叙述
# TCP、UDP
# 的区别(2
# 分)
"""
tcp    安全  面向连接 字节流
udp       不面向连接  速度快

"""
# 17
# 简述你对管道、队列的理解；（3
# 分）
"""
管道: 先进先出  内部pickle实现的   不安全
 
队列: 管道+锁  队列里自带互斥锁  维护了先进先出的顺序   且保证了数据的安全

"""
# 18.
# 创建一个闭包函数需要满足哪几点？（2 分）
"""
 有一个外层函数
内层闭包函数需要对外层函数的局部变量进行引用，不能引用全局变量。
 
 """


# 19.
# 用什么模块能知道文件夹存不存在？
# 怎么获取这个文件夹的大小？(2分)
"""
os 
os.path.exists(path)
os.getsize
"""
# 20
# 简单解释Python中staticmethod（静态方法）和classmethod（类方法）(2分)

"""
static method（静态方法）:即引用类变量（静态变量或类方法）也没引用对象属性的方法 可以当成普通函数来用。
class method（类方法）:引用了类变量（静态变量或类方法）但没有引用对象属性的方法 约定俗成默认传cls

"""
# 21.
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？（编程题）(5分)
"""
a=[1,2,3,4]
b=[str(int(i))+str(int(k))+str(int(j))for i in a  for j in a for k in a  if i !=j and i !=k and k!=j ]
print("组成的个数为:%s "%(len(b)))
print("分别是: %s"% b)

"""
# 22.
# 有这个一个test2文件，文件中模拟一个网站的页面定义了多个函数，现在有个需求是不使用if，else条件语句，
# 进行判断然后调用我要使用的函数(5 分)

# 例如：
# 请输入你要访问的url >> >：login
# 然后执行test2文件中的函数


# 23.
# 实现一个发红包的编程题（使用random）编程题(10)
"""
import random
def red(money,num):
    l=[]
    for i in range(num-1):
        a=money*random.random()
        l.append(a)
        money -= a
    l.append(money)
    return l
print(red(20,5))

"""




# 24.
# 读以下代码，写出答案并简述原因(面试题建议不使用电脑)(5
# 分)
# 下面代码会输出什么：
#
# def f( x, l = []) :
#     for i in range(x):
#         l.append(i * i)
#     print(l)
#
#
# f(2)
# f(3, [3, 2, 1])
# f(3)

"""
[0, 1]  在一个内存空间
[3, 2, 1, 0, 1, 4]  添加到了列表 是开辟了一个新空间 
[0, 1, 0, 1, 4]   还是在一个内存空间

"""

# 25.
# 写一个socket客户端和服务端并进行通讯(5
# 分)
"""
见客户端 服务器
"""
# 二
# 面向对象（30
# 分）
#
# 1.
# 请简述类、对象、实例化、实例这些名词的含义（2分）

"""
类：具有相同属性和性能
对象：对类进行具体的描述 实例化出来的 
实例化：从一个类中创建一个对象
实例：一个对象

"""

# 2.
# 面向对象的三大特性是什么？（3
# 分）
"""  多态 继承 封装 
"""
# 3.
# 有一个类定义：(5)
#
#
# class Person：
#
#
# def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#
# 1）初始化10个不同的对象（2）


# 2）求最高age的对象的name（3）

"""


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

li = []
for i in range(10):
    name = input('name:')
    age = int(input('age:'))
    p = Person(name,age)
    li.append(p)

"""



# 4.
# 模拟cs游戏（15分）
# 1）人物角色分为警察和匪徒两种，定义成两个类（10
# 分）
#
# 所有的警察的角色都是police
# 每个警察都有自己独有名字，生命值，武器，性别
# 每个都可以开枪攻击敌人，切攻击目标不能是police
#
# 所有的警察的角色都是terrorist
# 每个匪徒都有自己独有名字，生命值，武器，性别
# 每个都可以开枪攻击敌人，切攻击目标不能是terrorist
# 2）实例化一个警察，一个匪徒，警察攻击匪徒，匪徒掉血（2
# 分）
# 3）提取警察类和匪徒类相似之处定义成一个父类，使用继承的方式减少代码重复（3
# 分）
# class Person():
#     def __init__(self,name,sex,hp,weapon):
#         self.name=name
#         self.sex=sex
#         self.hp=hp
#         self.weapon=weapon
# class Police(Person):
# class Terrorist(Person):


#
# class Police():
#     def __init__(self,name,sex,hp,weapon):
#         self.name=name
#         self.sex=sex
#         self.hp=hp
#         self.weapon=weapon
#     def attack(self):
#
#
#
#
#
# class Terrorist():
#     def __init__(self,name,sex,hp,weapon):
#         self.name=name
#         self.sex=sex
#         self.hp=hp
#         self.weapon=weapon
# class Weaopn():
#     def __init__(self, name, ad):
#         self.name = name
#         self.ad = ad
#
#
# alex=Police("alex","男",20,"ak47")
# taibai=Terrorist("太白","男",15,"098k")
# ak47=Weaopn("ak47",30)
# o98k=Weaopn("o98k",25)


# 5
# 读代码（10
# 分）
#
# 5（1）
#
# class Base:
#     def f1(self):
#         self.f2()
#
#     def f2(self):
#         print('...')
#
#
# class Foo(Base):
#     def f2(self):
#         print('9999')
#
#
# obj = Foo()
# obj.f1()

# 问题1: 面向对象中的self指的什么？（2
# 分）

"""
传入的对象  使用该方法的对象
"""
# 问题2: 写出运行结果并简述原因（3分）
"""
9999
foo这个类 继承了base这个类,所以base是它的父类, obj调用f1函数先从自己类中找, 找不到往父类中找父类中调用了f2这个函数
因为是foo这个类调用f1  所以要到自己的类中先找有没有f2这个函数 显然是有的, 然后执行f2这个函数  打印9999


"""

# 5（2）
#
# class JustCounter:
#     __secretCount = 0
#
#     def count(self):
#         self.__secretCount += 1
#         print(self.__secretCount)
#
#
# class Bars(JustCounter):
#
#     def count(self):
#         print(self.__secretCount)
#
#
# counter1 = JustCounter()
# counter2 = Bars()
#
# counter1.count()
# counter2.count()
# print(counter1.__secretCount)
#
# 问题1: 简述counter1.count()执行流程？（2分）





# 问题2: 运行结果并简述原因（3
# 分）

# 运行结果: 先打印1，再报错


   
# 附加思考题（20
# 分）：
# 有一个数据结构如下所示，请编写一个函数从该结构数据中返回由指定的字段和对应的值组成的字
# 典。如果指定字段不存在，则跳过该字段。（10
# 分）
# data: {"time": "2016-08-05T13:13:05",
#        "some_id": "ID1234",
#        "grp1": {"fld1": 1,
#                 "fld2": 2},
#        "xxx2": {"fld3": 0,
#                 "fld5": 0.4},
#        "fld6": 11,
#        "fld7": 7,
#        "fld46": 8}
#
# fields: 由
# "|"
# 连接的以
# "fld"
# 开头的字符串, 如: fld2 | fld3 | fld7 | fld19
#
#
# def select(data, fields):
#     # TODO:implementation
#     return result
#
#
# def select(data, fields):
#     fields_lst = fields.split(‘ | ’)
#     for key in data:
#         if type(data[key]) == dict:
#             pass
#     return result
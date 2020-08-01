from numpy import *;#导入numpy的库函数
import numpy as np; #这个方式使用numpy的函数时，需要以np.开头。

print("\N{Cat}")
greet="hello"

#sequence 序列
print(greet[-1])#负数表示从右往左数，第一个为-1，第二个为-2
print(greet[1:3:1])#切片slicing 表示从第a个到b-1个，步长为c
print(greet[:-3:-1])#默认为首尾，可以倒序
print(greet[3::-1])
print(len(greet))
print(max(greet))

greeting= greet+" you there! "#拼接
greeting = greeting*2#重复
greetnone = [[greeting, None], None]  #组合
print(greeting)
print("you" in greeting)  #查找
print(None in greetnone)
print([greeting, None] in greetnone)


#list 列表
af=list('Hello')#创建了列表类
print(af)
bt=''.join(af)#拼接为字符串
print(bt)
af[3]='t'   #修改
del af[2]   #删除
print(af)

af[2:]=list('el what') # 给切片赋值，替换为不同序列
af[2:2]=list('ll')#插入新元素
print(af)
af[-3::-2]=list('bcdef')# 当不是在某个位置插入时，要求长度一致
print(af)


obj=[1,2,3]
obj.append(4)
print(obj)
obj_2=obj
obj_2[2]=4#指向相同内存，知识名称不同，同时修改
print(obj)
obj_3=obj.copy()#新建了内存，两者无关系
obj_4=list(obj)
obj_5=obj[:]#这两种方法也不会改变，均是新建了存储空间
obj_3[2]=6
print(obj)


#列表函数调用：
lst=[1,2,3,4,[1,2],[1]]
lst2=list("dell is good")

lst.append(5)#添加单个元素，[1,2,3,4,5]，直接修改
a=lst.copy()#复制
ct=lst.count([1])#计算[1]出现的次数

#lst.clear()#清空[]

lst.extend(a)#在lst后附加列表a，直接修改，与拼接不同
lst.index([1])#元素第一次出现时的索引,没有时跳出异常,不会继续运行
print(lst)

lst.insert(3,'three')#将某一个对象插入列表
print(lst)
lst.insert(4,list('list'))#不能直接print，为什么？？？因为其并不会返回一个值，而是直接改变
lst[4:4]=['l','i','s','t']
print(lst)

lst.pop()#弹出最后一个元素并返回，改变原值，pop(0)从开头弹出
lst.append(5)#push可以用append 替代，没有提供专有

lst.remove('l')#删除第一个指定元素，若没有则报错。与pop区别：修改但不返回值

lst.reverse()#翻转列表，不返回值。
y=reversed(lst)#则近返回翻转列表，不改变对象。迭代器作用

lst2.sort()#修改列表，对列表排序（从小到大）。类型不同需要设置比较方法！类似地使用y=sorted（lst)
lst2.sort(key=len,reverse=True)#带参数的排序，排序依据和是否翻转





##元组：不可修改的序列
#可以作为映射的键值
#用括号括起
x=(1,)#单个元组
print(x)
x=1,2,3
print(x)#为啥可以修改？？？新建了另一个内存，不是修改。
#x[2]=1  会报错 'tuple' object does not support item assignment
y=tuple([1,2,3,4,5])


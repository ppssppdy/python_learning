#字符串  与序列的区别是不可直接修改内容(注意命名不要和已有的库等重复)
from string import Template
from math import e, pi
tb='who\'s your daddy'
#tb[3:3]='se'不可修改

#格式输出
#方法1：
format="hello, %s, %s enough for ya?" #百分号指定插入的位置和形式
values=('world','Hot') #元组表示插入的内容
print(format % values)
print("hello, %s ,%s enough for ya?"%(1,'Hot'))

#方法2： 模板字符串
tmp=Template("hello, $who, $what enough for ya?")
print(tmp.substitute(who='babi',what='loli'))#视为对参数提供值

#字符格式设定：字段名 转换标志 格式说明 
#字段名： 默认从前往后的顺序，不能同时手工和自动编号混用，有名称的和无名称的有区别（比如下面{3}报错）
print("{2},{0},{1},{value:.2f}.".format('first','second','third',value=4.243542))
print('const value is {p:.4f} and {e:.2f}'.format(p=pi,e=e))

#类型可查表 常用： 二进制b 字符c 整数d 定点小数f 默认小数g 字符串c 十六进制x
print(' value is {p:b} and {e:g}'.format(p=22,e=e))
#指定宽度 数字和字符串不同
print("{name:10},{num:10}".format(num=3,name='Bob'))
#指定精度 . 分隔符，
print('const value is {p:10.4f} and {e:20,d}'.format(p=pi,e=100**10))

#格式打印 填充数字0 左对齐< 右对齐> 居中^
print("{name:010},{num:10}".format(num=3,name='Bob'))
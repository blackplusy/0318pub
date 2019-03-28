#coding=utf-8
#设置字符集
#字符集就是翻译官，文件开头就需要定义字符集，常见字符集utf-8，GBK2312
#直接输出
# #代表注释，#后面跟的内容不会对代码产生影响，主要用于提示
#1.直接输出
print('您访问的网页不存在')
print(250)

#2.变量输出
a=100
#a是变量的名字，等号是赋值，100是要给变量的值
print(a)
b=200
#变量也可以进行操作，必须是同数据类型变量
#变量运算后结果输出
print(a+b)

#3.函数输出
# abs()   绝对值
# len()   元素的个数
print(abs(10))
a='abc'
print(len(a))

#4.格式化输出
#  %s   格式化显示字符类型数据
#  %d   格式化显示数字类型数据
name='python'
num=1
print('%s is no.%d'%(name,num))
name='heygor'
print('your name is %s' % name)











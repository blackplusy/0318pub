#coding=utf-8
a='hello memeda!'
#索引
print(a[0])
print(a[-2])
print(a[10])
#切片
print(a[2:])
print(a[-3:])
print(a[2:5])
print(a[:-2])

#字符串拼接
a='python'
b='super 6'
print(a[0]+b[-1])

#字符串遍历
for i in a:
    print(i)

#去空格
#strip()   去掉所有空格
#lstrip()  去掉左边空格
#rstrip()  去掉右边空格
a='   hello   '
print(a.strip())
print(a.lstrip())
print(a.rstrip())

#计算元素个数
#len() 函数
print(len(a))

print('************')
#单引号、双引号
print('hello')
print("hello")
#print('i'm your baba ')
print("i'm your mom!!")
print('say "hi baby!!"')

#三引号
#1.注释
#2.多行打印
'''
下面代码是用来把老板炒掉的
'''
print('我的名字是gaga')
print('我的年龄是18')
print('我的爱好是女')

print('''
我的名字是gaga
我的年龄是18
我的爱好是女
是哒
''')



















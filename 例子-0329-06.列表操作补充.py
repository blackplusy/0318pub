#coding=utf-8
'''
栈方式访问列表
'''
#列表.append()是向列表中新增元素
#列表.pop()是把列表中最后一个元素弹出(删除)
l=[1,2,3,4]
print(l)
l.append(5)
print(l)
l.append(6)
print(l)
l.pop()
print(l)
l.pop()
print(l)
'''
获取列表索引
'''
#列表.index() 元素第一次出现时候的索引
print('---------')
l1=[1,2,3,3,2,1]
print(l1.index(2))
l2=['a','b','c','a']
print(l2.index('a'))
#enumerate 获取索引和值
l3=['gaga','tfboy','dfsq']
for index,value in enumerate(l3):
    print('索引是：'+str(index)+' 值是：'+value)
print('---------')
'''
列表的排序
'''
l=[1,4,2,5,7,8.3]
print(l)
l.reverse()
print(l)

l=[1,4,2,5,7,8,3]
print(l)
l.sort()
print(l)

l=[1,4,2,5,7,8,3]
print(l)
l.sort(reverse=True)
print(l)




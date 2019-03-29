#coding=utf-8
'''
列表访问
'''
#直接访问
l=[1,2,3,4,5]
print(l)
print(type(l))

#遍历访问
for i in l:
    print(i)
    print(type(i))
#成员运算符访问
if 3 in l:
    print('3 is here!')

'''
列表的索引和切片
'''
l=['heygor','o8ma','ladeng','xiaoquan']
print(l[0])
print(l[-2])
print(l[:3])
print(l[1:3])
print(l[3:])
#print(l[8])

'''
列表的拼接
'''
l=[1,2,3]
l2=[4,5]
print(l+l2)

'''
列表的更新
'''
l=[1,3,5,7,9]
l[2]=8
print(l)
l[-3]=100
print(l)


'''
列表的删除
'''
l=[1,3,5,7,9]
del l[2]
print(l)
del l
print(l)




















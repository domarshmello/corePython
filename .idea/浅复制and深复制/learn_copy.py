import copy
# 改变了a的内容 b也是指向a的内容 内容改变了 地址也改变
a=[1,3,9]
print(id(a))
b=a
print('列表b为：',b)
print(id(b))
if id(a)==id(b):
    print('a的地址 和 b 的地址相同 ：\n ',id(a),id(b))
# 浅复制 c 不是指向a 引用指向的内容
c=copy.copy(a)
print(id(a)==id(c))


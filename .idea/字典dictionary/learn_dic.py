# 命名方式{} dic={'apple':1，'pear':2}
# [key v]  value可以是个字典
# 对字典的声明创建以及增加 删除
dic1={'apple':1,'pear':2}
dic2={1:'a',2:'b'}
# 查找字典里的apple
print('查找字典里的apple这个key 对应的 value 是 :',dic1['apple'])

# 删除字典的元素 del dic1['pear']
del dic1['pear']
print('删除字典的元素 pear 的后的字典是：',dic1)

# 增加元素到字典里  dic1['orange']=3
dic1['orange']=3
print('增加 orange 元素 到 字典里：',dic1)

# 增加元素到字典里 value可以是个字典  可以字典里套字典
dic1['grape']={1:'littegrape',2:'bigGrape'}
print('增加 grape 元素到字典里 value可以是个字典',dic1)


# 增加元素到字典里 value可以是个列表
dic1['alist']=[1,2,3,4]
print('增加 alist 元素到字典 dic1 里 value可以是个列表',dic1)

# 增加元素到字典里 value可以是个fun()  可以字典里套字典  ？ 待完善

print('-----查找字典的=------')
print('dic1字典里的grape这个key对应的 的value是个字典，字典 的 key 2 内容是 ：',dic1['grape'][2])


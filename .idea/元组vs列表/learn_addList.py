a_list=[1,2,3,2,6,5,-1]
# 增加 insert()
# 第一个参数代表插入的位置 ，第二个参数代表插入的值
a_list.insert(1,0)
print(a_list)

# remove(第一次出现的2)
a_list.remove(2)
print(a_list)
# 打印倒序的数字
print("打印出列表最后一个值 : ",a_list[-1])
# 打印前3个数  使用切片符 :  from arg1 to arg2
print(a_list[0:4])
# 从第5 位到最后 5:
print(a_list[5:])

# 打印列表里的第一个2的索引位置
print("列表里第一次出现 2 的位置 ：",a_list.index(2))
# 统计列表里出现4的次数
print("统计列表里出现4的次数 :",a_list.count(4))
# 对列表从小到大排序 而且会覆盖原有的list sort()
a_list.sort()
print(a_list)
# 逆序排序  sort（reverse=True)
a_list.sort(reverse=True)
print(a_list)
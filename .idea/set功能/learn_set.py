char_list=['a','b','c','a','a','d','e','f']

# set可以去掉重复的元素 返回形式类似字典的key组合
print(set(char_list))

print("----查看类型---")
print(type(set(char_list)))
print("------查看字典类型--")
print(type({1:'q',2:'w'}))

sentence='welcome to my world,my World is beautiful'
# 打印出来是个乱序的字典 大小写字母占用内存不同 会有区分 包括空格
print(set(sentence))
print("------合并着玩-------")
unique_char=set(char_list)
# 添加相同元素（元组）的话 就是检索到已知存在的话 不加
unique_char.add('x')
# 清除全部
# unique_char.clear()
# print(unique_char)
print(unique_char.remove('x'))
print(unique_char)

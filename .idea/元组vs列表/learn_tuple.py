# 元组声明形式 1:a_tuple=(1,2,3)  2:b_tuple=9,10,11

a_tuple=(1,2,3)
b_tuple=(9,10,11)


# 字典迭代循环输出
a_list=[5,7,9,8]
b_list=[0,2,11,8]

print("---输出 a_list ---")
for content in a_list:
    print(content)

print("---输出 b_list ---")
for index in range(len(b_list)):
    print('index =',index,' num in list is',b_list[index])

print("---输出元组 b_tuple ---")
for j in range(len(b_tuple)):
    print('j =',j,' num in list is',b_tuple[j])
print("---输出元组 a_tuple ---")
for i in a_tuple:
    print(i)

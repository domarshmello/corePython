a_list=[1,2,3]
b_list=[4,4,5]
print("-------zip竖向对齐合成元组tuple-----------")
print('返回一个功能：',zip(a_list,b_list))
print("-------转换成list输出 ----------")
print(list(zip(a_list,b_list)))

print("-----可以当迭代器使用的よ------")
for i,j in zip(a_list,b_list):
    print(i/2,j*2)
print('---------------------------')

def fun(x,y):
    return (x+y)

print('调用fun方法 返回结果 ： ',fun(2,5))

print('-----------lambda----------------')

fun2=lambda x,y:x+y
print("lambda定义简单的方程 ：",fun2(2,8))

# map就是将已知的功能加参数
print('----------map----------------')

print('test map 输出结果是 object :', map(fun,[1],[2]) )


print('-------转换成list 输出 map ---------')

print('test list（map） 输出结果是  :',list(map(fun,[1],[2])) )
print('-------转换成list 输出 map(fun 列表中第一个对应相加  1+2=3,3+9=12) ---------')
print('test list（map） 输出结果是  :',list(map(fun,[1,3],[2,9])) )

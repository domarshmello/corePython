# 函数封装功能 提供接口被调用
# 冒号 代表 in 在函数内部

a=1
b=2
c=a+b
print(c)

# 定义一个函数
def sum(a,b):
    c=a+b
    print(' this is sum(a,b) function  ')
    print(c)

# 调用函数
sum(5,7)


print("-------------------")
def dream_car(price,color='pink',brand='MINI',is_owner=True):
    print('price',price,
          'color',color,
          'brand',brand,
          'is_owner',is_owner)
dream_car(300000)
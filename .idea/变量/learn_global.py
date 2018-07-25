# 全局变量 字母大写
APPLE=1000

g=None
# 定义函数
def fun():
    global g
    g=30
    return g+20

# 调用函数
print("---测试变量APPLE  局部变量a ------")

print(APPLE)
print('past g の valueg is',g)
print(fun())

print('now g の valueg is ', g)

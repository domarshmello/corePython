# class の  __init__
# tips:报错原因 __init__   两个_ ， 即__init__
class Calculator:
    # 指的是调用属性时使用 self.name 类似java自己写构造方法
    def __init__(self,name,price):
        self.n=name
        self.price=price
    def times(self,x,y):
        print(x*y)
# 测试类的功能
c=Calculator('Bad name', 10)
print(c.n, c.price)
c.times(11,20)

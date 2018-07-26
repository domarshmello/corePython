class Calculator:
    name='a goog calculator'
    price=199
    # 指的是调用属性时使用 self.name
    def add(self,x, y):
        print(self.name)
        result=x+y
        print(result)
    def minus(self,x,y):
        print(x-y)
    def times(self,x,y):

        print(x*y)
# 测试类的功能
calculator=Calculator()
print("名称：",calculator.name," \n价钱：",calculator.price)
calculator.add(11,20)

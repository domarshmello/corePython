from collections import Iterable
# 1种

# def how_many_null(lst: list):
#     count = 0
#     for x in lst:
#         if isinstance(x, Iterable):
#             if len(x) == 0:
#                 count += 1
#     return len(lst) - count
# lst=[1, 2, 3, (), [], '', 5, '', 7]
# print(how_many_null(lst=lst))





# 2种
# def how_many_null(lst: list):
#     def __len__(self):
#         count = 0
#         for x in lst:
#             if hasattr(x, '__iter__'):
#                 if len(x) == 0:
#                     count += 1
#         return len(lst) - count

#
# lst=[1, 2, 3, (), [], '', 5, '', 7]
# print(how_many_null(lst=lst))

# len 这个函数不属于任何集合 len不属于任何类，它属于 buildins  它存在的意义是为了调用集合自带的__len__()
class Shixiong(list):
    def __len__(self):
        # 覆盖了 __len__  直接调用不行  需用父类的__len__()调用 然后因为父类的__len__的参数只有 self ，
        # 运行的同时会把存在的该类实例带进去 不需要传参数 隐式包含进去了233
        count = 0
        for x in self:
            if hasattr(x, '__iter__'):
                if len(x) == 0:
                    count += 1
        return super().__len__() - count


lst2 = Shixiong([1, 2, 3, (), [], '', 5, '', 7])

print(lst2.__len__())
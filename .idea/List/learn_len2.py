

lst=[1, 2, 3, (), [], '', 5, '', 7]
# class S(list):
#     def __len__(self):
#         for i in list:
#             if(len(i)==0):
#                list = list.remove(i)
#         return len(list)


def how_many_notNull(lst:list):
    return len(list(filter(lambda x:x is not None,lst)))
lst2=how_many_notNull(lst)
print(lst2)

print([] is not [])

# 重写父类__len__

lst=[1, 2, 3, (), [], '', 5, '', 7]
print('--1--')
print (" lst length : ",len(lst))

class S(lst):
    def __len__(self):
        while [] in lst:
            lst.remove([])
            print(lst)
            print('--2--')
        while '' in lst:
            lst.remove('')
            print(lst)
            print('--3--')
        while () in lst:
            lst.remove(())
            print(lst)
            print('-------')

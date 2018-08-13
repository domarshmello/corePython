lst=[1, 2, 3, (), [], '', 5, '', 7]
print (" lst length : ",len(lst))

print('--------')
class myList(list):
    def __len__(self):
        index=0
        var= iter(self)
        while True:
            try:
                if next(var):
                    index+=1
            except StopIteration:
                break
        return index
lst2=myList(lst)
print(len(lst2))
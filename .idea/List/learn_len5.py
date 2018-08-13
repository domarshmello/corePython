class MashList(list):
    def __len__(self):
        count = 0
        for x in self:
            if self.is_empty(x):
                count += 1
        return super().__len__() - count

    def remove_empty(self):
        return MashList(filter(lambda x: not self.is_empty(x), self))

    @staticmethod
    def is_empty(x):
        if hasattr(x, '__iter__'):
            if len(x) == 0:
                return True
        else:
            return False

lst2 = MashList([1, 2, 3, (), [], '', 5, '', 7])

print(len(lst2))
print(lst2.remove_empty())
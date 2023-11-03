import operator

class vector:
    def __init__(self,values) -> None:
        self.components = values
    
    def __iter__(self):
        return iter(self.components) ## nade the components iterable
    
    # def __getitem__(self,index):
    #     return self.components[index]

    def __getitem__(self,index):
        if isinstance(index,slice):
            cls = type(self)
            print('slice')
            return cls(self.components[index])
        else:
            print('operator used')
            index1 = operator.index(index)
            return self.components[index1]
    
# if __name__ == '__main__':
#     v = vector([1,2,3,4,5])
#     for i in v:
#         print(i)

v = vector([1,2,3,4,5])
#print(v[2])
print(type(v[slice(0,1,None)]))
c = v[slice(1,3,None)]
for i in c:
    print(i)

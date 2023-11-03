class vector:
    def __init__(self,iterable):
        self.data = list(iterable)

    def __iter__(self): ## allows for functions below to work without self.data
        return iter(self.data) 

    def __gt__(self,other):
        return all([1 for a, b in zip(self,other) if a > b])
    
    def __add__(self,other):
        print('called add')
        try:
            return vector([a+b for a, b in zip(self,other)])
        except TypeError:
            return NotImplemented
        
    def __matmul__(self,other):
        print('called mul')
        try:
            return vector([a*b for a, b in zip(self,other)])
        except TypeError:
            return NotImplementedError('Bad types')

    def __repr__(self):
        return f'{self.data}'
    
    def __radd__(self,other):  ## is other is not vector data type
        print('called radd')
        return self + other ### calls __add__
    
    def __eq__(self, other):
        if isinstance(other,vector):
            return len(self) == len(other) & all([a==b for a,b in zip(self,other)])
        else:
            return NotImplemented
        
    def __len__(self):
        return len(self.data)
    
    
v = vector([1,2,3])
b = vector([5,6,7])

print(b > v)
d = b+v
print(d)

k = [10,11,12]
print(k+b)

print(b@v)
print(b@k)  ## @ is matmul, * should be overloaded for scalar
print(k*b)  ## 


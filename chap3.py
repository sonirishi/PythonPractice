# def dump(**kwargs):
#     print(kwargs)
#     #print(x,y,c)

# dump(**{'x':1,'y':5,'c':3})

# def dump(x,y,c):
#     #print(kwargs)
#     print(x,y,c)

# dump(**{'x':1,'y':5,'c':3})

# my_dict = {}

# import collections

# print(isinstance(my_dict,collections.defaultdict))
# print(isinstance(my_dict,collections.abc.Mapping))
# print(isinstance(my_dict,collections.abc.MutableMapping))

# my_dict = {'1':'ris','2':'son'}

# print('1' in my_dict)
# print('ris' in my_dict)

# print(my_dict.keys())
# print(my_dict.items())

# for _,val in my_dict.items():
#     print(val)

# for data, val in zip([1,2,3],[4,5,6]):
#     print(data,val)

# from collections import OrderedDict

# dict_new = OrderedDict({'1':'rishabh','2':'shivangi'})

# # dict_new.popitem(last=False)
# # print(dict_new)

# dict_new.setdefault('3','bhag')

# print(dict_new['3'])
# print(dict_new.items())

import collections

class ListBasedSet(collections.abc.Set):
     ''' Alternate set implementation favoring space over speed
         and not requiring the set elements to be hashable. '''
     def __init__(self, iterable):
         self.elements = lst = []
         for value in iterable:
             if value not in lst:
                 lst.append(value)
     def __iter__(self):  ## operator overloading
         return iter(self.elements)
     def __contains__(self, value):
         return value in self.elements
     def __len__(self):
         return len(self.elements)

s1 = ListBasedSet('abcdef')
s2 = ListBasedSet('defghi')

print(len(s1))

for i, j in enumerate(range(10),3):
    print(i,j)


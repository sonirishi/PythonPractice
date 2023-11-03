# class coordinate:

#     def __init__(self,lat,long):
#         self.lat = lat
#         self.long = long
    
# moscow = coordinate(2,3)
# delhi = coordinate(2,3)

# print(moscow == delhi)

# class coordinate2:

#     def __init__(self,lat,long):
#         self.lat = lat
#         self.long = long
    
#     def __eq__(self,obj):
#         return self.lat == obj.lat and self.long == obj.long
    
# moscow = coordinate2(2,3)
# delhi = coordinate2(2,3)

# print(moscow == delhi)

# from collections import namedtuple

# city = namedtuple('city','city country lat long')

# print(city._fields)

# delhi_data = city('delhi','india',3,4)

# delhi = city._make(delhi_data)
# print(delhi._asdict())

# print(delhi_data)

# print(city(*delhi_data))

# from Chapter1 import Vector

# a = Vector(2,3)

# print(Vector)

from dataclasses import dataclass

@dataclass
class DemoDataClass:
    a:int
    b:float = 1.1
    c = 'spam'

from typing import NamedTuple

class DemoNTClass(NamedTuple):
    a:int
    b:float = 1.1
    c = 'spam'

@dataclass(frozen=True)
class DemoDataClassfroz:
    a:int
    b:float = 1.1
    c = 'spam'

#print(DemoDataClass.a)  ## cant call a
#print(DemoNTClass.a)
#print(DemoDataClassfroz.a)  ## cant call a

# @dataclass()
# class tempclass:
#     a:int
#     b:float = 1.1
#     c = 'spam'  ## if i add annotation str to it, it becomes instance attr

# print(tempclass.__annotations__)
# print(tempclass.__dataclass_fields__)

@dataclass()
class tempclass1:
    a:int
    b:float = 1.1
    c:str = 'spam'  ## if i add annotation str to it, it becomes instance attr

print(tempclass1.__annotations__)
print(tempclass1.__dataclass_fields__)  ## c appears
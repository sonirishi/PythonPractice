from chap4 import DemoDataClass

print(DemoDataClass.__annotations__)
print(DemoDataClass.__doc__)

cls = DemoDataClass(19)
print(cls.a)

cls.a = 20
print(cls.a) ## allows to change

from chap4 import DemoNTClass

print(DemoNTClass.__annotations__)
print(DemoNTClass.__doc__)

obj = DemoNTClass(19)
print(obj.a)

#obj.a = 20 ## not allowed, hence a better class type?

from chap4 import DemoDataClassfroz

print(DemoDataClassfroz.__annotations__)
print(DemoDataClass.__doc__)

cls1 = DemoDataClassfroz(19)
print(cls1.a)

cls1.a = 20
print(cls1.a) ## frozen works for this same as nametuple
from collections import UserDict

print(UserDict.mro())
print('*************')
print(dir(UserDict)) ## list of all function

a = 'rish'
b = iter(a)
print(next(b))  ## keep on doing next
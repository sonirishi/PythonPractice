def func(a,b):
    print(id(a))  ##aliases passed
    print(id(b))
    a.append(5)
    b.append(6)
    print(a);print(b)

a = [2,3]
b = [4,5]

print(id(a))
print(id(b))

func(a,b)
print(a); print(b)  ##appended to actual data

a = [2,3]
b = [4,5]

from copy import copy
func(copy(a),copy(b))
print(a); print(b)  ## copy is fine
# dict1 = {'name':'rishabh','job':'GS'}
# dict2 = dict1
# print(dict2 is dict1)
# print(dict2 == dict1) ##__eq__ for dict

# dict3 = {'name':'rishabh','job':'GS'}

# print(dict3 is dict1) ## it is a replica, not using same id is compares id
# print(dict3 == dict1) ##__eq__ for dict

l1 = [4,[44,55,66],(7,8,9)]
l2 = l1.copy()

# l1.append(100)
# l1[1].remove(55)
# l2[1].extend([77,88])
# l2[2] += (10,11)

# print(l1) ## [4, [44, 66, 77, 88], (7, 8, 9), 100]
# print(l2)  ## [4, [44, 66, 77, 88], (7, 8, 9, 10, 11)]

# print(id(l1)) ## different ids
# print(id(l2)) ## different ids
# print(id(l1[1]))  ## same ids
# print(id(l2[1])) ## same ids

# print(id(l1[2]))  ## same ids as they refer to same object
# print(id(l2[2])) ## same ids

# print(id(l1[2]))
# print(id(l2[2]))

# l2[2] += (10,11)

# print(id(l1[2]))
# print(id(l2[2]))  ## new location

print(id(l1[2]))
print(id(l2[2]))

l2[1].extend([77,88])

print(id(l1[1]))
print(id(l2[1]))
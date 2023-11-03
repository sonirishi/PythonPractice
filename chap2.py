# a,b,*rest = range(5)
# print(rest)
# print(a,b)

# a,*rest,b = range(5)
# print(rest)
# print(a,b)

# def fun(a,b,c,d,*rest):
#     print(a,b,c,d,rest)

# fun(*[1,2],3,*range(6))

# match_items = [
#     ['rishabh','soni',[123,456]],
#     ['shivangi','sharma',[456,789]],
#     ['yashika','soni',[178,3900]]
# ]

# def match_code(items):
#     for _,_,[n1,n2] in items:
#         if n2 > 500:
#             print(n1)

# match_code(match_items)

# def test_code(*a):
#     print(a)

# test_code(*[1,2,3])

# string = 'bicycle'
# print(string[::2])
# print(string[::-3])

# invoice = """
# 0.....6.......................................40...........52....56.........
# 1909   Rishabh                                   123           1    59
# 2345   Shivangi                                   423           2    56
# """
# SKU = slice(0,6)
# Name = slice(6,40)
# item = slice(40,52)
# a = slice(52,56)
# b = slice(56,None)

# line_items = invoice.split('\n')[2:]
# for items in line_items:
#     print(items[SKU],items[Name])

# tup = (1,2,3)
# print(isinstance(tup,tuple))

# tup[3] = 4 ## immutable

# t = (1,2,[30,40])

# t[2] += [50]
# print(t) ## this still changes t though gives error
# ## bytcode wise it pushese the list on TOP, now list is mutable hence
# ## concat is allowed by reassignment to tuple isnt
# ## however as the reference list has changed so has the tuple

# from array import array

# arr = array('h',[-2,-1,0,1,2])
# print(arr)
# mem = (memoryview(arr))  ## share memory between data structures without copying

# mem_1 = mem.cast('B')

# mem_1 = mem_1.to_list()
# print(mem_1)
# mem_1[5] = 10
# print(arr)
# print(mem_1)

import time
for n in (100000, 200000, 300000, 400000):
    data = b'x'*n
    start = time.time()
    b = data
    while b:
        b = b[1:]
    print(f'     bytes {n} {time.time() - start:0.3f}')

for n in (100000, 200000, 300000, 400000):
    data = b'x'*n
    start = time.time()
    b = memoryview(data)
    while b:
        b = b[1:]
    print(f'memoryview {n} {time.time() - start:0.3f}')
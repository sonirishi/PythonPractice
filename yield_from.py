def gen1():
    yield 1
    yield from gen2()
    yield 2
    ## added using vim, insert is i

def gen2():
    yield 3
    yield 4
    yield 5

for val in gen1():
    print('*'*50)
    print(val)

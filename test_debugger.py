import pdb

def test_debug(a,b):
    a = a + b
    b = a - b
    breakpoint()
    a = a*b
    b = b*a
    return a,b

c,d = test_debug(2,3)
# def testfunc(a,b,*args,**kwargs):
#     print(a,b)
#     print(args)
#     print(kwargs)

# testfunc(1,2,3,4,name='rishi')

from functools import partial

def testfunc(a,b,c,d):
    return a*b*c*d

newfunc = partial(testfunc,1)

print(newfunc)
print(newfunc(2,3,4))
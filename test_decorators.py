def main_decorate(doit=True):
    def decorate(func):
        def inner(*args):
            """
            decorator func
            """
            if doit:
                result = func(*args)
                return result
            else:
                return 0    
        return inner
    return decorate
from numpy import sum

# @main_decorate(doit=True)
# def testfunction(input):
#     return sum(input)       

# print(testfunction([1,2,3,4]))

@main_decorate(doit=False)
def testfunction1(input):
    """
    Details on the func
    """
    return sum(input)       

print(testfunction1([1,2,3,4]))
print(testfunction1.__name__)
print(testfunction1.__doc__)

from functools import wraps

def main_decorate1(doit=True):
    def decorate1(func):
        @wraps(func)
        def inner1(*args):
            if doit:
                result = func(*args)
                return result
            else:
                return 0    
        return inner1
    return decorate1

@main_decorate1(doit=False)
def testfunction2(input):
    """
    Details on the func
    """
    return sum(input)       

print(testfunction2([1,2,3,4]))
print(testfunction2.__name__) ## functools wraps keeps the function details
print(testfunction2.__doc__)
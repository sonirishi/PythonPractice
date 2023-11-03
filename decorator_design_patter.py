from typing import Callable, Optional,List

calculate = Callable[[int],int]  ## inside input, outside return

calctypes: List[calculate] = []

def calc(inputfunc: calculate) -> calculate:
    calctypes.append(inputfunc)
    return inputfunc

def getbest(val: int) -> int:
    return (max(calctype(val) for calctype in calctypes))

@calc
def func1(val):
    return val*1.2

@calc
def func2(val):
    return val+10

@calc
def func3(val):
    return val*1.1 + 25

if __name__ == '__main__':
    print(globals().items())
    print(getbest(1.8))
    print(getbest(0.08))


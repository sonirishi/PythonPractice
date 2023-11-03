# registry = []

# def register(func):
#     print('register')
#     registry.append(func)
#     return func

# @register
# def f1():
#     print('run f1')

# @register
# def f2():
#     print('run f2')

# def f3():
#     print('run f3')

# def main():
#     print('run main')
#     f1()
#     f2()
#     f3()

# if __name__ == '__main__':
#     main()

# b = 6
# def test(a):
#     print(a)
#     print(b)

# test(3)

# b = 6
# def test(a):
#     print(a)
#     print(b)
#     b = 10

# test(3)
from numpy import mean

# def make_avg():
#     series = []
#     def avg_func(new_val):
#         series.append(new_val)
#         return mean(series)
#     print(f'avg_func id = {id(avg_func)}')
#     return avg_func
    
# avg = make_avg()
# print(avg(10))
# print(avg(11))
# print(avg(12))
# print(id(avg))

# temp = make_avg()
# print(temp(20))

# print(avg.__code__.co_varnames)
# print(avg.__code__.co_freevars)
# print(avg.__closure__)

# def tst():
#     print('test')

# print(tst.__closure__)  ## no closure

# def make_avg():
#     count = 0
#     total = 0
#     def new_avg(val):
#         count += 1 ## doesnt work as above for series as immutable
#         total += val
#         return total/count
#     return new_avg

# avg = make_avg()
# print(avg(10))

def make_tst():
    total = 10
    def new_tst(val):
        return total + val  ## referencing the variable is fine
    return new_tst

newtest = make_tst()
print(newtest(10))
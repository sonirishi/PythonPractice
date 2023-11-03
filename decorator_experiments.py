from functools import lru_cache

from dec_clock import clock

# @lru_cache(maxsize=40)
# @clock
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)

# @clock
# def fib1(n):
#     if n < 2:
#         return n
#     return fib1(n-1) + fib1(n-2)

# if __name__ == '__main__':
#     fib1(4)

@lru_cache
@clock
def test_dec(input,i):
    return test_dec(input[i:],i+1) 

# import time

# def clock1(func):
#     def clocked(input,i):
#         t0 = time.perf_counter()
#         results = func(input,i)
#         elapsed = time.perf_counter() - t0
#         name = func.__name__
#         #arg_str = ', '.join(repr(arg) for arg in args)
#         #print(f'{arg_str} and {name}')
#         print(elapsed)
#         return results
#     return clocked

# @clock1
# def test_dec1(input,i):
#     if len(input) == 0:
#         return None
#     return test_dec1(input[i:],i+1) 

if __name__ == '__main__':
    test_dec([1,2,3,4,5],0) ### unhashable error for lru_cache
#     test_dec1([1,2,3,4,5],0)
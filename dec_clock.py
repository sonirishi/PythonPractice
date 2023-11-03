import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        results = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'{arg_str} and {name}')
        print(elapsed)
        return results
    return clocked
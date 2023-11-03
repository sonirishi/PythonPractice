from contextlib import contextmanager
import sys

@contextmanager
def looking_glass():
    original_write = sys.stdout.write

    def reverse_write(text):
        return original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'ABC'
    sys.stdout.write = original_write

if __name__ == '__main__':
    with looking_glass() as what:
        print("Rishabh is trying")
        ## some error here can cause issue
        print(what)
    print('*'*10)
    print(what)
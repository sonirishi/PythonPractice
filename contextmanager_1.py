from contextlib import contextmanager
import sys

@contextmanager
def looking_glass():
    original_write = sys.stdout.write

    def reverse_write(text):
        return original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = 'temp'
    try:
        yield
    except ZeroDivisionError:
        msg = 'No Zero divide'
    finally:
        sys.stdout.write = original_write
        print(msg)

if __name__ == '__main__':
    with looking_glass() as what:
        print("Rishabh is trying")
        ## some error here can cause issue
        print(what) ## Nothing yielded by generator so None
    print('*'*10)
    print(what)
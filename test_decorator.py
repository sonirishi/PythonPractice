import time
from dec_clock import clock

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

if __name__ == '__main__':
    print(f'calling snooze {snooze(.2)}')
    print('*'*40)
    print(f'factorial {factorial(6)}')
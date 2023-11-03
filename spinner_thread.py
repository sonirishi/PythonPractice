import itertools
import time
from threading import Thread, Event

def spin(msg,done):
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status,end='',flush=True)
        if done.wait(.1):
            print('enter wait')
            break
    blanks = ' '*len(status)
    print(f'\r{blanks}\r', end='')

def slow():
    print('enter slow')
    time.sleep(3)
    return 42

def supervisor():
    done = Event()
    spinner = Thread(target=spin,args=('thinking',done))
    print(f'spinnger object: {spinner}')
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result

def main():
    result = supervisor()
    print(f'Answer {result}')


if __name__ == '__main__':
    main()
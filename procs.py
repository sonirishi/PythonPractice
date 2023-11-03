import sys
from time import perf_counter
from typing import NamedTuple
from multiprocessing import Process, SimpleQueue, cpu_count
from multiprocessing import queues
from primes import is_prime, NUMBERS

class PrimeResult(NamedTuple):
    n: int
    prime: bool
    elapsed: float

Jobqueue = queues.SimpleQueue[int]
Resultqueue = queues.SimpleQueue[PrimeResult]

def check(n):
    t0 = perf_counter()
    res = is_prime(n)
    return PrimeResult(n,res,perf_counter()-t0)

def worker(jobs,results,i):
    print(f'process started {i}')
    while n := jobs.get():
        print(n)
        results.put(check(n))
    results.put(PrimeResult(0,False,0.0))

def start_jobs(procs,jobs,results):
    for n in NUMBERS:
        jobs.put(n)
    #print(jobs)
    for i in range(procs):
        proc = Process(target=worker,args=(jobs,results,i)) ## args to worker function
        print(f'initiated process {i}')
        proc.start()
        #print(i)
        jobs.put(0)
        print(f'adding 0 to process {i}')

def main():
    if len(sys.argv) < 2:
        procs = cpu_count()
    else:
        procs = int(sys.argv[1])
    t0 = perf_counter()
    jobs = SimpleQueue()
    results = SimpleQueue()
    start_jobs(procs,jobs,results)
    checked = report(procs,results)
    elapsed = perf_counter() - t0
    print(f'time elapsed {elapsed}')

def report(procs, results):
    checked = 0
    procs_done = 0
    while procs_done < procs:
        n,prime,elapsed = results.get()
        if n == 0:
            procs_done += 1
        else:
            checked += 1
            label = 'P' if prime else 'N'
            print(f'printing {n} {label} {elapsed}')
    return checked

if __name__ =='__main__':
    main()


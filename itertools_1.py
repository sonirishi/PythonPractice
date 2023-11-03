import itertools as it

sample = [5,8,3,1,4,5,7,8,5,7]

generate = it.accumulate(sample)

print(list(it.accumulate(sample,min)))

for value in generate:
    print(value)

names = ['rishabh','rishabh','pappu','pappu','pappu']

for _, group in it.groupby(names,len):
    print(f'Group list {list(group)}')

for char, group in it.groupby(names):
    print(f'Group new {len(list(group))}') ## good one!!

from operator import mul

gensum = map(mul,range(11),it.repeat(5,11)) ## map creates generate

for val in gensum:
    print(val)

pp = enumerate(it.accumulate(sample),1)  ## start enumerate from 1

for value in pp:
    print(value)

p2 = it.starmap(lambda a, b: b/a, enumerate(it.accumulate(sample),1))
## enumerate creates the tuple, start map can process iterator with iterator

for val in p2:
    print(val)

p3 = it.starmap(lambda *a: '-'.join(a),[('1','2','3'),('4','5','6'),('7','8','9')])

for val in p3:
    print(val)


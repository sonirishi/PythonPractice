def make_average():
    count = 0
    total = 0
    def averager(new_value):
        ## print(total) ## this doesnt work as compiler think its local
        nonlocal count, total
        count += 1
        total += new_value
        print(f'nonlocal {total}')
        return total/count
    return averager

avg = make_average()
print(avg(10))
print(avg(20))
# print(locals())
# print(globals())

import inspect

print(inspect.getmembers(avg))

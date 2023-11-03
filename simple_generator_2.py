def running_sum(data):
    result = 0
    for value in data:
        result += value
        yield result

generate_sum = running_sum([1,2,3,4,5,6,7,8,9]) 

print(generate_sum)

print(next(generate_sum))

print('*'*50)

for val in generate_sum:  ## as we have already done 1 next, it starts from second iter
    print(val)

from itertools import product, combinations, tee

product_gen = product([1,2,3,4],[4,5,6,7])

print(next(product_gen))

comb_generate = combinations([1,2,3,5,6,7],2)

print(next(comb_generate))

g1,g2 = tee('rishabh')

print(list(g1))
print(list(g2))

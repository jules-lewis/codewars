
'''
While trying to implement a lazy list (still haven't achieved this!), I ended up 
writing a function to merge sorted generators, keeping the contents in order.
'''

# Yields an ordered list of results from generators a and b
def mergeGenerators(gen_a, gen_b):
    next_a = next(gen_a, None)
    next_b = next(gen_b, None)
    while True:
        if (next_a is None) and (next_b is None):
            return
        elif (next_a != None) and (next_b is None):
            yield next_a
            next_a = next(gen_a, None)
        elif (next_a is None) and (next_b != None):
            yield next_b
            next_b = next(gen_b, None)
        elif next_a < next_b:
            yield next_a
            next_a = next(gen_a, None)
        elif next_a > next_b:
            yield next_b
            next_b = next(gen_b, None)
        else:
            yield next_a
            next_a = next(gen_a, None)
            next_b = next(gen_b, None)


gen_a = (i for i in [1, 2, 3])
gen_b = (i for i in [1, 2, 3])
print(list(mergeGenerators(gen_a, gen_b)))


gen_a = (i for i in ['a', 'b', 'c', 'w', 'yankee', 'z'])
gen_b = (i for i in ['a', 'c', 'f', 'y', 'yahoo', 'yak'])
print(list(mergeGenerators(gen_a, gen_b)))


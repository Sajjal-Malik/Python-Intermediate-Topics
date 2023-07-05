def generator():
    yield 1
    yield 2
    yield 3

g = generator()

# n = next(g)
# print(n)
# n = next(g)
# print(n)
# n = next(g)
# print(n)

sum_of_g_values = sum(g)
# print(sum_of_g_values)

sorted_g_values = sorted(g)
# print(sorted_g_values)




def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1

# cd = countdown(5)
# value = next(cd)
# print(value)
# value = next(cd)
# print(value)
# value = next(cd)
# print(value)
# value = next(cd)
# print(value)



import sys

def firstN(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num = num + 1
    return nums

print(firstN(10))
# print(sys.getsizeof(firstN(100000)))
print(sum(firstN(10)))

def generator_firstN(n):
    num = 0
    while num < n:
        yield num
        num = num + 1

print(list(generator_firstN(10)))
# print(sys.getsizeof(generator_firstN(100000)))   # generators save a lot of memory for large data
print(sum(generator_firstN(10)))





def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(35)
# for i in fib:
#     print(i)




mygenerator = (i for i in range(10) if i % 2 == 0)    # uses tuple syntax but makes a generator
# print(tuple(mygenerator))
# print(sys.getsizeof(mygenerator))
for i in mygenerator:
    print(i)


mylist = [i for i in range(10) if i % 2 == 0]
print(mylist)
# print(sys.getsizeof(mylist))
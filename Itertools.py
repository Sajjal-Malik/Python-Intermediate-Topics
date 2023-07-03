from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator


ls_a = [1, 2]
ls_b = [3, 4]

prod = product(ls_a, ls_b)    # product function will calculate the catersian product of the passed arguments
# print(prod)    # it will create the itertools object so we need to convert it into an iterable

# print(tuple(prod))
# print(list(prod))


tp_a = (1, 2)
tp_b = (3,)

prod = product(tp_a, tp_b, repeat=3) 

# print(tuple(prod))
# print(list(prod))







ls_1 = [1, 2, 3]
perm = permutations(ls_1,)   # permutation is each of several possible ways in which a set or number of things can be ordered or arranged.
# print(list(perm))


ls_1 = [1, 2, 3]
perm = permutations(ls_1, r=2)    # defining no. of permutations using r as argument in permutation function
# print(list(perm))








ls_2 = [1, 2, 3, 4, 5]    # it makes combinations without repeated values
comb = combinations(ls_2, r=2)   # defining no. of permutations using r as argument in combinatin function is a must
# print(list(comb))

comb_wr = combinations_with_replacement(ls_2, r=2)    # it includes repeated values, it is opposite of (combinations) 
# print(list(comb_wr))






ls_3 = [1, 2, 3, 4]
acum = accumulate(ls_3)    # it is used to get the accumulated sum of elements of iterable
# print(list(acum))

# print(accumulate.__doc__)

ls_3 = [1, 2, 3, 4]
acum = accumulate(ls_3, func=operator.mul) 
print(list(acum))

ls_3 = [1, 2, 5, 3, 4 ]
acum = accumulate(ls_3, func=max) 
print(list(acum))









def smaller_than_3(x):
    return x < 3

ls_4 = [1, 2, 3, 4]
group_obj = groupby(ls_4, key=smaller_than_3)
for key,value in group_obj:
    print(key, list(value))



persons = [{'name':'sajjal', 'age':23}, {'name':'malik','age':23}, {'name':'john','age':22}, {'name':'ripper','age':21}]
group_obj = groupby(persons, key=lambda x: x['age'])
for key,value in group_obj:
    print(key, list(value))







# for i in count(10, 2):
#     print(i)
#     if i == 16:
#         break


# ls = [1, 2, 3]
# for i in cycle(ls):
    # print(i)

# for i in repeat(2, 4):
#     print(i)





# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# tple = ("apple", "mac", "linux")

# print(tple)
# print(type(tple))

# mytple = tuple(["apple", "orange","banana"])

# print(mytple)
# print(type(mytple))


mytple = ("sajjal", 23, True)

mytples = ('sajjal',)     # tuple with one value is defined like this


# mytple[2] = False    # this will give error becasue it is not supported by tuples

# print(mytple[0])

# print(mytple)

for i in mytple:
    print(i)

if 'malik' in mytple:
    print(True)
else:
    print(False)

if True in mytple:
    print(True)
else:
    print(False)




newtuple = ('a', 'b', 'c', 'd', 'e', 'f')

print(len(newtuple))

print(newtuple.count('f'))

print(newtuple.index('d'))







# Type Conversion from tuple to list and vice versa

tuple_to_list = list(newtuple)

print(tuple_to_list)

list_to_tuple = tuple(tuple_to_list)

print(list_to_tuple)


sliced_tuple = newtuple[1:5]

print(sliced_tuple)



mytuple = ('a', 'b', 'c', 'd', 'e', 'f')

print(mytuple[:5:3]) 
print(mytuple[::-1])   # reversing the tuple using slicing







# Packing and Unpacking in Python Tuples

tuple_for_unpacking = ('Sajjal', 23, 'BSCS')

name, age, study = tuple_for_unpacking

print(name)
print(age)
print(study)







tuple_for_unpacking = ('Sajjal',20, 21, 22, 23, 'BSCS')

val_first, *vals_all, val_last = tuple_for_unpacking

print(val_first)    # first value will be passed to this variable
print(vals_all)     # all the remaing values will be passed to this variable and change it to  --> ( list )
print(val_last)     # last value will be passed to this variable






import sys

my_tuple = ('Sajjal', 23, 'BSCS')
my_list = ['Sajjal', 23, 'BSCS']

# Although they have same values but their size is different
print(sys.getsizeof(my_tuple), 'bytes')   
print(sys.getsizeof(my_list), 'bytes')




import timeit

print(timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]", number=1000000))
print(timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)", number=1000000))
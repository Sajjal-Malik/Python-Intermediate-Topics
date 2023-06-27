# List is a collection which is ordered and changeable. Allows duplicate members.

mylist = ['apple', 'orange', 'mango']
mylist2 = ['guava', 'blueberry']

# print(mylist + mylist2)
           

# print(mylist)

# if 'apple' in mylist:
#     print('yes')
# else:
#     print('no')


# newlist = mylist.append('pineapple')
# newlist = mylist.insert(1, 'banana')
# newlist = mylist.remove('banana')
# newlist = mylist.clear()
# print(newlist)

# There are still few methods left to implement   try them yourself


newlist = [0] * 5
newlist2 = [1,2,3,4,5]

# print(newlist)

newlist3 = newlist + newlist2      # works fine
# newlist3 = newlist * newlist2    # error
# newlist3 = newlist - newlist2    # error

print(newlist3)


newlist = [1,2,3,4,5,6,7,8,9,10,11,12]

# list indexing syntax --> [start, stop, step]
print(newlist[1:6])
print(newlist[2:3])
print(newlist[1:])
print(newlist[2:3:2])
print(newlist[:-1])
print(newlist[::-1])
print(newlist[:-3])
print(newlist[:-3][1:])



org_list = ['apple', 'orange', 'mango']

copy_list = org_list       # passing by reference

print(copy_list)

copy_list[2] = 'cherry'

print(copy_list)    # copy list is changed
print(org_list)     # original list is also changed


# To make a copy    copy(), list()-constructor and slicing  these ways are safe to use

copy_list = org_list.copy()

copy_list = org_list[:]

copy_list = list(org_list)

print(copy_list)    # this is a new list and completely safe to use anywhere in the program



# List comprehensions 
my_list = [1,2,3,4,5]

new_list = [i**2 for i in my_list]
new_list = [i for i in my_list if i % 2 == 0]

print(new_list)
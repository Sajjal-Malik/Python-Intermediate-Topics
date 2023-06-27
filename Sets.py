# Set is a collection which is unordered, changeable, and unindexed. No duplicate members.

set1 = {1,2,3}
set2 = set((1,2,3))
set3 = set([1,2,3])
set4 = set('hellow')

print(set1)
print(set2)
print(set3)
print(set4)


# Empty set - Wrong way
emp_set = {}
print(emp_set)  
print(type(emp_set)) # it is not a set but a dictionary

# Empty set - Right way
emp_set = set() 
print(emp_set)
print(type(emp_set))

new_emp = {()}
print(new_emp)
print(type(new_emp))



# Adding elements to the empty set
emp_set.add(1)
emp_set.add(2)
emp_set.add(3)
emp_set.add(4)
print(emp_set)



emp_set.remove(2)
# emp_set.remove(5)   # if element not there it will raise a key error
emp_set.discard(3)
# emp_set.clear()   # it will remove all elements
emp_set.pop()   # it removes an element in any order
print(emp_set)






# Looping throught the Sets
for i in set1:
    print(i)




# Checking values in the Sets
if 3 in set2:
    print('yes')

if 7 not in set3:
    print('right')




odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

union = odds.union(evens)
print(union)

intersection = odds.intersection(evens)
print(intersection)   # empty set is returned because there are no same elements

intersection = odds.intersection(primes)
print(intersection)  


intersection = evens.intersection(primes)
print(intersection)  








setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# difference method selects elements from set 1 only
diff = setA.difference(setB)
print(diff)
diff = setB.difference(setA)
print(diff)


# symmetric_difference method selects elements from both sets
diff = setA.symmetric_difference(setB)
print(diff)
diff = setB.symmetric_difference(setA)
print(diff)




# setA.update(setB)
# print(setA)

# setB.update(setA)
# print(setB)


# setA.intersection_update(setB)
# print(setA)

# setB.intersection_update(setA)
# print(setB)



# setA.difference_update(setB)
# print(setA)

# setB.difference_update(setA)
# print(setB)



# setA.symmetric_difference_update(setB)
# print(setA)

# setB.symmetric_difference_update(setA)
# print(setB)




setC = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setD = {1, 2, 3}
setE = {11, 22, 33}

print(setC.issubset(setD))   # Output: False
print(setD.issubset(setC))   # Output: True

print(setC.issuperset(setD))   # Output: True
print(setD.issuperset(setC))   # Output: False

print(setC.isdisjoint(setD)) # Output: False
print(setD.isdisjoint(setC)) # Output: False


print(setC.isdisjoint(setE)) # Output: True
print(setD.isdisjoint(setE)) # Output: True





setF = setA
print(setF)

setF.add(100)
print(setF)
print(setA)


setF = set(setA)
print(setF)

setF.add(200)
print(setF)
print(setA)

setF = setA.copy()
print(setF)

setF.add(300)
print(setF)
print(setA)





frozen_set = frozenset([1,2,3,4,5])
print(frozen_set)
print(type(frozen_set))
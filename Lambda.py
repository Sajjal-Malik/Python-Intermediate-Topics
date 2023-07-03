# syntax:       
# lambda x: x   # this x is a return value
# func = lambda x: x * x



lambda_add = lambda x: x + 10
# print(lambda_add(10))

lambda_mul = lambda x,y: x * y
# print(lambda_mul(10,11))   


points2D = [(1, 2), (15, 1), (5, -1), (10, 4)] 
points2D_sorted = sorted(points2D)     # by default it is arranging the values using 0 index elements

# print(points2D)
# print(points2D_sorted)





points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])     # now it will sort the values on behalf of 1 index elements
# print(points2D)
# print(points2D_sorted)

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1]) 
# print(points2D)
# print(points2D_sorted)





def sort_by_index_1(x):
    return x[1]

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=sort_by_index_1) 
# print(points2D)
# print(points2D_sorted)







# map(func, seq)   --------->
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
# print(b)     # map object
# print(list(b))

c = [x * 2 for x in a]
# print(c)




# filter(func, seq)   --------->
a = [1, 2, 3, 4, 5]
b = filter(lambda x: x%2==0, a)
# print(b)     # map object
# print(list(b))

c = [x for x in a if x % 2 == 0]
# print(c)






from functools import reduce
a = [1, 2, 3, 4, 5]
reduce_a = reduce(lambda x,y: x*y, a)
print(reduce_a)






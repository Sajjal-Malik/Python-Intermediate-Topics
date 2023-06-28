from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

string = "aaaaabbbcccc"

counter_string = Counter(string)
 
# print(counter_string)
# print(type(counter_string))   # class collections.Counter 

# print(counter_string.items())
# print(counter_string.keys())
# print(counter_string.values())

# print(counter_string.most_common())   # all elements are equally common 
# print(type(counter_string.most_common()))

# print(counter_string.most_common(1)) 
# print(counter_string.most_common(1)[0])
# print(counter_string.most_common(1)[0][0])

# print(list(counter_string.elements()))
# print(tuple(counter_string.elements()))
# print(set(counter_string.elements()))







# std = namedtuple('Student','name,age')
std = namedtuple('Student',['name','age'])   # namedtuple (Name, [Names of the field or Attributes])  in iterable form 
                                                                                                # either string or anyother
s = std('sajjal', 23)
print(s)
# print(type(pt))    # class __main__.point

print(s.name)
print(s.age)








# order_dic = {}
order_dic = OrderedDict()
order_dic['a'] = 1
order_dic['b'] = 2
order_dic['c'] = 3
# print(order_dic)
# print(type(order_dic)) # class collections.OrderedDict





default_dic = defaultdict()
default_dic['a'] = 1
default_dic['b'] = 2
# default_dic['c'] = '3'
default_dic['c'] = 'malik'
print(default_dic)
# print(default_dic['a'])
print(default_dic['c'])
# print(type(default_dic))  # class collections.defaultdict









d = deque()
d.append(1)   # by default append method add elements from the right or end
d.append(2)
d.append(3)

d.appendleft(4)   # this method add elements from the left or start
d.appendleft(5)
d.appendleft(6)

d.pop()         # by default pop method remove elements from the right or end
d.pop()

d.popleft()   # this method remove elements from the left or start
d.popleft() 

d.extend([4,5,6,7])
d.extendleft([9,8,7])

print(d)
# print(type(d))   # class collections.deque

# d.rotate(1)   # move or rotate elements from the right or end side
d.rotate(-1)    # move or rotate elements from the left or start side
print(d)
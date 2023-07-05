import random

number = random.randint(0, 10)   # it will never select number 10 but between the range 0 to 9

# print(number)      # these are sudo random numbers



mylist = list("ABCDEFGHIJKLMNOP")

rand = random.choice(mylist)    # it will select only one unique element

rand = random.sample(mylist, 4) # it selects more than one  unique elements , and return a list

rand = random.sample(mylist, k=3) # it allows to select more than one element but elements can be similar as well , and return a list

random.shuffle(mylist)

# print(mylist)



random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))
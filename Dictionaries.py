# Dictionary is a collection which is ordered** and changeable. No duplicate members.

myDict = {'name': 'sajjal', 'age':23, 'city': 'BWP'}
print(myDict)

# my_Dict = dict(name='malik', age=23, city='BWP')
# print(my_Dict)


# value1 = myDict['name']
# value2 = myDict['age']
# print(value1)
# print(value2)



# As we know dictionary is mutable let's check to make sure
myDict['city'] = 'Berlin'   
myDict['state'] = 'PUNJAB'   # if a key:value is not there using this way we can add it to the dictionary
print(myDict)


# To delete items we can use
# del myDict['age']
# myDict.pop('state')
# myDict.popitem()   # it is like pop method of list, it removes the last element




# To check if the keys are in the dictionary
if 'name' in myDict:
    print(myDict['city'])
else:
    print('specified key is not in the dictionary')

try:
    print(myDict['lname'])
except:
    print("Error caught!")


checking = myDict.get('name', 'None')   # if key is found it's value will be returned
print(checking)
checking = myDict.get('email', 'email key is not in the dictionary')   # if key is found it's value will be returned
print(checking)


print('-------------------------------------------')

# For looping through dictionaries
for item in myDict:    # it prints keys only
    print(item)

print('-------------------------------------------')

for item in myDict.items():   # it prints both in tuple format
    print(item)
    # print(type(item))

print('-------------------------------------------')

for key, value in myDict.items():   # it prints value only
    print(key,value)
    # print(type(key or value))

print('-------------------------------------------')

for key in myDict.keys():   # it prints keys only
    print(key)

print('-------------------------------------------')

for value in myDict.values():   # it prints value only
    print(value)





# Copying the list
myDict_copy = myDict
print(myDict_copy)

myDict_copy['email'] = 'user@example.com'
print(myDict_copy)
print(myDict)   # original dictionary has changed




new_dict = myDict.copy()
new_dict = dict(myDict)
new_dict['email2'] = 'user2@example.com'
print(new_dict)
print(myDict)



# Changing and Updating the values or keys of a dictionary
myDict1 = {'fname': 'sajjal', 'oldage':23, 'oldcity': 'BWP'}
# my_Dict2 = dict(name='malik', age=24, city='Berlin')
# my_Dict2 = dict(lname='malik', newage=24, newcity='Berlin')

# myDict1.update(my_Dict2)
# print(myDict1 )


new_dict1 = {2:4, 3:9, 4:16, 5:25}
# tple = [8, 7]   # list cannot be set as key for the dictionary
tple = (8, 7)
new_dict1 = {tple: 15}    # tuple can be set as key for the dictionary
print(new_dict1)




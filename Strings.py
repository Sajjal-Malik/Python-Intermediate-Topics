# Strings in python are surrounded by either single quotation marks, or double quotation marks. they are ordered, immutable and iterable

mystring = "Hello World"
mystring = 'Hello World'
mystring = "Hello I'm learning python from the World'"
mystring = 'Hello I"m learning python from the World'
mystring = """Hello I'm learning 
python         from       the 
World"""
mystring = '''Hello I'm learning 
python   from    the 
World'''

# print(mystring)



string = 'I am a student'
# print(len(string))
# print(string[1:4])
# print(string[1:-1])
# print(string[::1])   # by default step value is 1
# print(string[::2])
# print(string[::-1])


# string[0] = 'i'  # ERROR:   string does not support item assignment (because they are immutable)
# print(string)


fname = 'Sajjal'
lname = 'Malik'
fullname = fname + " " + lname
# print(fullname)






# eid_greetings = "Eid Mubarak to ALL loved ones"
# for i in eid_greetings:
#     if i == ' ':
#         continue
#     print(i)

# print("---------------------------------------")


# eid_greetings = "Eid Mubarak to ALL loved ones"
# for i in eid_greetings:
#     print(i)

# print("---------------------------------------")

# eid_greetings = "Eid Mubarak to ALL loved ones"
# for i in eid_greetings[::]:
#     print(i)

# print("---------------------------------------")

# eid_greetings = "Eid Mubarak to ALL loved ones"
# for i in eid_greetings[::2]:
#     print(i)

# print("---------------------------------------")

# print(len(eid_greetings))
# for i in range(len(eid_greetings)):
#     print(i)

# for i in range(len(eid_greetings)):
#     print(eid_greetings[i])



greeting = 'hello'
if 'e' in greeting:
    print('yes')




# greeting = '       hello     '
# print(greeting)

greeting = '       hello     '
stripped_greeting = greeting.strip()
print(stripped_greeting)    # new string changed
print(greeting)    # original string remainds the same



print(greeting.upper())
print(greeting.lower())
print(greeting.startswith(''))
print(greeting.endswith(''))
print(greeting.startswith(' '))
print(greeting.endswith(' '))
print(greeting.find('o'))
print(greeting.count('l'))
# new_greeting = greeting.replace('       hello     ', 'hello')
# print(new_greeting)


# ls_string = greeting.split()
# print(ls_string)

string = 'Hello buddy how are you?'
# print(string)
# string_ls = string.split("")  # this is by default for split("")
string_ls = string.split()
# print(string_ls)


string = 'Hello,buddy,how,are,you?'
print(string)
string_ls = string.split() # it will treat the string as one word whole
string_ls = string.split(",") # it will seperate the words on behalf of the delimeter   (comma -> ,)
# print(string_ls)

newstring = " ".join(string_ls)   # changing the list back to strings
# print(newstring)

from timeit import default_timer as timer


thisstring = ['a'] * 10000
# print(thisstring)
# print("-------------------------------------")

# not a good approach 
# start = timer()
emp_str = ''
for i in thisstring:
    emp_str += i
# stop = timer()
# print(emp_str)
# print(stop - start)

# print("-------------------------------------")

# better approach
# start = timer()
emp_str = ''.join(thisstring)
# stop = timer()
# print(emp_str)
# print(stop - start)





name = 'Sal'
age = 23
result_perc = 88.500000
var_str = "Hello %s" % name
var_str = "Hello %s and your age is %d it seems" % (name, age)
var_str = "Hello %s and your age is %d it seems and you got %.2f percentage in 7th Semester and  that is good" % (name, age, result_perc)
# print(var_str)



format_string = "hello {} you are {} years old".format(name, age)   # old way of formatting strings
print(format_string)


f_string = f"hello {name} you are {age} years old"    # new way of formatting strings
print(f_string)
# f_string = f"hello {name} you are {age*7} years old"    # making changes on runtime


raw_string = r"hello {name} you are {age} years old"   # raw strings 
print(raw_string)

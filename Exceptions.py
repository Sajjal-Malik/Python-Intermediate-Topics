# a = -5
# if a < 0:
#     raise Exception("X is negative")


# a = -5
# assert (a < 0), "X is negative"


# try:
#     a = 5 / 0
# except Exception as e:    # python will automatically(implicitly) raise the error according to the code
#     print(e)

 
# try:
#     a = 5 / 0
# except ZeroDivisionError as e:      # we can explicitly define and raise exception as well
#     print(e)
    

# try:
#     a = 5
#     b = a + 'hello'
# except TypeError as e:      # we can explicitly define and raise exception as well 
#     print(e)
    


# try:
#     a = 5
#     b = a + 10
# except TypeError as e:     
#     print(e)
# else:                           # if try run successfully then else will be executed
#     print("This will be printed when try is successfully executed, and Everything is fine!")
    



# try:
#     a = 5
#     b = a + 's'
# except TypeError as e:     
#     print(e)
# else:                          
#     print("This will be printed when try is successfully executed, and Everything is fine!")
# finally:
#     print("Finally block will be executed no matter what happens!")






# Making our own Error Class and Function ---------->
class ValueTooHighError(Exception):
    pass

def test_value_too_high(value):
    if value > 100:
        raise ValueTooHighError("Value is too high")
    
test_value_too_high(200)




class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(value):
    if value > 100:
        raise ValueTooHighError("Value is too high")
    if value < 5:
        raise ValueTooLowError("Value is too low", value)

try:
    test_value(2)
# except ValueTooHighError as e:
#     print(e)
except ValueTooLowError as e:
    print(e.message, e.value)
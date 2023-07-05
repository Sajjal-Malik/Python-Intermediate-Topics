def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print("Starting")
        result = func(*args, **kwargs)
        print("Ending")
        return result
    return wrapper

# @start_end_decorator
# def print_name():
#     print("Alex")

@start_end_decorator
def add_5(param):
    return param + 5

# print_name = start_end_decorator(print_name)   # we use decorator for this same purpose
# print_name()


result = add_5(10)
print(result)
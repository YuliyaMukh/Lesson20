
def decorator(func):
    def wrapper():
        print("Before starting...")
        func()
        print("After starting...")

    return wrapper

@decorator

def testing():
    print("testing...")

testing()
# def some():
#     print("some...")
#
#
# d = 10
#
# d = testing
# some = testing
#
# some()

# def decorator(func):
#     if type(func).__name__== "function":
#         func()
#
# decorator(testing)
# def decorator():
#     def wrapper():
#         print("testing wrapper function...")
#     return wrapper
#
# t = decorator()
# t()



# testing = decorator(testing)
# testing = decorator(testing)
# testing = decorator(testing)
# testing = decorator(testing)
#
# testing()
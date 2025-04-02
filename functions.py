def hello_world():
    print("Hello World!")


hello_world()  # Calling the Function

# functions with parameters
# def sum(num1, num2):
#     print(num1 + num2)
# # here num1 and num2 are parameters and the actual data is given in the form of arguments at the time of calling of function.
# sum(45, 85)


# def sum(num1=0, num2=0):      # provinding default values
#     if (type(num1)) is not int or type(num2) is not int:
#         return 0
#     return (num1 + num2)


# total = sum(2, 3)
# print(total)


# If there are multiple unknown parameters
def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Dave", "John", "Sara")


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Dave", last="Gray")

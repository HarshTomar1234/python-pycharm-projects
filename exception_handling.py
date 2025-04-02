x = 2
try:
    raise Exception("I'm a custom exception!")
    # print(x)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
except NameError:
    print('NameError means something is probably undefined')
except ZeroDivisionError:
    print("Pls don't divide by zero.")
except Exception as error:
    print(error)
else:
    print('No Error!')
finally:
    print("I'm am going to print with or without an error.")

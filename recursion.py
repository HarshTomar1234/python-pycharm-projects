# recursion = a function that calls itself from within
#  helps to visualise a complex problem into basic steps,which can be solved more easily iteratively or recursively.


def add_one(num):

    if num >= 9:
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)


mynewtotal = add_one(0)
print(mynewtotal)


# Another Example
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        # Fuction factorial is calling itself inside factorial func. with different argument
        return n * factorial(n-1)


print(factorial(5))


# Another Example(Fibonacci Sequence)
# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return f(n - 1) + f(n - 2)


# for i in range(10):
#     print(f(i))


# OR

value1 = 0
value2 = 1
for i in range(0, 10):
    if (i <= 1):
        next = i

    else:
        next = value1 + value2
        value1 = value2
        value2 = next
    print(next)

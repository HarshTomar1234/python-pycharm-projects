from functools import reduce


def squared(num): return num * num


# lambda num: num * num
print(squared(2))


def addTwo(num): return num + 2


# lambda num: num + num
print(addTwo(12))


def sum(a, b): return a + b


# lambda a, b : a + b
print(sum(8, 12))


################################
################################


def funcBulider(x):
    return lambda num: num + x


addTen = funcBulider(10)
addTwenty = funcBulider(20)

print(addTen(7))
print(addTwenty(7))


################################
################################

# Higher Order Function

numbers = [3, 5, 4, 8, 18, 21, 54]

squared_nums = map(lambda num: num * num, numbers)
# map is a built-in function in python that receives a function as it's first argument

print(list(squared_nums))

###########

odd_nums = filter(lambda num: num % 2 != 0, numbers)
# filter function return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true.

print(list(odd_nums))

############


numbers = [1, 2, 3, 4, 5, 6, 1]

total = reduce(lambda acc, curr: acc + curr, numbers)
# Apply a function of two arguments cumulatively to the items of a sequence or iterable, from left to right, so as to reduce the iterable to a singlevalue. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). If initial is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty.
print(total)


names = ["Dave Gray", " Sara Ito", "John Jacob"]
char_count = reduce(lambda acc, curr: len(curr) + acc, names, 0)
print(char_count)

import math
# String data type

# literal assignment

first_name = "Harsh"
last_name = "Tomar"

# Method for Checking datatype
# print(type(first_name))
# print(type(first_name) == str)
# print(isinstance(first_name, str))

# constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
# full_name = first_name + " " + last_name
# print(full_name)

# full_name += "!"
# print(full_name)

# Casting a number to a string
# decade = str(1980)

# print(type(decade))


# statement = "I like rock music from  " + decade + "s."
# print(statement)


# Multiple lines

# multiline = '''
# Hey, how are you?

# I was just checking in.
#                               All good?

# '''

# # print(multiline)

# # Escaping special characters
# # sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
# # print(sentence)


# # String Methods
# # print(first_name)
# # print(first_name.lower())
# # print(first_name.upper())
# # print(first_name)

# # print(multiline.title())
# # print(multiline.replace("good", "ok"))


# print(len(multiline))
# multiline += "                                                                                   "
# multiline = "                             " + multiline
# print(len(multiline))

# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# String index values
print(first_name[0])
print(first_name[-1])

print(first_name[1:-1])
print(first_name[1:])


# Some merhods return boolean data

print(first_name.startswith("H"))
print(first_name.endswith("N"))

# Boolean data type

myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.29
y = float(1.14)
print(type(y))
print(isinstance(gpa, bool))
print(isinstance(gpa, float))

# Complex type
comp_value = 5 + 3j
print(type(comp_value))
print((comp_value.real))
print((comp_value.imag))


# Built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))
print(round(gpa, 2))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zip_code = "001114"
zip_code = int(zip_code)
print(type(zip_code))


# Error if you attempt to cast incorrect data
# zip_code = int("New York")

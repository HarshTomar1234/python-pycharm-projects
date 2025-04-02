# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break          # Break statement stops the loop
#     value += 1

# value = 1
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

names = ["Dave", "Sara", "John"]
# for x in names:
#     print(x)


# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue     # Continue stops the current iteration and goes to the next one in loop
#     print(x)


# for x in range(4):
#     print(x)

# for x in range(2, 4):
#     print(x)


# Increment in range of numbers...
# for x in range(5, 101, 5):
#     print(x)
# else:
#     print("Glad that\'s over!")


names = ["Dave", "Sara", "John"]
actions = ["code", "eats", "sleeps"]

# Nested Loops
# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")


for action in actions:
    for name in names:
        print(name + " " + action + ".")

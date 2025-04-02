users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []


# checking particular qty. is in list or not..
print("Dave" in users)
print("Dave" in data)
print("Dave" in emptylist)

# Getting a value in list using index
print(users[0])
print(users[-2])
print(users[-1])


# Getting index of specific value
print(users.index("Sara"))


# Getting a range of values
print(users[0:2])  # It exclude last  index value
print(users[-3:-1])   # It exclude last  index value
print(users[0:])  # It include every value of list from index 0
print(users[1:3])   # It exclude last  index value


print(len(data))  # returns no. of items in list


# Adding an item in list
users.append("Carolina")
print(users)

# Adding a new list to previous working list
# Method 01
users += ["Danny", "Jason"]
print(users)
# Method 02
users.extend(['Robert', 'Katrina'])
print(users)


# Adding item at a particular spot in list
users.insert(0, "Florence")
print(users)


users[2:2] = ["Eddie", "Terry"]
print(users)

# Replacing values(Slicing)
users[1:3] = ["Angelina Jolie", "Yami"]
print(users)

# Removing Item from list
users.remove("Danny")
print(users)

# Popping off last item from list
print(users.pop())  # It also removes that last item from list
print(users)

# Deleting a specific item from list
del users[0]  # mentioning its index
print(users)

# Deleting a range of items using slicing
# del users[0:4]
# print(users)

# del data   '''It delete that list and cause error during printing and shows that list data is not defined although it is defined'''
data.clear()  # It makes list completely clear and empty and will show empty list existence
print(data)


# Sorting a list
users.sort()  # arranges list in alphabetical order
print(users)

users[1:3] = ["harsh", "gagan"]  # Relpacing(slicing) items at index 1 and 2
users.sort()
print(users)  # arranges upper case items first and lower case items later

# Including or making lower case items arranging at a coorect place in a list
# All the datatypes must be same during this method of sorting
users.sort(key=str.lower)
print(users)

# Reversing the list
nums = [4, 56, 45, 85, 96]
nums.reverse()
print(nums)

# nums.sort()
# print(nums)  # arranges in ascending order

# nums.sort(reverse=True)
# print(nums)  # arranges in descending order


# this will not change our nums list and on printing nums it shows earlier nums list
print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()  # Making copy of nums list
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

# Checking datatype of list
print(type(users))

# Creating list using constructor func.
mylist = list(["Yuan", "Neil"])
print(mylist)


# Tuples

# We can't change order in tuple and also data or items inside tuple will not change just like list

mytuple = tuple(('Dave', 5, True))

another_tuple = (1, 5, 48, 58, 5, 5, 5)  # Packing(assigning values) of tuple

print(mytuple)
print(type(another_tuple))


# Since Tuple can't be changed but we can add new item in tuple by this way
newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newlist)
print(newtuple)


# Unpacking tuple
(one, two, *hey) = another_tuple
print(one)
print(two)
print(hey)

print(another_tuple.count(5))

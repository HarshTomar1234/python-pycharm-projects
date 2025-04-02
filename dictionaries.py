# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page",
}

# Using constructor function to create dictionaries

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)

# Detection of Datatype
print(type(band))

print(len(band))   # shows no. of {key : value,...} pairs

# Access Items from dictionaries
print(band["vocals"])
print(band.get("guitar"))   # Using get method

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# Verify if key exist in dictionary or not
print("guitar" in band)
print("harmonium" in band2)

# Change Values
# chage the value of key("vocals") from Plant to Coverdale.
band["vocals"] = "Coverdale"

# update method is used to change values of key as well as also used to add another key/value pair..
band.update({"guitar": "Hendrix"})
band.update({"bass": "JPG"})
print(band)

# Removing items
# pop method return the value of key which is to be removed.
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

# popitem method removes the last key/value pair from the list and also return that removed key/value pair as tuple.
print(band.popitem())
print(band)

# Delete and clear items
band["drums"] = "Bonham"
# delete key("drums")and its value("Bonham") from dictionary(band).
del band["drums"]
print(band)

# make a dictionary empty and display curly braces with no key/value pairs.
band2.clear()
print(band2)

del band2  # completely delete the dictionary
# print(band2)  # shows error message that name 'band2' is not defined.

# Copying dictionaries

# band2 = band    # create a reference (both have same memory locations.)
# print("Bad Copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()   # both doesn't have same reference
band2["drums"] = "Dave"
print("Good Copy")
print(band)
print(band2)


# or use the dict() constructor func. for copying..
band3 = dict(band)
print("Good Copy")
print(band3)

# Nested Dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}

member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])


# Nesting
capitals = {
    "France":  "Paris",
    "Germany": "Berlin",
}

# Nesting a List in Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}


# # Nesting a Dictionary in Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 10},
}


# # Nesting a Dictionary in List
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10
    },
]


# #adding new country in the form of dictionary in travel_log list using function
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# Sets

nums = {1, 2, 3, 4}
nums2 = set({1, 2, 3, 4})
print(nums)
print(nums2)
print(type(nums))  # detecting datatype
print(len(nums))  # represent and shows no. of elements in set

# No duplicate allowed
nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1, false is  a dupe of zero.
set = {1, True, 2, False, 3, 4, 0}
print(set)


# check if a value is in a set
print(2 in set)

# but you cannot  refer to an element in the set with an index position or a key

# adding a new element to a set
set.add(8)
print(set)

# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# You can use update with lists, tuples, and dictionaries,too.


# Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7, 8}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 7, 8}
one.intersection_update(two)
print(one)


# keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 7, 8}
one.symmetric_difference_update(two)
print(one)

# Checking whether a set is subset of another set or not..
num1 = {1, 8, 9, 6, 7}
num2 = {5, 1, 9, 6, 3, 7, 8, 2}
print(num1.issubset(num2))
print(num1.issuperset(num2))
print(num2.issuperset(num1))


# Removing random item from the set
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

# Checking whether one set has some common elements with another set...
num3 = {4, 88, 95, 16}
num4 = {4, 85}
# isdisjoint function return True if both sets has no common elements otherwise if common elements exists it return False
print(num3.isdisjoint(num4))
print(num1.isdisjoint(num3))

# Removing particular item from set
num1.remove(8)
print(num1)

# remove method  will raise error when you are asking to remove that item which doesn't exist in list
# num3.remove(95)
# print(num3)

# Discarding specified item from set
# discard method doesn't raise error in case you are discarding item that is not present in the set
# num3.discard(88)
# print(num3)
# num4.discard(96)
# print(num4)


# Sorting the set
print(sorted(num3))

# Remember:- Sets are not in ordered form and lists are in ordered form so even by converting a set into a list and then perform reversing on that list using reverse method and then again converting that reversed list back into  set and print that set does not guarantee that we will get back a ordered set..

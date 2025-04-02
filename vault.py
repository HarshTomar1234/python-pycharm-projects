# Operator Overloading

# Operator Overloading is a powerful feature in Python that allows us to define the behavior of an operator for a user-defined class. 
# This feature is widely used in Python classes to define the behavior of the built-in operators in Python.

# For example, we can define the behavior of the + operator for a user-defined class by defining a special method called __add__().

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)

#     def __mul__(self, scalar):
#         return Vector(self.x * scalar, self.y * scalar)

#     def __truediv__(self, scalar):
#         return Vector(self.x / scalar, self.y / scalar)

#     def __str__(self):
#         return f"Vector({self.x}, {self.y})"

# # Example usage
# v1 = Vector(2, 3)
# v2 = Vector(4, 5)

# print(v1 + v2)  # Output: Vector(6, 8)
# print(v1 - v2)  # Output: Vector(-2, -2)
# print(v1 * 3)   # Output: Vector(6, 9)
# print(v1 / 2)   # Output: Vector(1.0, 1.5)




class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts



    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"   

    def __add__(self, other):  # This is an example of operator overloading
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts) 


potter = Vault(7, 21, 42)
print(potter)


weasley = Vault(23, 107, 121)
print(weasley)

# galleons = potter.galleons + weasley.galleons
# sickles = potter.sickles + weasley.sickles
# knuts = potter.knuts + weasley.knuts

total = potter + weasley
print(total)


import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]


    @classmethod # class method is used to define a method that is bound to the class rather than the object of the class. It takes cls as the first parameter
    def sort(cls, name):
        print(name, "is in",  random.choice(cls.houses))


# classmethod is used to define a method that is bound to the class rather than the object of the class. It takes cls as the first parameter.
# classmethod can be called by both class and object

# why we need to use @classmethod decorator?
# example: if we have a class and we want to create a method that should be called on the class rather than on the instance of the class then we use classmethod.
    # code: 
        # class MathOperations:
        #     @classmethod
        #     def add(cls, a, b):
        #         return a + b

        # # Calling the class method without creating an instance of the class
        # result = MathOperations.add(5, 3)
        # print("The sum is:", result)


Hat.sort("Harry")



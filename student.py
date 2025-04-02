# OOP

# def main():
#     student= get_student()
#     # if student[0] == "Padma":
#     #     student[1] = "Ravenclaw"   # This will not work as tuple is immutable (cannot be changed)

#     if student["name"] == "Padma":
#         student["house"] = "Ravenclaw"  # This will work as dictionary is mutable (can be changed)
#     print(f"Hello, {student['name']} from {student['house']}!")

# def get_student():
#     # name = input("Name: ")
#     # house = input("House: ")
#     # return (name, house)  or name , house  # Basically returning a tuple
  
#     student = {"name": input("Name:"), "house": input("House:")}
#     return student
    



# if __name__ == "__main__":
#     main()


##################################################

# Classes

class Student():
    def __init__(self, name, house): # here __init__ is a constructor and self is a reference to the object itself
        self.name = name  # here name and house are instance variables or attributes
        self.house = house
        # self.patronus = patronus

    def __str__(self): # This is a special method that gets called when we try to convert an object to a string
        return f"{self.name} from {self.house}"
     
    
    @classmethod  
    def get(cls):
        name = input("Name: ")
        house = input("House: ")    
        return cls(name, house)  # cls is used to refer to the class itself
    

    # @property
    # def name(self):
    #     return self._name   
    
    # @name.setter
    # def name(self, name):
    #     if not name:
    #         raise ValueError("Name is required")
    #     self._name = name
    
    # # Getter and Setter methods
    # # Getter and Setter methods are used to get and set the values of the attributes of a class respectively.
    # @property   # property decorator is used to define a getter method. It basically allows us to access the method as an attribute
    # def house(self):
    #     return self._house  # _house is used because if  instance variables and functiom names are same then it is a convention to use _ before the variable name
    
    # @house.setter
    # def house(self, house):
    #     if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
    #         raise ValueError("House is not valid")
    #     self._house = house  



    # def charm(self):
    #     match self.patronus:
    #         case "Stag" :
    #             return "🦌"  
    #         case "Otter":
    #             return "🦦"
    #         case "Eagle":
    #             return "🦅"
    #         case "Jack Russell Terrier":
    #             return "🐶"
    #         case _:
    #             return "🪄"
            
            
    
        

# Constructor is a special method that gets called when we create a new object of a class. it is used to initialize the object's attributes
# __init__ method is a constructor in python used to initialize the object's attributes
# self keyword is used to refer to the object itself

# Properties of a class is called attributes that are used to store data in a class and methods are used to perform operations on the data stored in the attributes...Properties are generally used to be more defensive and to prevent the data from being accessed directly from outside the class


'''
The difference between a function and a method is that a method is associated with an object and a function is not.

The difference between a class and an object is that a class is a blueprint for creating objects and an object is an instance of a class.

The difference between a class and a module is that a class is a blueprint for creating objects and a module is a file that contains code.

The difference between a class and a package is that a class is a blueprint for creating objects and a package is a directory that contains modules.

The difference between a class and a library is that a class is a blueprint for creating objects and a library is a collection of code that can be used by other programs.

The difference between __init__ method and __str__ method is that __init__ method is a constructor used to initialize the object's attributes and __str__ method is a special method that gets called when we try to convert an object to a string.

'''


def get_student():
    name= input("Name: ")
    house = input("House: ")
    # patronus = input("Patronus: ")
    student = Student(name, house) # Creating an object of class Student or instantiating the class
    return student




def main():
    # student = get_student()
    student = Student.get()
    # print(f"Hello, {student.name} from {student.house}!")
    print(student) # This will call the __str__ method of the class Student
    # print("Expecto Patronum! ", student.charm())


if __name__ == "__main__":
    main()    
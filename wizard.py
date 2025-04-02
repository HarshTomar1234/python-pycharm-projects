class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Name is required")
        self.name = name
        

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__()   # In order to call the __init__ method of the parent class we use super() method
        self.name = name
        self.house = house
    

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__()
        self.name = name
        self.subject = subject    


# Here above we are using Inheritance...
# Inheritance is a mechanism in which one class acquires the property of another class. For example, a child inherits the traits of his/her parents. With inheritance, we can reuse the fields and methods of the existing class.        


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defence against Dark arts")


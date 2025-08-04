#Class in python
class person:            #Defining a Class
    def __init__(self, name, age):  #__init__ = constructor and name/age are the attributes/variables
        self.name=name #self returns the current instance of the class and is used to access the attributes and methods of a class
        self.age=age
    
    def greet(self):  #method
        print(f"my name is {self.name} and my age is {self.age}")
    
    def is_adult(self):
        return self.age >=18

p1 = person("Sarat", 20) #Create an object

p1.greet()  #Call method
p1.is_adult()  

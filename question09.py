#A
class Customer(Person):
    # This line of code defines a new class named 'Customer', which inherits from another class named 'Person'.
    # This means that 'Customer' will inherit all attributes and methods from the 'Person' class.
#B
    def __init__(self, name):
        self.name = name  # This line of code is part of the constructor method (__init__) for a class.
        # It initializes a new object of the class with an attribute 'name'.
        # The value of 'name' is set to the name passed to the constructor when an object of this class is created.
#C
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello, my name is {self.name}!")
#D
class Customer(Person):
    def display_customer_info(self):
        print(f"Customer Name: {self.name}")  # An additional method specific to Customer

customer1 = Customer("Mark")

customer1.name = "Mark"

customer1.greet()

customer1.display_customer_info()
# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
  
  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'
  
  def has_birthday(self):
    self.age += 1

# Customer class
class Customer(User):
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0
  
  def set_balance(self, balance):
    self.balance = balance
  
  def greeting(self):
      return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'
  
# Init user object
shehryar = User('Shehryar Assad', 'xshehryar@gmail.com', 18)

# Edit property
shehryar.age = 19

print(shehryar.age)

# Call method
print(shehryar.greeting())

shehryar.has_birthday()

print(shehryar.age)

# Init customer
john = Customer('John Doe', 'john@gmail.com', 40)

john.set_balance(500)

print(john.balance)
print(john.greeting())


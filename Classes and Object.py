#!/usr/bin/env python
# coding: utf-8
Python is the object oriented programming Language.
It implies that almost everything in python is object, with its properties and methodsA CLASSS is a object contructor or blueprint for creating object

"class" keyword is use to create the class


# In[2]:
class number:
    x = 7
    
print(number.x)

1. __init__() function:
It is in-build function, which is always executed when the class is being initiated


# In[5]:
class name :
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
person = name('Alen', 'Walker')
print(person.first_name, person.last_name)

2. __str__() function:
The __str__() functio`n controls what should be returned when the class object is represented as a string.

    
# In[9]:
class name :
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def __str__(self):
        return f"First name is {self.first_name} and last name is {self.last_name}."
    
person = name('Alen', 'Walker')
print(person)


# ## Object Method
METHODS are functions that belong to the class and OBJECT is the variables used in the class.


# In[13]:
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.color = "Black"

    def get_description(self):
        """Return a formatted descriptive name for the car."""
        long_name = f"{self.year} {self.make} {self.model} having {self.color} color"
        return long_name.title()

    def service(self):
        """Simulate servicing the car."""
        print(f"{self.make} {self.model} has been serviced.")

# Creating an instance of the Car class
my_car = Car('audi', 'a4', 2020)
print(my_car.get_description())
my_car.service()

get_description, service are the methods of class "Car".
# ## Self Parameter
SELF parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
"Self" is just a variable name, we can give any variable name.


# In[15]:
class HOME:
    def __init__ (person, Name, Children, Car):
        person.Name = Name
        person.Children = Children
        person.Car = Car
silicon_valley = HOME("Tommy Sein",2,1)
silicon_valley.Car

Here "person" is used as the self parameter.

    
# ## Modify Object Properties
# In[16]:
class HOME:
    def __init__ (person, Name, Children, Car):
        person.Name = Name
        person.Children = Children
        person.Car = Car
silicon_valley = HOME("Tommy Sein",2,1)
silicon_valley.Car = 4


# In[17]:
silicon_valley.Car

Using assigning operator, Objects can be change.

    
# ## Delete Object Properties
Object property and object can be removed by using "del" 


# In[33]:
class HOME:
    def __init__ (person, name, children, car):
        person.name = name
        person.children = children
        person.car = car
silicon_valley = HOME("Tommy Sein",2,1)


# In[26]:
print(silicon_valley.name, silicon_valley.children, silicon_valley.car)


# In[27]:
del silicon_valley.children


# In[28]:
print(silicon_valley.name, silicon_valley.children, silicon_valley.car)

"silicon_valley.children" object property was deleted from the class silicon_valley, compiler doesn't found any object property named "children" and return the error.


# In[29]:
## Deleting object

# In[34]:
silicon_valley


# In[35]:
del silicon_valley

"silicon_valley" object can be deleted using del.


# In[36]:
silicon_valley

"silicon_valley" object was deleted, compiler throw error because it didn't find any object named "silicon_valley".


# ## PASS Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error."if we create class without anything and we want to work on something else."


# In[38]:
# Not using "PASS" statement

class desktop:

# In[39]:
# Using 'PASS' statement

class Nothing:
    pass


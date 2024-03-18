#!/usr/bin/env python
# coding: utf-8

# ## INHERITANCE
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
# In[4]:


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass

x = Student("Dwayne", "Johnson")
x.printname()

There are two classes named as "Person" and "Student". 
"Person" class has "printname" as object,
"__init__" contains parameters of class "Person"

"Student" class is empty class which inherit the property of the class "Person""Person" class is parent class.
"Student" class is child class of "Person" (parent) class.
# In[5]:


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

x = Student("Dwayne", "Johnson")
x.printname()

In this above example code,
"Student" class has its own "__init__",
that means "Student" class no more inherit the property of "__init__" parameter of "Person" class.
# #### To overcome with this problem
Rewriting the "__init__" function in child class mentioning the parent class
# In[11]:


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self,fname, lname)

x = Student("Qwin","Zenn")
x.printname()

Even after adding "__init__" function in child class,
if we mention "__init__" function of parent class,
child class "Student" will inherit the property of parent class "Person".
# ## SUPER() FUNCTION
Python has a super() function that will make the child class inherit all the methods and properties from its parent
# In[12]:


class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def info(self):
        return f"Subject: {self.name}, Teacher: {self.teacher}"

class OptionalSubject(Subject):
    def __init__(self, name, teacher, topic):
        super().__init__(name, teacher)
        self.topic = topic

    def info(self):
        parent_info = super().info()
        return f"{parent_info}, Topic: {self.topic}"

# Creating instances of Subject and SpecialSubject
maths = Subject("Mathematics", "Mr. Smith")
Deep_learning = OptionalSubject("Deep_learning", "Ms. Johnson", "Neuron Network")

# Calling the info method for each subject
print(maths.info())
print(Deep_learning.info())


# ## Add properties in child class

# In[16]:


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, graduationyear):
        super().__init__(fname, lname)
        self.graduationyear = graduationyear

x = Student("Mike", "Olsen", 2025)
print(x.graduationyear)


# In[ ]:





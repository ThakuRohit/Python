#!/usr/bin/env python
# coding: utf-8

# ## Errors are the problems in a program due to which the program will stop the execution. 
# ## On the other hand, exceptions are raised when some internal events occur which changes the normal flow of the program. 

# #### Two types of Error occurs in python. 
# #### Syntax errors : When the proper syntax of the language is not followed then a syntax error is thrown.
# #### Logical errors (Exceptions) : When in the runtime an error that occurs after passing the syntax test is called exception or logical type.

# ## Errors can be handled using try | except | finally.

# # 1. Try
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
These errors can be handled using "try".
# In[2]:


try:
    print(x)
except:
    print("Error")

Since the try block raises an error, the except block will be executed.
# In[3]:


# Without the try block, the program will crash and raise an error:
    
print(x)  


# In[18]:


# if there are multiple exceptions


# In[17]:


try:
    print(2+None)
except NameError:
    print("Variable is not defined")
except:
    print("Something else went wrong")


# # 2. else
You can use the else keyword to define a block of code to be executed if no errors were raised:
# In[22]:


try:
    print("Hello")
except:
    print("Name Error")
else:
    print("Nothing went wrong")


# In[20]:


#The try block does not raise any errors, so the else block is executed


# # 3. Finally
The finally block, will be executed regardless if the try block raises an error or not.
It executes atleast one time.
# In[21]:


try:
    print(x)
except:
    print("Error")
finally:
    print("The 'try except' is finished")


# In[26]:


import pandas as pd

try:
    try:
        df = pd.read_csv("file.csv")
    except:
        print("Error in reading the file")
    finally:
        df.close()
except:
    print("Something went wrong")

The program can continue, without leaving the file object open.
# # 4. Raise an exception
As a Python developer we can choose to throw an exception if a condition occurs.
To throw (or raise) an exception, use the raise keyword.
# In[29]:


x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

Note:
    The raise keyword is used to raise an exception.
    We can define what kind of error to raise, and the text to print to the user.
# In[35]:


x = 4

if not type(x) is str:
    raise TypeError("Only character are allowed")


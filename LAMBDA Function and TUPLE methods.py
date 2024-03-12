#!/usr/bin/env python
# coding: utf-8

# ## LAMBDA Function

# A lambda function is a small anonymous function.
# 
# A lambda function can take any number of arguments, but can only have one expression.

# In[1]:


x = lambda x, y : x**y
x(2,3)


# In[2]:


y = lambda x, y, z : x+y+z
y(8,9,10)


# In[7]:


z = lambda x : x*2


# In[8]:


z(3)


# In[11]:


p = lambda x,y : x*y + y*x


# In[12]:


p(2,3)


# In[14]:


def power(n):
    return lambda a : a**n

square = power(2)
print(square(4))


# In[20]:


def power(n):
    return lambda a : a**n

square = power(2)
cube = power(3)
print('square of 4 : ', square(4))
print('cube of 4 : ', cube(4))


# ## Tuples Methods

# In[64]:


(1,2,3,4,1).index(1)


# In[60]:


def indexs(set,value):
    for i in range(len(set)):
        if set[i] == value:
            return i
    return "Value not in set"


# In[62]:


indexs((1,2,3,4,1),1)


# In[67]:


(1,2,3,4,5,1,7,9,1,10,1).count(11)


# In[66]:


def countse(set,value):
    c = 0
    for i in range(len(set)):
        if set[i] == value:
            c+=1
    return c


# In[69]:


countse((1,2,3,4,5,1,7,9,1,10,1),0)


# In[ ]:





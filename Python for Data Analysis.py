#!/usr/bin/env python
# coding: utf-8

# In[4]:


# generate random number using numpy


import numpy as np

data = [np.random.standard_normal() for i in range (7)]

data


# In[6]:


# print statement

print('hello world!')


# In[7]:


get_ipython().run_line_magic('pwd', '')
path ='ch02/usagov_bitly_data2012-03-16-1331923249.txt'


# In[10]:


open(path).readline()
import json
path= 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]

records[0]
records[0]['tz']
print(records[0]['tz'])


# # Tab Completion

# In[15]:


an_apple = 27

an_example = 42


an_example


# In[21]:


# type "b" and tab will give you all built in funtion for list,
#append(), #count(), insert(), reverse(), clear(), copy(), extend(), index()
# pop(), remove(), sort()

b=[1,2,3]
    b.


# In[22]:


import datetime


# In[ ]:


datetime.


# # Variable and Argument
# 
# When assigning a variable(or name) in python, you are creating a reference to the object
# 
# 
# 

# In[24]:


a=[1,2,3] # e.g of variable and argument


# In[26]:


b=a

b
a


# In[29]:


b.append(4)
a


# # List is mutalable

# In[30]:


# e.g of appended list

fruit_basket = ['banana','apple','grape','organe','kiwi']

fruit_basket


# In[31]:


fruit_basket.append('manago')


# In[32]:


fruit_basket


# # ##Dynamic reference, strong types
# *variable in python have no in herent type associate with them; a variable can refer to a different tupe of pbject simple by doing an assignment,
# 
# 

# In[39]:


a=5
print (type(a))

a = 'foo'
print(type(a))


# In[37]:


a ="foo"
type(a)


# In[40]:


# isinstance can accept a tuple of types

a=5

isinstance(a, int)


# In[42]:


a=5; b=4.5

isinstance(b,(int,float))


# # Attribute and methods
# - object in pyhton have both attribute and methods. Both of them are accesed via the syntax obj.attribute_name.

# In[44]:


a='foo'

a.count # just type (a. and tab with return a list of all methods)  attribute and method can also be access by name via
getattr function:


# In[45]:


getattr(a,"split")


# #### in Python a module is file with .py extension contain  python code

# ## Imports

# In[48]:


PI=3.14159

def f(x):
    return x+2


# In[ ]:





# In[ ]:





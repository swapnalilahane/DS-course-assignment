#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# ### Q1 create numpy array starting from 2 till 50 and stepsize of 3 

# In[3]:


a  = np.arange(2,50,3)
a


# ### Question 2 

# In[4]:


l1 = []
l2 = []
n = int(input("enter no of elements in list:"))
for i in range(n):
    l1.append(int(input("enter elements:")))   
print("the list l1:",l1) 
for j in range(n):
    l2.append(int(input("enter elements:")))    
print("the list l2:",l2)
x = np.array(l1)
print("array1 :",x)
y = np.array(l2)
print("array2 :",y)
con = np.concatenate((x,y))
con.sort()
print(con)


# ### Q3 Write a code to find the dimensions of ndarray and its size

# In[6]:


a = np.array([[1,2,3,4],[4,5,6,7]])
a.ndim


# In[7]:


a.size


# ### Q4 convert 1D array to 2D array

# In[10]:


# 1D to 2D

b = np.array([1,2,3,4,5,6])
x = np.reshape(b,(2,3))
x


# ### Q5 stack vertically and horizontally

# In[4]:


a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[8,9]])
a
b
np.hstack((a,b))


# In[9]:


x = np.arange(1,10).reshape(3,3)
y = np.arange(11,20).reshape(3,3)
x


# In[10]:


y


# In[11]:


np.vstack((x,y))


# In[2]:


import pandas as pd


# ### Question 6

# In[3]:


df = pd.DataFrame(data = {
    'std_id' : [1,2,3,4,5,6],
    'name'   : ['karan ' , 'riya' , 'swapna' , 'kavya' , 'rohit' , 'priya'],
    'game_plays' : ['football' , 'carom' , 'chess', 'cricket' , 'badminton' , 'carom']
})
df


# In[4]:


print(df[['std_id' , 'game_plays']].nunique())


# In[ ]:





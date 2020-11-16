#!/usr/bin/env python
# coding: utf-8

# ### Question 1 

# In[1]:


import pandas as pd


# In[2]:


print(pd.__version__)


# In[3]:


pd.__version__


# ### Q2 series creation using numpy array

# In[4]:


import numpy as np


# In[5]:


a = np.array([1,2,3,4,9,8,5,6,7,0,10])
b = pd.Series(a)
print(b)


# In[10]:


x = np.array(['swapnali','priya','rushali','karan','rohan','nikita'])
y = pd.Series(x)
print(y)


# ### Question 3 

# In[14]:


obj = {
    'product': ['mouse','printer','monitor','computer','phone','charger'],
    'price' : [250,400,1200,30000,5000,300]
      }
df = pd.DataFrame(obj , columns = ['product','price'], index = ['obj1','obj2','obj3','obj4','obj5','obj6'])
df


# In[21]:


x = pd.Series([1,2,3,4,5], name = 'items' , index = pd.Index(['a','b','c','d','e'], name = 'items'))
x


# In[24]:


x.reset_index(name = 'values')


# ### Question 4  -  load mpg dataset

# In[25]:


import seaborn as sns
mpg=sns.load_dataset('mpg')
print(mpg)


# ### Question 5   -    which country origin cars are part of this dataset

# In[29]:


mpg=sns.load_dataset('mpg')
df = pd.DataFrame(mpg)
df.origin.unique()


# ### Q6  extract part of dataframe which contains cars belonging to usa

# In[37]:


df[df['origin'].str.contains("usa")]


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data = pd.read_csv("D://pubg.csv")
data


# In[9]:


data.dtypes


# In[10]:


data.describe()


# In[21]:


data.kills.mean()


# In[27]:


np.percentile(data.kills,99)


# In[31]:


data.kills.max()


# In[32]:


print(data.columns)


# In[39]:


sns.distplot(data.matchDuration);


# In[49]:


sns.distplot(data.walkDistance);


# In[63]:


fig,axs=plt.subplots(2,1)
sns.distplot(data.matchDuration,ax=axs[0]);
sns.distplot(data.walkDistance,ax=axs[1]);


# In[64]:


fig,axs=plt.subplots(1,2)
sns.distplot(data.matchDuration,ax=axs[0]);
sns.distplot(data.walkDistance,ax=axs[1]);


# In[ ]:


sns.pairplot(data.head(500));


# In[ ]:


print("Unique value in matchType is :",pd.unique(data['matchType']))
print()
print("Count of unique value in matchType is :",len(pd.unique(data['matchType'])))


# In[ ]:





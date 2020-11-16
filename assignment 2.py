#!/usr/bin/env python
# coding: utf-8

# ### Question 1

# In[1]:


list = []
n = int(input("enter the size of list: "))
for i in range(1,n+1):
    x = int(input("enter the element:"))
    list.append(x)
even = [] 
for j in list:
    if (j % 2 == 0):
        even.append(j)
print("list: ",even)   


# ### Question 3

# In[13]:


d = dict()
n = int(input("input:"))
for i in range(1 , n):
    d[i] = i**2
print(d)    


# In[ ]:


x=0
y=0
n = int(input())

for i in range(n):
    direction = input().split(' ')  
    
    if direction[0].upper() == "UP":
        y += int(direction[1])
    elif direction[0].upper() == "RIGHT":
        x += int(direction[1])
    elif direction[0].upper() == "DOWN":
        y -= int(direction[1])
    elif direction[0].upper() == "LEFT":
        x -= int(direction[1])
    else:
        print("Invalid Input")    
pos = float((x**2+y**2)**0.5)
print(round(pos))


# In[ ]:





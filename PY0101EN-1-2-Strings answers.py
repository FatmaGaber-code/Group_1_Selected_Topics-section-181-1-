#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Assign string to variable
name = "Michael Jackson"
name


# In[4]:


# Print the first element in the string
print(name[0])


# In[5]:


# Print the element on index 6 in the string
print(name[6])


# In[6]:


# Print the last element in the string
print(name[-1])


# In[7]:


# Take the slice on variable name with only index 0 to index 3
name[0:4]


# In[8]:


# Get every second element. The elments on index 1, 3, 5 ...
name[::2]


# In[9]:


# Get every second element in the range from index 0 to index 4
name[0:5:2]


# In[10]:


# Concatenate two strings
statement = name + "is the best"
statement


# In[11]:


# Print the string for 3 times
3 * "Michael Jackson"


# In[12]:


# New line escape sequence
print(" Michael Jackson \n is the best" )


# In[13]:


# Convert all the characters in string to upper case
a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)


# In[18]:


# Find the substring in the string. Only the index of the first elment of substring in string
name = "Michael Jackson"
name.find('el')


# In[19]:


# Find the substring in the string.
name.find('Jack')


# In[20]:


# If cannot find the substring in the string
name.find('Jasdfasdasdf')


# In[23]:


#What is the value of the variable a after the following code is executed?
# Write your code below and press Shift+Enter to execute
a = "1"
a


# In[24]:


# Write your code below and press Shift+Enter to execute
b = "2"
b


# In[25]:


# Write your code below and press Shift+Enter to execute
c = a + b
c


# In[26]:


# Write your code below and press Shift+Enter to execute
d = "ABCDEFG"
d


# In[27]:


# Write your code below and press Shift+Enter to execute
g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"
g


# In[28]:


g = "Mary"
c= g.replace('Mary', 'Bob')
c


# In[ ]:





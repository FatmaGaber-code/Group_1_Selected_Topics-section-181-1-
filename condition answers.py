#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Condition Equal
a = 5
a == 6


# In[2]:


# Greater than Sign
i = 6
i > 5


# In[3]:


# Greater than Sign
i = 2
i > 5


# In[4]:


# Inequality Sign
i = 2
i != 6


# In[5]:


# Inequality Sign
i = 6
i != 6


# In[6]:


# Use Equality sign to compare the strings
"ACDC" == "Michael Jackson"


# In[7]:


# Use Inequality sign to compare the strings
"ACDC" != "Michael Jackson"


# In[8]:


# Compare characters
'B' > 'A'


# In[9]:


# Compare characters
'BA' > 'AB'


# In[24]:


# If statement example
age = 19
#age = 18
#expression that can be true or false
if age > 18:
#within an indent, we have the expression that is run if the condition is true
 print("you can enter" )
#The statements after the if statement will run regardless if the condition is true or false
print("move on")


# In[27]:


# Else statement example
age = 8
# age = 19
if age > 18:
 print("you can enter" )
else:
 print("go see Meat Loaf" )
print("move on")


# In[28]:


# Elif statment example
age = 18
if age > 18:
 print("you can enter" )
elif age == 18:
 print("go see Pink Floyd")
else:
 print("go see Meat Loaf" )
print("move on")


# In[29]:


# Condition statement example
album_year = 1983
#album_year = 1970
if album_year > 1980:
 print("Album year is greater than 1980")
else:
 print("less than 1980")
print('do something..')


# In[30]:


# Condition statement example
album_year = 1991
if(album_year > 1979) and (album_year < 1990):
 print ("Album year was in between 1980 and 1989")
print("")
print("Do Stuff..")


# In[33]:


# Condition statement example
album_year = 1990
if(album_year < 1980) or (album_year > 1989):
 print ("Album was not made in the 1980's")
else:
 print("The Album was made in the 1980's ")


# In[34]:


rating = 8.5
if rating > 8:
    print ("This album is Amazing!")


# In[36]:


rating = 7
if rating > 8:
    print ("this album is amazing")
else:
    print ("this album is ok")


# In[37]:


album_year = 1979

if album_year < 1980 or album_year == 1991 or album_year == 1993:
    print ("this album came out already")


# In[ ]:





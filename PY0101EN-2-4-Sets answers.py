#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Convert list to set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)
album_set


# In[2]:


# Convert list to set
music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock",
"soul", \
"progressive rock", "soft rock", "R&B", "disco"
])
music_genres


# In[4]:


# Add element to set
A.add("NSYNC")
A


# In[5]:


# Try to add duplicate element to the set
A.add("NSYNC")
A


# In[6]:


# Remove the element from set
A.remove("NSYNC")
A


# In[7]:


# Verify if the element is in the set
"AC/DC" in A


# In[11]:


# Sample Sets
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set1, album_set2


# In[12]:


# Find the intersections
intersection = album_set1 & album_set2
intersection


# In[13]:


# Find the difference in set1 but not set2
album_set1.difference(album_set2)


# In[15]:


# Use intersection method to find the intersection of album_list1 and album_list2
album_set1.intersection(album_set2)


# In[16]:


# Find the union of two sets
album_set1.union(album_set2)


# In[17]:


# Check if superset
set(album_set1).issuperset(album_set2)


# In[18]:


# Check if subset
set(album_set2).issubset(album_set1)


# In[21]:


list = ['rap', 'house', 'electronic music', 'rap']
set(list)


# In[ ]:





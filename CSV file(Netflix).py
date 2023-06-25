#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data= pd.read_csv("8. Netflix Dataset.csv")


# In[2]:


data


# In[3]:


data.head(2)


# In[4]:


data.head(5)


# In[5]:


data.tail(2)


# In[6]:


data.shape


# In[7]:


data.size


# In[8]:


data.columns


# In[9]:


data.dtypes


# In[10]:


data.info()


# In[11]:


data.shape


# In[12]:


data.duplicated()


# In[13]:


data[data.duplicated()]


# In[14]:


data.drop_duplicates()


# In[16]:


data.drop_duplicates(inplace=True)


# In[17]:


data[data.duplicated()]


# In[19]:


data.head(1)


# In[20]:


data.isnull()


# In[21]:


data.isnull().sum()


# In[ ]:


import seaborn as sns
sns.heatmap(data.isnull())


# In[23]:


data.head(1)


# In[24]:


data["Title"]


# In[25]:


data["Title"].isin(['House of Cards'])


# In[27]:


data[data["Title"].isin(['House of Cards'])]


# In[28]:


data[data["Title"].str.contains('House of Cards')]


# # in which year highest no. of Tv shows and movies were released? show with bar graph
# 

# In[29]:


data.head(1)


# In[41]:


data['Date_N']=pd.to_datetime(data['Release_Date'])


# In[42]:


data.dtypes


# In[43]:


data['Date_N'].dt.year.value_counts()


# In[45]:


data['Date_N'].dt.year.value_counts().plot(kind='bar')


# # show all the movies that were released in year 2020

# In[46]:


data.head(1)


# In[47]:


data.head(5)


# In[48]:


data['Category']


# In[49]:





# In[51]:


data['year']=data['Date_N'].dt.year


# In[52]:


data[(data['Category']=='Movie')&(data['year']==2020)]


# # show only the titles of all tv shows that were released in india only
# 

# In[53]:


data.head(5)


# In[54]:


data[(data['Category']=='TV Show')& (data['Country']=='India')]


# In[55]:


data[(data['Category']=='TV Show')& (data['Country']=='India')]['Title']


# # show top 10 directors who gave the highest no. of tv shows and movies on netflix

# In[56]:


data.head(5)


# In[57]:


data['Director'].value_counts().head(10)


# # show all records where category is movie and type should be comedy or country is united kingdom

# In[58]:


data.head(5)


# In[59]:


data[(data['Category']=='Movie')&(data['Type']=='Comedies')|(data['Country']=='United Knigdom')]


# In[ ]:





# # how many movies/shows Tom Cruise was Casted

# In[60]:


data.head(1)


# In[61]:


data[data['Cast']=='Tom Cruise']


# # what are the different ratings defined by netflix

# In[62]:


data.Rating.nunique()


# In[63]:


data.Rating.unique()


# # how many movies got the 

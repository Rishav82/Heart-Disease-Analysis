#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("C:\/Users\/risha\/Downloads\heart (1).csv")


# In[3]:


data.head()


# In[4]:


data.tail()


# In[5]:


data.shape


# In[6]:


print("Number of Rows", data.shape[0])
print("Number of Columns", data.shape[1])


# In[7]:


data.info()


# In[9]:


data.isnull().sum()


# In[12]:


data_dup = data.duplicated().any()
print(data_dup)


# In[13]:


data = data.drop_duplicates()


# In[14]:


data.shape


# In[15]:


data.describe()


# In[21]:


plt.figure(figsize = (17, 6))
sns.heatmap(data.corr(), annot = True)


# In[22]:


data.columns


# In[23]:


data['target'].value_counts()


# In[24]:


sns.countplot(data['target'])


# In[26]:


data.columns


# In[27]:


data['sex'].value_counts()


# In[30]:


sns.countplot(data['sex'])
plt.xticks([0,1], ['Female', 'Male'])
plt.show()


# In[31]:


data.columns


# In[35]:


sns.countplot(x = 'sex', hue = 'target', data = data)
plt.xticks([1,0], ['Male', 'Female'])
plt.legend(labels = ['No-Disease', 'Disease'])
plt.show()


# In[38]:


sns.distplot(data['age'], bins = 20)
plt.show()


# In[42]:


sns.countplot(data['cp'])
plt.xticks([0,1,2,3], ['typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'])
plt.xticks(rotation = 75)
plt.show()


# In[43]:


data.columns


# In[46]:


sns.countplot(x = 'cp', hue = 'target', data = data)
plt.legend(labels = ['No-Disease', 'Disease'])
plt.show()


# In[47]:


sns.countplot(x = 'fbs', hue = 'target', data = data)
plt.legend(labels = ['No-Disease', 'Disease'])
plt.show()


# In[48]:


data.columns


# In[49]:


data['trestbps'].hist()


# In[52]:


g = sns.FacetGrid(data, hue = 'sex', aspect = 4)
g.map(sns.kdeplot, 'trestbps', shade = True)
plt.legend(labels = ['Male', 'Female'])


# In[53]:


data.columns


# In[54]:


data['chol'].hist()


# In[55]:


data.columns


# In[58]:


cate_val = []
cont_val = []
for column in data.columns:
    if data[column].nunique() <= 10:
        cate_val.append(column)
    else:
        cont_val.append(column)
    


# In[59]:


cate_val


# In[60]:


cont_val


# In[64]:


data.hist(cont_val, figsize = (15, 6))
plt.tight_layout()
plt.show()


# In[ ]:





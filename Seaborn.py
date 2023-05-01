#!/usr/bin/env python
# coding: utf-8

# # Distribution plots

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


tips = sns.load_dataset('tips')


# In[3]:


tips.head()


# In[4]:


sns.displot(tips.total_bill)
plt.show() 


# In[5]:


sns.displot(tips.total_bill, stat = 'density', kde = True)
plt.show()


# In[6]:


sns.displot(tips.total_bill, bins = 30)
plt.show()


# In[7]:


sns.jointplot(x = 'total_bill', y = 'tip', data = tips)
plt.show()


# In[8]:


sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'hex')
plt.show()


# In[9]:


sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'reg')
plt.show()


# In[10]:


sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'kde')
plt.show()


# In[11]:


sns.pairplot(tips)
plt.show()


# In[12]:


sns.pairplot(tips, hue = 'sex')
plt.show()


# In[13]:


sns.pairplot(tips, hue = 'sex', palette = 'coolwarm')
plt.show()


# In[14]:


sns.rugplot(tips.total_bill, color = 'blue')
plt.show()


# # Categorical plots

# In[15]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
tips = sns.load_dataset('tips')
tips.head()


# In[16]:


sns.barplot(x = 'sex', y = 'total_bill', data = tips)
plt.show()


# In[17]:


sns.barplot(x = 'sex', y = 'total_bill', data = tips, estimator = np.std)
plt.show()


# In[18]:


sns.countplot(x = 'sex', data = tips)


# In[19]:


sns.boxplot(x = 'day', y = 'total_bill', data = tips)
plt.show()


# In[20]:


sns.boxplot(x = 'day', y = 'total_bill', data = tips, hue = 'smoker')
plt.show()


# In[21]:


sns.violinplot(x = 'day', y = 'total_bill', data = tips)
plt.show()


# In[22]:


sns.violinplot(x = 'day', y = 'total_bill', data = tips, hue = 'sex')
plt.show()


# In[23]:


sns.violinplot(x='day', y='total_bill', data =tips, hue='sex', split=True)
plt.show()


# In[24]:


sns.stripplot(x='day', y='total_bill', data=tips)
plt.show()


# In[25]:


sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)
plt.show()


# In[26]:


sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex')
plt.show()


# In[27]:


sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex')
plt.show()


# In[28]:


sns.swarmplot(x='day', y='total_bill', data=tips, color='purple')
plt.show()


# In[29]:


sns.catplot(x='day', y='total_bill', data=tips)
plt.show()


# # Matrix plots

# In[30]:


import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
tips.head()


# In[31]:


flights.head()


# In[32]:


tips_corr = tips.corr(numeric_only=[True,False])


# In[33]:


tips_corr


# In[34]:


sns.heatmap(tips_corr)
plt.show()


# In[35]:


sns.heatmap(tips_corr, annot=True)
plt.show()


# In[36]:


sns.heatmap(tips_corr, annot=True, cmap='coolwarm')
plt.show()


# In[37]:


flights


# In[38]:


flights.pivot_table(index='month', columns='year', values='passengers')


# In[39]:


flight_pivot = flights.pivot_table(index='month', columns='year', values='passengers')


# In[40]:


sns.heatmap(flight_pivot)
plt.show()


# In[41]:


sns.heatmap(flight_pivot, cmap='magma')
plt.show()


# In[42]:


sns.heatmap(flight_pivot, cmap='magma', linecolor='white', linewidths=3)
plt.show()


# In[43]:


sns.clustermap(flight_pivot)
plt.show()


# In[44]:


sns.clustermap(flight_pivot, cmap='coolwarm')
plt.show()


# In[45]:


sns.clustermap(flight_pivot, cmap='coolwarm', standard_scale=1)
plt.show()


# # Grids

# In[46]:


import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset('iris')
iris.head()


# In[47]:


print(iris.species.unique())


# In[48]:


sns.PairGrid(iris)
plt.show()


# In[49]:


mapping = sns.PairGrid(iris)
mapping.map(plt.scatter)
plt.show()


# In[50]:


mapping = sns.PairGrid(iris)
mapping.map_diag(sns.violinplot)
mapping.map_upper(sns.kdeplot)
mapping.map_lower(plt.scatter)
plt.show()


# In[51]:


tips = sns.load_dataset('tips')
tips


# mapping = sns.FacetGrid(data=tips, col='time', row='smoker')

# In[52]:


mapping = sns.FacetGrid(data=tips, col='time', row='smoker')
mapping.map(sns.histplot,'total_bill')
plt.show()


# # Regression plots

# In[53]:


import seaborn as sns
tips = sns.load_dataset('tips')
tips.head()


# In[54]:


sns.lmplot(x='total_bill', y='tip', data=tips)
plt.show()


# In[55]:


sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex')
plt.show()


# In[56]:


sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='magma')
plt.show()


# In[57]:


sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='magma', markers=['s', 'v'])
plt.show()


# In[58]:


sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='magma', markers=['s', 'v'], scatter_kws={'s':70})
plt.show()


# In[59]:


sns.lmplot(x='total_bill', y='tip', data=tips, col='sex')
plt.show()


# In[60]:


sns.lmplot(x='total_bill', y='tip', data=tips, col='sex', row='time')
plt.show()


# In[61]:


sns.lmplot(x='total_bill', y='tip', data=tips, col='day', row='time', hue='sex')
plt.show()


# In[62]:


sns.lmplot(x='total_bill', y='tip', data=tips, col='day', hue='sex', aspect=0.6)
plt.show()


# In[71]:


sns.set_context('poster')
sns.lmplot(x='total_bill', y='tip', data=tips, col='day', hue='sex', aspect=0.6)
plt.show()


# # Style and Color

# In[63]:


sns.set_style('dark')
sns.countplot(x='sex', data=tips)
plt.show()


# In[64]:


sns.set_style('darkgrid')
sns.countplot(x='sex', data=tips)
plt.show()


# In[65]:


sns.set_style('white')
sns.countplot(x='sex', data=tips)
plt.show()


# In[66]:


sns.set_style('whitegrid')
sns.countplot(x='sex', data=tips)
plt.show()


# In[67]:


sns.set_style('ticks')
sns.countplot(x='sex', data=tips)
plt.show()


# In[68]:


sns.set_style('ticks')
sns.countplot(x='sex', data=tips)
sns.despine()


# In[69]:


sns.set_style('ticks')
sns.countplot(x='sex', data=tips)
sns.despine(left=True, bottom=True)


# In[70]:


plt.figure(figsize=(12,3))
sns.countplot(x='sex', data=tips)
plt.show()


# In[77]:


sns.set_context('talk')
plt.figure(figsize=(12,3))
sns.countplot(x='sex', data=tips)
plt.show()


# In[80]:


sns.set_context('talk',font_scale=2)
plt.figure(figsize=(12,3))
sns.countplot(x='sex', data=tips)
plt.show()


# In[88]:


sns.set_context('notebook')
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='hot')
plt.show()


# In[89]:


sns.set_context('notebook')
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='plasma')
plt.show()


# In[90]:


# Matplotlib colormap link - https://matplotlib.org/stable/tutorials/colors/colormaps.html


# In[ ]:





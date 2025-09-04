
#!/usr/bin/env python
# coding: utf-8

# ### Amazon Sales Report

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df=pd.read_csv('Amazon Sale Report.csv',encoding= 'unicode_escape')


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info()


# In[7]:


#drop unrelated/blank columns
df.drop(['New','PendingS'], axis=1, inplace=True)


# In[8]:


df.info()


# In[9]:


pd.isnull(df) 
# checking null value 


# In[10]:


pd.isnull(df).sum()
# sum will give total values of null values


# In[11]:


df.shape


# In[12]:


#drop null values
df.dropna(inplace=True)


# In[13]:


df.shape


# In[14]:


df.columns


# In[15]:


# change data type
df['ship-postal-code']=df['ship-postal-code'].astype('int')


# In[16]:


#checking whether the  data type change or not
df['ship-postal-code'].dtype


# In[17]:


df['Date']=pd.to_datetime (df['Date'])


# In[18]:


df.columns


# In[19]:


#rename Columns
df.rename(columns={'Qty':'Quantity'})


# In[20]:


#describe() method return description of the data in the DataFrame(i.e count,mean,std,min..etc)
df.describe()


# In[21]:


df.describe(include='object')


# In[22]:


#use describe() for specific columns
df[['Qty','Amount']].describe()


# # Exploratory Data Analysis
# 

# In[23]:


df.columns


# ### size

# In[24]:


ax=sns.countplot(x='Size' ,data=df)


# In[25]:


ax=sns.countplot(x='Size' ,data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# #### Note: From above Graph you can see that most of the people buys M-Size 

# # Group By
# #### The groupby() function in pandas is used to group data based on one or more columns in a DataFrame

# In[26]:


df.groupby(['Size'], as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)


# In[27]:


S_Qty=df.groupby(['Size'], as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)

sns.barplot(x='Size',y='Qty', data=S_Qty)


# ##### Note: From above Graph you can see that most of the Qty buys M-Size in the sales 

# ### Courier Status 

# In[28]:


sns.countplot(data=df, x='Courier Status',hue= 'Status')


# In[31]:


plt.figure(figsize=(12,7))

ax=sns.countplot(data=df, x='Courier Status',hue= 'Status')

plt.show()


# ##### Note: From above Graph the majority of the orders are shipped through the courier.

# In[32]:


#histogram 
df['Size'].hist() 


# In[36]:


df['Category'] = df['Category'].astype(str)
column_data = df['Category']
plt.figure(figsize=(10, 5))
plt.hist(column_data, bins=30, edgecolor='Black')
plt.xticks(rotation=60)
plt.show()


# ##### Note: From above Graph you can see that most of the  buyers are T-shirt 

# In[37]:


# Checking B2B Data  by using pie chart 
B2B_Check = df['B2B'].value_counts()

#  Plot the pie chart
plt.pie(B2B_Check, labels=B2B_Check, autopct='%1.1f%%')
#plt.axis('equal')
plt.show()


# In[38]:


# Checking B2B Data  by using pie chart 
B2B_Check = df['B2B'].value_counts()

#  Plot the pie chart
plt.pie(B2B_Check, labels=B2B_Check.index, autopct='%1.1f%%')
#plt.axis('equal')
plt.show()


# ##### Note : From above chart  we can see that maximum i.e. 99.3% of buyers are retailers and 0.7% are B2B buyers

# In[39]:


#  Prepare data for pie chart
a1 = df['Fulfilment'].value_counts()

# Step 4: Plot the pie chart
fig, ax = plt.subplots()

ax.pie(a1, labels=a1.index, autopct='%1.1f%%', radius=0.7, wedgeprops=dict(width=0.6))
ax.set(aspect="equal")

plt.show()


# ##### Note: From above chart you can see that most of the  Fulfilment  are  amazon 

# In[40]:


# Prepare data for scatter plot
x_data = df['Category']  
y_data = df['Size'] 

# Plot the scatter plot
plt.scatter(x_data, y_data)
plt.xlabel('Category ')  
plt.ylabel('Size')  
plt.title('Scatter Plot') 
plt.show()


# In[41]:




# Plot count of cities by state
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of State')
plt.xticks(rotation=90)
plt.show()


# In[87]:


# top_10_States 
top_10_state = df['ship-state'].value_counts().head(10)
# Plot count of cities by state
plt.figure(figsize=(12, 6))
sns.countplot(data=df[df['ship-state'].isin(top_10_state.index)], x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of  State')
plt.xticks(rotation=45)
plt.show()


# #### Note: From above Graph you can see that most of the  buyers are Maharashtra state

# ### Conclusion

# #### The data analysis reveals that the business has a significant customer base in Maharashtra state, mainly serves retailers, fulfills orders through Amazon, experiences high demand for T-shirts, and sees M-Size as the preferred choice among buyers.

# In[ ]:




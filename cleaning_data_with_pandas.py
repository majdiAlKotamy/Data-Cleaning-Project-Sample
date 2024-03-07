#!/usr/bin/env python
# coding: utf-8

# In[16]:


#read excel file in pandas
import pandas as pd
df = pd.read_excel(r"C:\Users\vmsof\Downloads\bank_customers.xlsx")
df


# In[17]:


#set index
df = df.set_index('customer_id')
df


# In[18]:


# check for duplicate values 
duplicate_values = df.duplicated()
print(duplicate_values)


# In[19]:


# remove the dublicate rows data
df.drop_duplicates()


# In[20]:


#delete unnecessary column data
df = df.drop(columns = 'not_useful_column')
df


# In[24]:


#clean geneder column data
df['gender']= df['gender'].str.lstrip('/')
df['gender']= df['gender'].str.rstrip('/')
df['gender']= df['gender'].str.strip()
df['gender'] = df['gender'].str.replace('Female','F')
df['gender'] = df['gender'].str.replace('Male','M')
df


# In[25]:


#clean phone_number column data
df['phone_number'] = df['phone_number'].apply(lambda x : str(x))
df['phone_number'] = df['phone_number'].str.replace('[^a-zA-Z0-9]', '', regex=True)
df['phone_number'] = df['phone_number'].apply(lambda x : x[0:3] + '-' + x[3:6] + '-' + x[6:10])
df['phone_number'] = df['phone_number'].str.replace('nan--','')
df['phone_number'] = df['phone_number'].str.replace('Na--','')
df


# In[26]:


#clean address column ans spilt it
df[['street_address','state','zip_code']]= df['address'].str.split(',',  n=2 , expand=True)
df


# In[28]:


#remove Nan N/a
df=df.fillna('')
df = df.replace('NaT','')
df


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# 
# # Road Accidents

# Road safety continues to be a major developmental issue, a public health concern and a leading
# cause of death and injury across the world. At least one out of 10 people killed on roads across the world is
# from India, according to the World Health Organization. The cost of road accidents is borne not only by the
# victims and their family, but by the economy as a whole in terms of untimely deaths, injuries, disabilities
# and loss of potential income. It is indeed a matter of great concern that despite the continuing efforts of the
# Government in this regard and our commitments for halving fatalities we have not been able to register
# significant progress on this front.
# During the year 2021, a total number of 4,12,432 road accidents have been reported in the country,
# claiming 1,53,972 lives and causing injuries to 3,84,448 persons. Unfortunately, the worst affected age
# group in Road accidents is 18-45 years, which accounts for about 67 percent of total accidental deaths.

# In[62]:


import pandas as pd 
import numpy as np
import seaborn as sns #its a visualiztion tools (library)
import matplotlib.pyplot as plt #its a library
import os
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#here we are checking the current working directory
os.getcwd()


# In[3]:


#now we are changing the directory and want to read and see the csv file
os.chdir('C:\Desktop\Data Analyst Project\Road Accident')


# In[4]:


#current working directory
os.getcwd()


# ### import data 

# In[5]:


#reading the file from directry
df=pd.read_csv(r"C:\Desktop\Data Analyst Project\Road Accident\Road Accident Data.csv")


# ### we have successfully imported the dataset and now we can view by using descriibe method 

# In[6]:


df.describe


# ### To view all the columns data type, and those null values use info method

# In[7]:


df.info() # to view all the columns data types and check if there null values 


# ### now to see the total number of rows and columns use shape method

# In[8]:


df.shape #it show in the rows and columns format

here we can see the total rows and columns 
# In[9]:


#to see all the columns of present data frame
df.columns


# # Data Clean-up (Missing value Treatment)

# ### Drop all  the null values from the all columns

# In[10]:


#count the number of missing value or null values
df.isnull().sum()

as we can see there is null values in few columns ,here we used sum method to sum of the null values
# ### Now  drop All the null values from dataset  to make free from unusual data to database

# In[11]:


#remove all the null values by using dropna mothod
df.dropna(inplace=True)

#here we have successfully removed all the null values from the dataset
and the inpalce=True means it permanently removes the null values from columns
# In[12]:


#here recheck the null values
df.isnull().sum()


# now we can see that no null values are ,so now we can move move forward for the next process in data analysis

# In[13]:


#now recheck data,is it removed or not
df.shape


# now we can see that the number of rows had decreased

# # show table data

# In[15]:


df.head(5)


# # Data clean up correcting the data type

# # check all the variables  that need to be change 

# In[16]:


df.info()


#     From this information, we can see that , Accident_Index,Month,Time ,Area  are in numeric type but still some of the columns need to be change are Date , Year,casualities,Number Of Vehicles ,Speed limit 

# In[17]:


#here we are changing Date into integer type
df['Date']=df['Date'].astype('int')


# In[18]:


# here we are changing Year into integer type
df['Year']=df['Year'].astype('int')


# In[19]:


#here we are changing Casualities into type integer
df['Casualities']=df['Casualities'].astype('int')


# In[20]:


# here we are changing Number_of_vehicles  float type into integer type
df['Number_of_Vehicles'] =df['Number_of_Vehicles'].astype('int')


# In[21]:


# here we are changing Speed limit float type into integer type
df['Speed_limit']=df['Speed_limit'].astype('int')


# Here we successfully changed date,Year ,Casuaities,,Number_Of_Vehicles, and Speed linmit (float type) in to integer data type

# In[22]:


df.info()


# now we can see , we have converted identifies columns into integer  datatype

# In[23]:


df.head()


# In[24]:


df['Area'].value_counts()

here we can see the number of accident cases in urban area is more than as compared to Rural area
# # Perform Basic EDA

# ## Whats are the sum of casualities in term of  accident severity effect

# In[11]:


df.groupby(['Accident_Severity'])['Casualities'].sum().plot(kind='pie')
plt.show()

here we can see the number of slight cases are 351235,serious cases are 59298 and fatal cases are 7135 so now we can say most of the cases are slight and the total of fatal and serious cases very less as comapred to slight
# ## show the trend week days with the casualities how does it changes and affect.

# In[12]:


df.groupby(['Day_of_Week'])['Casualities'].sum()


# In[23]:


sns.jointplot(y='Day_of_Week',x='Casualities',data=df)
plt.show()


# here we can see the most number of cases are at friday and the least on os sunday it might be because ,most of the person prefer to live at home 

# ### make histogram to show the data for a particular interval of time like date, year,longitude,etc

# In[22]:


df.hist()
sns.set(rc={'figure.figsize':(10,9)})
plt.show()


# # Now Lets see how the casualities with Light Condition and Months.

# In[18]:


ax=sns.barplot(data=df,y='Month',x='Casualities',hue='Light_Conditions')
sns.set(rc={'figure.figsize':(5,68)})
for bars in ax.containers:
    ax.bar_label(bars)
    plt.xticks(rotation=80)
    plt.show()
  


# #  The Number of casualities  with police force

# In[24]:


df.groupby(['Police_Force'])['Casualities'].sum()


# In[25]:


df.groupby(['Police_Force'])['Casualities'].sum().plot(kind='line')
sns.set(rc={'figure.figsize':(8,4)})
plt.show()


#  here we used line plot to display ,and we can see that the number ofcasualities on  Metropolitan Police have highest  around 57 thousand

# # Months vs  Total number of  casualities 

# In[29]:


a=df.groupby('Month')['Casualities'].sum()
a


# In[30]:


am=df.groupby(['Month'],as_index=False)['Casualities'].sum().sort_values(by='Casualities',ascending=False)
sns.barplot(data=am,y='Month',x='Casualities',color='r')
sns.set(rc={'figure.figsize':(5,7)})
plt.show()


# here we can see that monthly casualities in range 12 thousands to 23 thousands and its decreasing with respect to time as per given data

# # transport namethat mostly get affected 

# In[31]:


ax=df.groupby('Vehicle_Type')['Casualities'].sum()
ax


# In[33]:


ax=df.groupby(['Vehicle_Type'],as_index=False)['Casualities'].sum().sort_values(by='Casualities',ascending=False)
sns.barplot(data=ax, y='Vehicle_Type', x='Casualities')
sns.set(rc={'figure.figsize':(4,6)})
plt.xticks(rotation=80)
plt.show()


# Here we can see that most number of accident happpen with cars its 35 thousands
# least number of cases  3 with horses and all other are varing from  3 to 15000

# # What will be the casualities in 2021 and 2022 and how does it changes with weather display?

#  plot a bar to display casualities  Yearly cases vs  weather condition year wise 

# In[38]:


cx=sns.countplot(data=df,x='Weather_Conditions',hue='Year')
sns.set(rc={'figure.figsize':(8,10)})
for bars in cx.containers:
    cx.bar_label(bars)
    plt.xticks(rotation=60)
   


# here we can see fine no high winds have hoghest number of cases and after this raining and hgh winds respectively

# # Make a pairplot with the columns of accident severity,speed limit,casualities ,number of  ans show how does they change with other columns

# In[ ]:


sns.pairplot(df,vars=['Accident_Severity','Speed_limit','Casualities','Number_of_Vehicles'])
sns.set(rc={'figure.figsize':(33,60)})
plt.xticks(rotation=80, textsize=7)
plt.show()


# # what is the total number of casualities as per the given area

# In[ ]:


a=df.groupby(['Area'])['Casualities'].sum()
a


# here we can see the casualities percentages on urban areas are more than that of rural area

# In[ ]:


df.columns #to view all the columns use df.columns


# # Name the  month have highest and lowest number of cases on urban and rural areas ?

# Month vs Area Bar Chart to display casualities of urban and rural area  monthwise

# In[42]:


ax=sns.countplot(data=df,y='Month',hue='Area')
sns.set(rc={'figure.figsize':(4,28)})
for bars in ax.containers:
    ax.bar_label(bars, label=24)
    plt.xticks()


# here we can see that the number of rural cases are lesser as compared to urban area , and in urban area highest cases on novwmbwe 2021 and lowest on december 2020 while on other side in rural areas the highest number of cases are on novembwe 2021 and least on December 2022

# ## On which day most number of cases occurs and least as well ?

# 
# Display the sum of  Casualities in week days 

# In[46]:


df.groupby(['Day_of_Week'])['Casualities'].sum()


# here we can see the highet number of cases onn friday and wednesday respectively

# Make a bar plot to dispaly the total casualities on week days  

# In[49]:


bx=df.groupby(['Day_of_Week'],as_index=False)['Casualities'].sum().sort_values(by='Casualities',ascending=False)
sns.barplot(data=bx,y='Day_of_Week',x='Casualities')

sns.set(rc={'figure.figsize':(9,12)})
plt.show()


# ###  Do casualities changes with Road type ,if it does then explain it?

# In[50]:


cv=df.groupby(['Road_Type'])['Casualities'].count()
cv


# here we can see the most number casualities on single carriageway 2.26lakh and dual carriageway ,Roundabout are around 45 thousand and 20 thousand respectively

# ### make chart a display the casualities on basis of road type ,how does the rate increases and decreases 

# In[51]:


ax=sns.countplot(data=df,x='Road_Type')
sns.set(rc={'figure.figsize':(9,4)})
for bars in ax.containers:
    ax.bar_label(bars)

one way road and slip road are 6 thousand and 3.1 thousand respectivery which is very much lesser as comapred to single carriageway
# # do the casualities changes with ,how much and how do ?

# make a line plot to display the casualities with the accident date

# In[52]:


df.groupby(['Accident Date'])['Casualities'].count().plot(kind='line')                                                                        
sns.set(rc={'figure.figsize':(8,11)})
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     


# In[53]:


df.columns


# In[54]:


ab=df.groupby(['Accident Date'])['Casualities'].sum()
ab


# # how many cases are on different junctions?

# In[55]:


b=df.groupby(['Junction_Detail'])['Casualities'].count()
b

here we can see that highest number of cases are within the range of 20 meter 
# In[56]:


ax=sns.countplot(data=df, x='Junction_Detail')
sns.set(rc={'figure.figsize':(8,6)})
plt.xticks(rotation=80)
for bars in ax.containers:
    ax.bar_label(bars)


# In[57]:


a=df.groupby(['Time'])['Casualities'].sum()
a


# #whats the total number vehicals accidents occurs monthwise ? 

# In[58]:


a=df.groupby(['Month'])['Number_of_Vehicles'].sum()
a


# In[59]:


ax=df.groupby(['Month'],as_index=False)['Number_of_Vehicles'].sum().sort_values(by='Number_of_Vehicles',ascending=False)
sns.barplot(data=ax,y='Month',x='Number_of_Vehicles')
sns.set(rc={'figure.figsize':(5,8)})


# we can esee here highest number of vehicles accident on november and least accident on december 2022

# # what is the number of casualities with different road conditions?

# In[60]:


df.groupby(['Road_Surface_Conditions'])['Number_of_Vehicles'].sum()


# In[61]:


zx=df.groupby(['Road_Surface_Conditions'],as_index=False)['Number_of_Vehicles'].sum().sort_values(by='Number_of_Vehicles',ascending=False)
sns.barplot(data=zx,x='Road_Surface_Conditions',y='Number_of_Vehicles')
sns.set(rc={'figure.figsize':(6,5)})


# here we can see that `most number of casualities are on dry road and after this on wet or damp ,froast or ice snow respectively

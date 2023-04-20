#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[150]:


car = pd.read_csv("cardata.csv")
car


# In[167]:


plt.hist(car.carbody)
plt.title('Usage of Carbody')
plt.xlabel("Carbody")
plt.ylabel("Usage")

plt.show()


# In[169]:


#car.drivewheel

plt.hist(car.drivewheel)

plt.xlabel("Drive Wheel")
plt.ylabel("Number of Cars")

plt.show()


# In[162]:


sns.scatterplot(data=car, x='carbody', y='compressionratio').set(title='Carbody vs. Compression Ratio')
plt.xlabel("Carbody")
plt.ylabel("Compression Ratio")
plt.show()


# In[161]:


sns.regplot(data=car, x='enginesize', y='compressionratio').set(title='Engine Size vs. Compression Ratio')
plt.xlabel("Engine Size")
plt.ylabel("Compression Ratio")
plt.show()


# In[163]:


sns.set(rc={"figure.figsize": (14,10)})
ax=sns.lineplot(x="CarName", y="price", data=car)
plt.xlabel("Car Name")
plt.ylabel("Price")

ax.tick_params(axis='x', rotation=90)


# In[48]:


sns.set(rc={'figure.figsize':(14,10)})
ax = sns.lineplot(x='CarName', y='price', hue = 'carbody', data = car)
ax.tick_params(axis='x', rotation=90)


# In[185]:


sns.set(rc={'figure.figsize':(14,10)})

sedan = car.loc[car["carbody"]== "sedan"].reset_index()

result = sns.lineplot(x='CarName', y='price', data = sedan)
result.tick_params(axis='x', rotation=90)


# In[184]:


sns.set(rc={'figure.figsize':(14,10)})

sedan = car.loc[car["carbody"]== "sedan"].reset_index()

result = sns.lineplot(x="CarName", y="price", data = sedan, hue="cylindernumber", style="aspiration", errorbar=None,  markers=True)
result.tick_params(axis="x", rotation=90)


# In[186]:


result = sns.boxplot(x="cylindernumber", y="price", data=car, color = 'green')
plt.xlabel("Cylinder Number")
plt.ylabel("Price")
plt.show()


# In[191]:


categories = ['carbody', 'aspiration','doornumber','drivewheel','enginelocation', 'fuelsystem']
for c in categories:
    result = sns.boxplot(x="cylindernumber", y="price", data=car, color = 'green')
    for container in ax.containers:
        result.bar_label(container)
    plt.xlabel(c)
    plt.ylabel("Price")
    plt.show()


# categories = ['carbody', 'aspiration','doornumber','drivewheel','enginelocation', 'fuelsystem']


# for c in categories:
    
#     ax = sns.barplot(x=c, y="price", hue = 'fueltype', data=raw_data, ci=False)
#     for container in ax.containers:
#         ax.bar_label(container)
#     plt.title(c)
#     plt.show()


# In[74]:


car[['carbody', 'price']].groupby('carbody', as_index = False).agg({'price':'mean'})


# In[182]:


result = sns.barplot(x="carbody", y="price", data=car, errorbar=("ci",False))
result.bar_label(result.containers[0])
plt.title("Boxplot Showing Average Price Per Carbody", size=18)
plt.show()


# In[183]:


resukt = sns.barplot(x="carbody", y="price", hue="fueltype", data=car, errorbar=("ci",False))
for container in ax.containers:
    result.bar_label(container)
plt.title("Boxplot Showing Average Price Per Fuel Types for Different Carbodies", size=18)
plt.show()


# In[105]:


categories = ['carbody', 'drivewheel','aspiration','doornumber','enginelocation', 'fuelsystem']

for c in categories:
    
    ax = sns.barplot(x=c, y="price", hue = 'fueltype', data=car, errorbar=('ci',False))
    for container in ax.containers:
        ax.bar_label(container)
    plt.title(c)
    plt.show()


# In[109]:


ax = sns.barplot(x="price", y="carbody", hue = 'fueltype', data=car, orient = 'h', errorbar=('ci',False))
for container in ax.containers:
    ax.bar_label(container)
    plt.title("Total Price By Carbody & FuelType")


# In[176]:


fueltype = car["fueltype"]

gas = car.loc[car["fueltype"]== "gas"].count()[0]
diesel = car.loc[car["fueltype"]== "diesel"].count()[0]

labels = ["Gas", "Diesel"]
colors = ["#eb4034", "#3492eb"]
explode = (0, 0.2)
plt.pie([gas, diesel], colors = colors,  labels=labels, explode=explode, pctdistance=0.5,autopct='%.2f %%')

plt.title ("Consumption of Gas vs Diesel")

plt.show()


# In[128]:


x = car['price'].values
sns.histplot(x, color = '#4287f5')

plt.xlabel("Prices")
plt.show()


# In[149]:


x = car['price'].values

sns.histplot(x, color = '#4287f5')

mean = car['price'].mean()

plt.axvline(mean, 0,1, color = 'orange')
plt.show()


# In[147]:


mean


# In[ ]:





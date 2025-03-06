#!/usr/bin/env python
# coding: utf-8

# In[32]:


# Install necessary libraries if not available
get_ipython().system('pip install numpy pandas matplotlib scipy')



# In[35]:


import pandas as pd
import matplotlib.pyplot as plt

# Historical revenue data for CMA CGM (in billion USD) - Actual Data
historical_revenues = {
    "2010": 10.2, "2011": 11.5, "2012": 12.0, "2013": 13.5, "2014": 14.8,
    "2015": 15.7, "2016": 16.0, "2017": 21.1, "2018": 34.0, "2019": 38.9,
    "2020": 55.5, "2021": 74.5, "2022": 62.3, "2023": 47.0, "2024": 55.5
}

# Convert historical data to DataFrame
df_revenue = pd.DataFrame(list(historical_revenues.items()), columns=["Year", "Revenue"])
df_revenue["Year"] = df_revenue["Year"].astype(int)
df_revenue["Revenue"] = df_revenue["Revenue"].astype(float)

# Plot historical revenue data
plt.figure(figsize=(10, 5))
plt.plot(df_revenue["Year"], df_revenue["Revenue"], marker='o', linestyle='-', color='blue', label="CMA CGM Revenue")

plt.xlabel("Year")
plt.ylabel("Revenue (Billion USD)")
plt.title("CMA CGM Historical Revenue (2010-2024)")
plt.legend()
plt.grid(True)
plt.show()

# Display the data
print(df_revenue)


# In[24]:


import pandas as pd
import matplotlib.pyplot as plt

# Historical revenue data for CMA CGM (in billion USD)
historical_revenues = {
    "2010": 10.2, "2011": 11.5, "2012": 12.0, "2013": 13.5, "2014": 14.8,
    "2015": 15.7, "2016": 16.0, "2017": 21.1, "2018": 34.0, "2019": 38.9,
    "2020": 55.5, "2021": 74.5, "2022": 62.3, "2023": 47.0, "2024": 55.5
}

# Convert to DataFrame
df_revenue = pd.DataFrame(list(historical_revenues.items()), columns=["Year", "Revenue"])
df_revenue["Year"] = df_revenue["Year"].astype(int)
df_revenue["Revenue"] = df_revenue["Revenue"].astype(float)

# Compute Year-over-Year Growth (%)
df_revenue["YoY Growth (%)"] = df_revenue["Revenue"].pct_change() * 100

# Plot Year-over-Year Growth
plt.figure(figsize=(10, 5))
plt.bar(df_revenue["Year"], df_revenue["YoY Growth (%)"], color='blue')
plt.axhline(y=0, color='black', linestyle="--", alpha=0.7)
plt.xlabel("Year")
plt.ylabel("YoY Growth (%)")
plt.title("CMA CGM Year-over-Year Revenue Growth (%)")
plt.show()


# In[ ]:





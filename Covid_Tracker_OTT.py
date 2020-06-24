#%% 
import wget
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import os

#%% Grab the official city of Ottawa COVID stats 
url = 'https://www.arcgis.com/sharing/rest/content/items/cf9abb0165b34220be8f26790576a5e7/data'
path = 'C://Users//Saptak/Downloads/CS_EXMPL.csv'

if os.path.exists('C://Users//Saptak/Downloads/CS_EXMPL.csv'):
  os.remove('C://Users//Saptak/Downloads/CS_EXMPL.csv')
  wget.download(url, path)
else:
  wget.download(url, path)

#%% Read in the data and process dates for easy graphing
cases = pd.read_csv('C://Users//Saptak/Downloads/CS_EXMPL.csv')
cases['Non-Inst Cumulative Cases'] = cases['Sporadic Cases'].cumsum() + cases['Community Cases'].cumsum()
cases.columns = ['Date', 'Sporadic Cases', 'Community Cases', 'Institutional Cases', 'Cumulative Cases', 'Cumulative Deaths', 'Non-Inst Cumulative Cases']
cases = cases[['Date', 'Sporadic Cases', 'Community Cases', 'Institutional Cases', 'Cumulative Cases', 'Non-Inst Cumulative Cases', 'Cumulative Deaths']]
cases['Date'] = pd.to_datetime(cases['Date']).dt.strftime('%B %d, %Y')

#%% Visualize curve data
x = pd.to_datetime(cases['Date'])
y1 = cases['Cumulative Cases']
y2 = cases['Non-Inst Cumulative Cases']

fig = plt.figure()
fig.set_size_inches(16,8)
ax = fig.add_subplot(1,1,1)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%B %d, %Y'))
fig.autofmt_xdate()
ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))

plt.scatter(x,y1)
plt.scatter(x,y2)
plt.xlim([min(x), max(x)])
plt.legend(['Cumulative Cases', 'Non-Inst Cumulative Cases'])
plt.title('Ottawa Cumulative COVID-19 Curve')
print('Last updated on', max(x))
fig.savefig('C://Users//Saptak/Downloads/COVID_CURVE.png', dpi=500)

# %%

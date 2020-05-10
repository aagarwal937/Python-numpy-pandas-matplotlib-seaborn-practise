import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import seaborn as sns

df = pd.read_csv('911.csv')

print(df.info())
print(df.head())

# What are the top 5 zipcodes for 911 calls?
print(df['zip'].value_counts().head())

# What are the top 5 townships (twp) for 911 calls?
print(df['twp'].value_counts().head())

# Take a look at the 'title' column, how many unique title codes are there?
print(df['title'].nunique())

# In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value.

print(df.head())

s = "EMS: BACK PAINS/INJURY"
new_s = s.split(':')[0].replace('', '')
print(new_s)

# df.apply(lambda row: row.zip + row.zip, axis=1)
print(df.apply(lambda x: x.title.split(':')[0].replace('', ''), axis=1))

df['Reason'] = df.apply(lambda x: x.title.split(':')[0].replace('', ''), axis=1)
print(df.head(10))

# What is the most common Reason for a 911 call based off of this new column?
print(df['Reason'].value_counts())

# using seaborn

# to create a countplot of 911 calls by Reason
sns.set_style('whitegrid')
sns.countplot(x='Reason', data=df)

# Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column?
print(type(df['timeStamp'][0]))

# Use pd.to_datetime to convert the column from strings to DateTime objects.
print(df.head())
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
print(type(df['timeStamp'][0]))
time = df['timeStamp'].iloc[0]
print(time.day)
print(time.year)
print(time.date())

print(time.hour)
print(time.month_name())
print(time.day_name())

# using seaborn

# to create a countplot of the Day of Week column with the hue based off of the Reason column.
sns.countplot(x='Day of Week', data=df, hue='Reason')

# Nowfor Month
df['Month No'] = df.apply(lambda x: x['timeStamp'].month, axis=1)
sns.countplot(x='Month No', data=df, hue='Reason')

# while using the countplot some moths were missing so in order to see all the months now we shall be using pandas

# creating a gropuby object called byMonth, where you group the DataFrame by the month column and use the count() method for aggregation. Use the head() method on this returned DataFrame.
print(df.head(1))
byMonth = df.groupby(['Month No'])[
    ['lat', 'lng', 'desc', 'zip', 'title', 'timeStamp', 'twp', 'addr', 'e', 'Reason', 'Hour', 'Day of Week']].count()
byMont = df.groupby('Month No')
print(data.groupby(['col1', 'col2'])['col3'].mean())

# creating a plot off of the dataframe indicating the count of calls per month.
byMonth['twp'].plot()

# creating a linear fit on the number of calls per month
byMonth = byMonth.reset_index()
print(byMonth)

sns.lmplot(x='Month No', y='twp', data=byMonth)

# creating heatmaps with seaborn

dayHour = df.groupby(by=['Day of Week', 'Hour']).count()['Reason'].unstack()
print(dayHour)

# plt.plot()
plt.show()

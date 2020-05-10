import pandas as pd
from pandas.io import data , wb
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

#inbuild pandas data is used

start = datetime.datetime(2013,1,1)
end = datetime.datetime(2017,1,1)
print(start.date())

#Symbols for companys

# Bank of America
BAC = data.DataReader("BAC", 'iex', start, end)

# CitiGroup
C = data.DataReader("C", 'iex', start, end)

# Goldman Sachs
GS = data.DataReader("GS", 'iex', start, end)

# JP Morgan
JPM = data.DataReader("JPM", 'iex', start, end)

# Morgan Stanley
MS = data.DataReader("MS", 'iex', start, end)

# Wells Fargo
WFC = data.DataReader("WFC", 'iex', start, end)

WFC.head()


#Creating a list of the ticker symbols (as strings) in alphabetical order

tickers = ["BAC ", "C ", "GS ", "JPM ", "MS ", "WFC "]


#Using pd.concat to concatenate the bank dataframes together to a single data frame called bank_stocks.

bank_stocks = pd.concat([BAC,C,GS,JPM,MS,WFC],axis=1,keys=tickers)
print(bank_stocks.head())

bank_stocks.columns.names = ['Bank Ticker','Stock Info']
print(bank_stocks.head())


# QUESTIONS

#What is the max Close price for each bank's stock throughout the time period?

bank_stocks.xs(key='close', axis=1, level='Stock Info').max()
#df.xs('one', level=1)

#Creating a new empty DataFrame called returns. This dataframe will contain the returns for each bank's stock.
returns = pd.DataFrame()
print(bank_stocks.head())


for tick in tickers:
    returns[tick + ' Return'] = bank_stocks[tick]['close'].pct_change()

returns.head()

#Creating a pairplot using seaborn of the returns dataframe

sns.pairplot(data=returns[1:]) # indexing 1st row since they are empty elements

#Using returns DataFrame, figure out on what dates each bank stock had the best and worst single day returns

print(returns.idxmin())

print(returns.idxmax())

print(returns.std())    # checking standard deviation as higher standard deviation leads to higher risks

returns.loc['2015-01-01':'2015-12-31'].std() #higher ones are Bank of America and Morgan Stanley

#Creating a distplot using seaborn of the 2015 returns for Morgan Stanley

ns.set_style("whitegrid")
sns.distplot(returns.ix['2015-01-01':'2015-12-31']['MS  Return'], bins=100, color='coolwarm')
plt.tight_layout()

#Creating a distplot using seaborn of the 2008 returns for CitiGroup

sns.set_style("whitegrid")
sns.distplot(returns.ix['2013-09-24':'2013-12-31']['C  Return'], bins=50, color='red')
plt.tight_layout()

#plt.plot()
plt.show()
from heapq import merge
import pandas as pd

listDf = pd.read_csv(r'C:\Users\chris\Desktop\etfs.csv')

pricesDf = pd.read_csv('etf_prices.txt', sep='\t', names=['ticker', 'frequency', 'close', 'high', 'low', 'open', 'date', 'volume'], parse_dates=['date'])
#indiceDf = pd.read_csv(r'C:\Users\chris\Desktop\indice_data.txt', sep='\t', names=['ticker', 'date', 'close'], parse_dates=['date'])

prices1 = pd.read_csv(r'C:\Users\chris\Desktop\pricesOneYearAgo.csv', parse_dates=['date'], dtype={'ticker': str, 'frequency':str, 'low': 'float64', 'open': 'float64', 'close': 'float64', 'high': 'float64', 'volume': 'float64'})
prices2 = pd.read_csv(r'C:\Users\chris\Desktop\pricesTwoYearsAgo.csv', parse_dates=['date'], dtype={'ticker': str, 'frequency':str, 'low': 'float64', 'open': 'float64', 'close': 'float64', 'high': 'float64', 'volume': 'float64'})
prices3 = pd.read_csv(r'C:\Users\chris\Desktop\pricesThreeYearsAgo.csv', parse_dates=['date'], dtype={'ticker': str, 'frequency':str, 'low': 'float64', 'open': 'float64', 'close': 'float64', 'high': 'float64', 'volume': 'float64'})
prices4 = pd.read_csv(r'C:\Users\chris\Desktop\pricesFourYearsAgo.csv', parse_dates=['date'], dtype={'ticker': str, 'frequency':str, 'low': 'float64', 'open': 'float64', 'close': 'float64', 'high': 'float64', 'volume': 'float64'})
prices5 = pd.read_csv(r'C:\Users\chris\Desktop\pricesFiveYearsAgo.csv', parse_dates=['date'], dtype={'ticker': str, 'frequency':str, 'low': 'float64', 'open': 'float64', 'close': 'float64', 'high': 'float64', 'volume': 'float64'})

#indice1 = indiceDf.loc[indiceDf['date'] > '2021-04-13']

df1 = pricesDf[['ticker', 'date', 'close']]

mergeDf = pd.concat([df1, prices1, prices2, prices3, prices4, prices5])
mergeDf = mergeDf[['ticker', 'date', 'close']]
mergeDf = mergeDf.drop_duplicates()
mergeDf = mergeDf.reset_index()
mergeDf = mergeDf.drop(columns=['index'])
mergeDf = mergeDf.loc[mergeDf.index != '195']

pivDf = pd.pivot_table(mergeDf, values='close', index='date', columns='ticker')
pctDf = pivDf.pct_change()

meanDf = pd.DataFrame()
for (name, data) in pctDf.iteritems():
    newData = data.dropna()
    d = {'series_id': [name], 'mean': [newData.mean()], 'std': [newData.std()]}
    newDf = pd.DataFrame(d)
    meanDf = meanDf.append(newDf)

meanDf['annual_return'] = ((meanDf['mean'] + 1) ** 252) -1
meanDf['annual_std'] = meanDf['std'] * (252 ** (1/2))
meanDf.to_csv(r'C:\Users\chris\Desktop\meanEtfValues.csv', index=False)


#meanDf.to_csv(r'C:\Users\chris\Desktop\etf_returns.csv',index=False)
# SUB_CLASS = 'Large Blend'

# subClassList = []
# for index, row in listDf.iterrows():
#     if (row['sub_class'] == SUB_CLASS):
#         subClassList.append(row['ticker'])

# for item in subClassList:
#     try:
#         df = pricesDf.loc[pricesDf.iloc[:,0] == item]
#         print(df)
#     except:
#         print(item)
#         pass
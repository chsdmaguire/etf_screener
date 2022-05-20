import pandas as pd

indiceDf = pd.read_csv(r'C:\Users\chris\Desktop\indice_data.txt', sep='\t', names=['ticker', 'date', 'close'], parse_dates=['date'])
pivDf = indiceDf.pivot(values='close', index='date', columns='ticker')
pivDf = pivDf.dropna()
pctDf = pivDf.pct_change()

meanDf = pd.DataFrame()
for (name, data) in pctDf.iteritems():
    d = {'series_id': [name], 'mean': [data.mean()], 'std': [data.std()]}
    newDf = pd.DataFrame(d)
    meanDf = meanDf.append(newDf)

meanDf['annual_return'] = ((meanDf['mean'] + 1) ** 252) -1
meanDf['annual_std'] = meanDf['std'] * (252 ** (1/2))
meanDf.to_csv(r'C:\Users\chris\Desktop\meanIndiceReturns.csv', index=False)
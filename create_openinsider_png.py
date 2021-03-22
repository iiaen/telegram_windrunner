#!/usr/bin/python3
import pandas as pd
import yfinance as yf
from makeimages import save_df_as_image


# Get html table
# url = 'http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=1&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&vl=10&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&isceo=1&iscfo=1&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=100&page=1'
url = 'http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=1&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&vl=10&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&isceo=1&iscfo=1&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=100&page=1'
df = pd.read_html(url)
df = df[11][1:] # might change in the future
# print(len(df))
df.columns = df.columns.str.replace(r"\xa0", " ")


# Clean up
df1 = df.drop(["X", "Trade Type", "Insider Name", "Qty", "Owned", '1d', '1w', '1m', '6m'], axis=1)
df1['Filing Date'] = df['Filing Date'].str[:10]
# df1['Filing\xa0Date'] = pd.to_datetime(df1['Filing\xa0Date']).dt.date
# df1['Sector'] = df1.apply(lambda x: (yf.Ticker(x.Ticker).info['sector']), axis=1)

# Add yahoo finance info
df1["Sector"] = ""
df1["BookValue"] = ""
df1["AvgVol10D"] = ""

for index, row in df1.iterrows():
    info = yf.Ticker(row.Ticker).info
    row["Sector"] = info['sector']
    row["BookValue"] = info['bookValue']
    row["AvgVol10D"] = info['averageDailyVolume10Day']

# Clean up columns
df1 = df1[['Filing Date', 'Trade Date', 'Ticker', 'Company Name', 'Sector', 'Title', 'Price', 
           'ΔOwn', 'Value', 'BookValue', 'AvgVol10D']]
df1.rename(columns = {'Value':'InsiderTradeVal'}, inplace = True) 


save_df_as_image(df1, "openinsider.png")
print('shish kebab')
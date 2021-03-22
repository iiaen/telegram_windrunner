#!/usr/bin/python3
import pandas as pd
import yfinance as yf
from makeimages import save_df_as_image
from personalstuff import portfolio

# Get yahoo finance info
portfolio_ls = portfolio #list of tickers
portfolio_df = pd.DataFrame(portfolio_ls, columns=["Ticker"])

portfolio_df["Sector"] = ""
portfolio_df["AvgVol10D"] = ""
portfolio_df["Volume"] = ""  #regularMarketVolume
portfolio_df["AvgVolume"] = ""  
portfolio_df["Avg50D"] = ""
portfolio_df["PreviousClose"] = ""
portfolio_df["DayHigh"] = ""
portfolio_df["DayLow"] = ""
portfolio_df["TrailingPE"] = ""

for index, row in portfolio_df.iterrows():
    info = ""
    try:
        info = yf.Ticker(row.Ticker).info
        if 'sector' in info:
            row["Sector"] = info['sector']
        if 'averageDailyVolume10Day' in info:
            row["AvgVol10D"] = info['averageDailyVolume10Day']
        if 'regularMarketVolume' in info:
            row["Volume"] = info['regularMarketVolume']
        if 'averageVolume' in info:
            row["AvgVolume"] = info['averageVolume']
        if 'dayHigh' in info:
            row["DayHigh"] = info['dayHigh']
        if 'dayLow' in info:
            row["DayLow"] = info['dayLow']
        if 'fiftyDayAverage' in info:
            row["Avg50D"] = info['fiftyDayAverage']
        if 'previousClose' in info:
            row["PreviousClose"] = info['previousClose']
        if 'trailingPE' in info:
            row["TrailingPE"] = info['trailingPE']
    except:
        print('Not found:', row.Ticker)


save_df_as_image(portfolio_df, "portfolio.png")
print('shish kebab')
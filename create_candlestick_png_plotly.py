import pandas as pd
# from pandas_datareader import data as web
import yfinance as yf
import plotly.offline
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
from datetime import datetime, time, timedelta
from dateutil.relativedelta import *

ticker = 'AAPL'
period = "5d"
interval = "5m"

intraday_df = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = ticker,

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = period,

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = interval,

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = False,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )

intraday_df = intraday_df.dropna(how='all')

title = ticker + ' ' + min(intraday_df.index).strftime("%Y"+"-"+"%m"+"-"+"%d") + ' (5m interval)'

plotly.io.orca.config.executable = r'C:\Users\Kuba\AppData\Local\Programs\Python\Python37\Lib\site-packages\orca'
plotly.io.orca.config.save()

fig = make_subplots(rows=2, cols=1)

fig.data = []
fig.layout = {}

fig.append_trace(
    go.Candlestick(x=intraday_df.index,
                open=intraday_df['Open'],
                high=intraday_df['High'],
                low=intraday_df['Low'],
                close=intraday_df['Close']),
    row=1, col=1
)

fig.append_trace(
    go.Bar(x=intraday_df.index, y=intraday_df.Volume, 
           marker={'color': intraday_df.Volume, 'colorscale': 'inferno_r'}),
    row=2, col=1
)


fig.update_layout(xaxis_rangeslider_visible=False, showlegend=False, title=title,
                margin=dict(l=20, r=20, t=80, b=40), title_font_size=27)

# fig.show()

plotly.io.write_image(fig, "intraday.png",
                      scale=None, width=None, height=None)


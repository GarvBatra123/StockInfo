# Desc: this programme shows how to create an interactive candlestick chart using plotly with python

import plotly
import plotly.graph_objects as go
import pandas as pd
import yfinance as yf

stock = input("PLEASE ENTER THE STOCK SYMBOL WHOSE INFORMATION YOU WANT TO CHECK: ").upper()
df = yf.download(stock, period = "1y", interval = "1h")
# print(df.head())
Open, High, Low, Close, AdjClose, Volume = df["Open"], df["High"], df["Low"], df["Close"], df["Adj Close"], df["Volume"]

# creating an interactive candlestick chart
figure = go.Figure(
    data = [
        go.Candlestick(x=df.index,
                       low = Low,
                       high = High, 
                       close = Close, 
                       open = Open,
                       increasing_line_color = "green", 
                       decreasing_line_color = "red")
    ]
)

# figure.update_layout(xaxis_rangeslider_visible=True)

figure.update_layout(
    title = f"{stock} PRICE",
    yaxis_title = "Amazon Stock Price USD ($)",
    xaxis_title = "Date"
)

figure.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1h", step="hour", stepmode="backward"),
            dict(count=5, label="5h", step="hour", stepmode="backward"),
            dict(count=1, label="1d", step="day", stepmode="backward"),
            dict(count=10, label="10d", step="day", stepmode="backward"),
            dict(count=1, label="1mo", step="month", stepmode="backward"),
            dict(count=2, label="2mo", step="month", stepmode="backward"),
            dict(count=5, label="5mo", step="month", stepmode="backward"),
            dict(step="all")
        ])
    )
)


figure.show()

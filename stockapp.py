import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
# Type the ticker symbol you wish to research, below will produce a chart with an 8 day and 20 day simple moving average.
""")

#define the ticker symbol
tickerSymbol = st.text_input('What Stock Symbol are you looking for?')
timeframe = st.selectbox('How far back do want to go?', ('1h','1d','1mo','1y'), help='1h- 1 hour, 1d- 1 day, 1mo- 1 month, 1y- 1 year')
val = st.selectbox('at what time interval would you like the data?', ('1m','15m','30m','1h','4h','1d'), help='Minimum for 1y is 1d, 1d is 1m, 1mo is 1d')
#get data on this ticker
tickerData = yf.download(tickerSymbol,period=timeframe,interval=val)
# Open	High	Low	Close	Volume
tickerData['8SMA'] = tickerData['Close'].rolling(8).mean()
tickerData['20SMA'] = tickerData['Close'].rolling(20).mean()
tickerData['Diff'] = tickerData['Close'] - tickerData['Open']
st.write("""
## Closing Price, 8 day Simple Moving Average, 20 day Simple Moving Average
###### When the 8 day SMA is crosses above the 20 day SMA, that is a buy/long signal.
###### Just the same when 8SMA crosses under the 20SMA, that is a sell/short signal
""")
st.line_chart(tickerData[['Close','8SMA','20SMA']])
st.write("""
## High/Low Price
""")
st.line_chart(tickerData[['High','Low']])
st.write("""
##Daily Change
""")
st.bar_chart(tickerData['Diff'])


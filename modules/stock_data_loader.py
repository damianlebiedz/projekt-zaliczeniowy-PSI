import pandas as pd
import yfinance as yf
from datetime import timedelta


def load_timeframe(start_date, end_date):
    try:
        business_days = pd.date_range(start=start_date, end=end_date, freq='B')
        timeframe = pd.DataFrame({'Date': business_days, 'Open': 0.0, 'Close': 0.0, 'Daily change [%]': 0.0,
                                  'Total change [%]': 0.0})

        return timeframe

    except Exception as e:
        print(f'Error in load_timeframe: {e}')

def load_stock_timeframe(ticker, timeframe):
    for index, row in timeframe.iterrows():
        try:
            date = row['Date']
            data = yf.download(ticker, start=date.strftime('%Y-%m-%d'),
                                   end=(date + timedelta(days=1)).strftime('%Y-%m-%d'), auto_adjust=False)
            open_price = data['Open'].iloc[0] if isinstance(data['Open'].iloc[0], float) else data['Open'].iloc[
                0].item()
            close_price = data['Close'].iloc[0] if isinstance(data['Close'].iloc[0], float) else data['Close'].iloc[
                0].item()

            timeframe.loc[index, 'Open'] = open_price
            timeframe.loc[index, 'Close'] = close_price

        except Exception as e:
            print(f"Error in load_stock_timeframe while retrieving data for {ticker} on {row['Date']}: {e}")
            timeframe.drop(index, inplace=True)
            continue

    timeframe['Daily change [%]'] = (timeframe['Close'] / timeframe['Open'] - 1) * 100
    timeframe['Total change [%]'] = (timeframe['Close'] / timeframe['Close'].iloc[0] - 1) * 100

def biggest_change(timeframe):
    if len(timeframe) >= 1:
        timeframe_copy = timeframe.copy()
        timeframe_sorted = timeframe_copy.reindex(
            timeframe_copy['Daily change [%]'].abs().sort_values(ascending=False).index
        )
        return timeframe_sorted.head()
    else:
        print('timeframe < 0 - check the date range in the controller!')
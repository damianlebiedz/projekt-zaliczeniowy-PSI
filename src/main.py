from modules.controller import *
from modules.stock_data_loader import *
from modules.plot_generator import *
from modules.x_data_loader import *

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    timeframe = load_timeframe(start_date, end_date)
    load_stock_timeframe(ticker, timeframe)
    print(timeframe)

    stock_plot(timeframe, 'Daily change [%]', ticker)
    stock_plot(timeframe, 'Total change [%]', ticker)

    biggest_changes = biggest_changes(timeframe, num_of_biggest_changes)
    print(biggest_changes)

    ## ERROR - fix needed
    # date = '2025-04-04'
    # popular_tweets = get_popular_tweets(date, keywords, max_tweets, top_n)
    # print(popular_tweets)
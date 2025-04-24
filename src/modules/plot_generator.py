import matplotlib.pyplot as plt


def stock_plot(timeframe, column, ticker):
    try:
        plt.plot(timeframe['Date'], timeframe[f'{column}'], label=f'{column} of {ticker}', linewidth=3, linestyle='--',
                 color='black')
        plt.xlabel('Date')
        plt.ylabel(f'{column}')
        plt.legend()
        plt.grid()
        plt.show()

    except Exception as e:
        print(f"Error in stock_plot: {e}")
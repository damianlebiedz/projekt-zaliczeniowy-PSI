from modules.controller import *
from modules.reddit_data_loader import *
from modules.sentiment_analysis import *
from modules.stock_data_loader import *
from modules.visualization import *

if __name__ == "__main__":
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)

    timeframe = load_timeframe(start_date, end_date)
    load_stock_timeframe(ticker, timeframe)

    stock_plot(timeframe, 'Daily change [%]', ticker)
    stock_plot(timeframe, 'Total change [%]', ticker)

    biggest_changes = biggest_changes(timeframe, num_of_biggest_changes)
    print(biggest_changes)
    dates = biggest_changes["Date"].tolist()

    ### main function to analyze all days from biggest_changes
    # for date in dates:
    #     print(f'Analysis for day {date}...')
    #     ...

    ### Debugging with one date
    date = '2025-04-04'
    df = fetch_top_comments_as_dataframe(date, top_x)
    print(df.head())

    df['embedding'] = df['text'].apply(get_embedding)
    df['sentiment'] = df['text'].apply(analyze_sentiment)

    embeddings = df['embedding'].tolist()
    df['cluster'] = cluster_pca_kmeans(embeddings, n_clusters)

    plot_wordcloud(df)
    overall_sentiment = calculate_weighted_sentiment(df)
    print(f"Overall weighted sentiment for the day {date}: {overall_sentiment:.3f}")

    """
        1: POSITIVE sentiment
        0: NEUTRAL sentiment
       -1: NEGATIVE sentiment
    """

    plot_cluster_wordcloud(df)

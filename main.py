from modules.controller import *
from modules.reddit_data_loader import *
from modules.sentiment_analysis import *
from modules.stock_data_loader import *
from modules.visualization import *

if __name__ == "__main__":
    timeframe = load_timeframe(start_date, end_date)
    load_stock_timeframe(ticker, timeframe)

    stock_plot(timeframe, 'Daily change [%]', ticker)
    stock_plot(timeframe, 'Total change [%]', ticker)

    biggest_change = biggest_change(timeframe)
    print(biggest_change)

    date = biggest_change['Date'].iloc[0].strftime("%Y-%m-%d")
    print(f'Analysis for day {date}...')
    df = fetch_top_comments_as_dataframe(date, top_x)
    print(df.head())

    df['embedding'] = df['text'].apply(get_embedding)
    df['sentiment'] = df['text'].apply(analyze_sentiment)

    embeddings = df['embedding'].tolist()
    df['cluster'] = cluster_pca_kmeans(embeddings, n_clusters)
    plot_wordcloud(df, date, stopwords=STOPWORDS_CUSTOM, word_regex=WORD_REGEX)

    overall_sentiment = calculate_weighted_sentiment(df)
    plot_sentiment(overall_sentiment, date)

    plot_wordcloud(df, date, cluster_column='cluster', stopwords=STOPWORDS_CUSTOM, word_regex=WORD_REGEX)
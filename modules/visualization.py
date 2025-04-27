import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import re


STOPWORDS_CUSTOM = set(STOPWORDS)
for letter in list("abcdefghijklmnopqrstuvwxyz"):
    STOPWORDS_CUSTOM.add(letter)

WORD_REGEX = re.compile(r"\b[a-zA-Z]{2,}\b")

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

def plot_wordcloud(df):
    text_series = df['text'].astype(str).tolist()
    all_text = ' '.join(text_series)
    tokens = WORD_REGEX.findall(all_text)
    combined = ' '.join(tokens)

    wc = WordCloud(
        width=800,
        height=400,
        background_color='white',
        stopwords=STOPWORDS_CUSTOM
    ).generate(combined)

    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def plot_cluster_wordcloud(df):
    for cluster_id in sorted(df['cluster'].unique()):
        texts = df.loc[df['cluster'] == cluster_id, 'text'].astype(str).tolist()
        all_text = ' '.join(texts)
        tokens = WORD_REGEX.findall(all_text)
        combined = ' '.join(tokens)

        wc = WordCloud(
            width=800,
            height=400,
            background_color='white',
            stopwords=STOPWORDS_CUSTOM
        ).generate(combined)

        plt.figure(figsize=(10, 5))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.title(f"WordCloud for Cluster {cluster_id}")
        plt.show()
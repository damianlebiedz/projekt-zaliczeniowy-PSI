import matplotlib.colors as mcolors
from wordcloud import STOPWORDS
import re
import numpy as np


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
        plt.savefig(f"output/{column}.png")
        plt.show()

    except Exception as e:
        print(f"Error in stock_plot: {e}")

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def plot_wordcloud(df, date, text_column='text', cluster_column=None, stopwords=None, word_regex=None):
    def create_wordcloud(texts, title):
        all_text = ' '.join(map(str, texts))
        if word_regex:
            tokens = word_regex.findall(all_text)
            combined = ' '.join(tokens)
        else:
            combined = all_text

        wc = WordCloud(
            width=800,
            height=400,
            background_color='white',
            stopwords=stopwords
        ).generate(combined)

        plt.figure(figsize=(10, 5))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        if title:
            plt.title(title)
        plt.savefig(f"output/{title}.png")
        plt.show()

    if cluster_column:
        for cluster_id in sorted(df[cluster_column].unique()):
            texts = df.loc[df[cluster_column] == cluster_id, text_column]
            create_wordcloud(texts, title=f"WordCloud for Cluster {cluster_id}")
    else:
        texts = df[text_column]
        create_wordcloud(texts, title=f"Global WordCloud for the day {date}")


def plot_sentiment(sentiment, date):
    if sentiment < -1 or sentiment > 1:
        raise ValueError("Sentiment value outside the range [-1, 1]")

    cmap = mcolors.LinearSegmentedColormap.from_list(
        'sentiment_cmap',
        [(0, 'red'), (0.5, 'gray'), (1, 'green')]
    )

    fig, ax = plt.subplots(figsize=(8, 2))

    gradient = np.linspace(-1, 1, 500)
    gradient = np.vstack((gradient, gradient))

    ax.imshow(gradient, aspect='auto', cmap=cmap, extent=[-1, 1, -0.5, 0.5])
    ax.axvline(sentiment, color='black', linewidth=3)

    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_title(f'Overall weighted sentiment for the day {date}: {sentiment:.3f}')
    plt.savefig(f"output/Sentiment for {date}.png")
    plt.show()
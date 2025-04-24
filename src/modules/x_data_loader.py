import pandas as pd
import snscrape.modules.twitter as sntwitter
import requests

### ERROR - fix needed
def get_popular_tweets(target_date, keywords, max_tweets, top_n):
    formatted_keywords = []
    for kw in keywords:
        kw = kw.strip()
        if ' ' in kw and not (kw.startswith('"') and kw.endswith('"')):
            formatted_keywords.append(f'"{kw}"')
        else:
            formatted_keywords.append(kw)

    query_keywords = ' OR '.join(formatted_keywords)
    query = f'({query_keywords}) since:{target_date} until:{target_date} lang:en -filter:retweets'

    tweets = []

    try:
        session = requests.Session()
        session.verify = False
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
            if i >= max_tweets:
                break
            tweets.append([
                tweet.date,
                tweet.content,
                tweet.user.username,
                tweet.likeCount,
                tweet.retweetCount,
                tweet.replyCount
            ])

    except Exception as e:
        print(f'Error in tweets_loader: {e}')
        return pd.DataFrame()

    df = pd.DataFrame(tweets, columns=['Date', 'Tweet', 'User', 'Likes', 'Retweets', 'Answers'])

    if not df.empty:
        df['Sum of interaction'] = df[['Likes', 'Retweets', 'Answers']].sum(axis=1)
        return df.sort_values('Sum of interaction', ascending=False).head(top_n)

    return df
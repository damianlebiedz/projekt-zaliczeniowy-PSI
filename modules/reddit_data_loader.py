import os
import pandas as pd
import praw
from praw.models import Comment
from dotenv import load_dotenv
from datetime import datetime
import re


load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = "sentiment-analysis by /u/your_username"

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=USER_AGENT
)

def format_date(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt.strftime("%B %d, %Y")

def is_valid_comment(text):
    text = text.strip().lower()
    if text.startswith("[deleted") or text.startswith("[ removed"):
        return False
    if re.search(r"http[s]?://|www\.|\.(com|jpg|png|gif)", text, re.IGNORECASE):
        return False
    if re.search(r"!\[.*?\]\(.*?\)", text):
        return False
    return True

def fetch_top_comments_as_dataframe(date_str, top_x=100):
    formatted_date = format_date(date_str)
    expected_title = f"Daily Discussion Thread for {formatted_date}"
    print(f"Searching for thread: {expected_title}...")
    subreddit = reddit.subreddit("wallstreetbets")

    for submission in subreddit.search("Daily Discussion Thread", sort="new", time_filter="all"):
        if expected_title in submission.title:
            print(f"Found: {submission.title}")

            print("Setting comment sort to 'top'...")
            submission.comment_sort = "top"
            submission.comments.replace_more(limit=0)

            comments = submission.comments.list()

            valid_comments = [
                comment for comment in comments
                if isinstance(comment, Comment) and is_valid_comment(comment.body)
            ]

            sorted_comments = sorted(valid_comments, key=lambda c: c.score, reverse=True)
            print(f"Taking top {top_x} valid comments...")

            top_comments_data = []
            for comment in sorted_comments[:top_x]:
                top_comments_data.append({
                    "text": comment.body,
                    "upvotes": max(comment.score, 1)
                })

            df = pd.DataFrame(top_comments_data)
            return df

    raise ValueError(f"Could not find Daily Discussion Thread for {date_str}")
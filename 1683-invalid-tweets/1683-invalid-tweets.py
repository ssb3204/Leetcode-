import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    filt = tweets[tweets["content"].str.len()>15]
    return filt[["tweet_id"]]
    
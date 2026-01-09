import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    filtered = views[views["viewer_id"]==views["author_id"]].sort_values(by="author_id")
    return filtered[["author_id"]].rename(columns={"author_id":"id"}).drop_duplicates()
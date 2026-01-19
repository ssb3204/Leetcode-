import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    df =scores.copy()
    df["rank"] = df["score"].rank(method="dense",ascending=False)
    return df.sort_values("score",ascending=False)[["score","rank"]]
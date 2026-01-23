import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df=activities.drop_duplicates(subset=["sell_date","product"])

    df=df.groupby("sell_date")["product"].agg(
            num_sold="nunique",
            products=lambda s : ",".join(sorted(s.astype(str).unique()))
         ).reset_index()


    return df
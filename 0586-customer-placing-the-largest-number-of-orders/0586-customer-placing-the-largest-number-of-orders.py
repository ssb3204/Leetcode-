import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    cnt_df= orders["customer_number"].value_counts().reset_index(name="cnt")
    cnt_df = cnt_df.rename(columns={"index":"customer_number"})
    
    val = cnt_df["cnt"].max()
    return cnt_df.loc[cnt_df["cnt"]==val,["customer_number"]]

    
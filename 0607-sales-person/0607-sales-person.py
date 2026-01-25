import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df= orders.merge(company,on="com_id",how="left")
    df = df.loc[df["name"]=="RED","sales_id"]
    df=sales_person.loc[~sales_person["sales_id"].isin(df),["name"]]

    return df
    
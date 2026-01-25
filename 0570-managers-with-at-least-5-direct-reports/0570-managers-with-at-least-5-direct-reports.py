import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # df= employee.merge(employee,left_on="managerId",right_on="id",how="left")
    df =employee["managerId"].value_counts().reset_index(name="cnt")

    df=df.loc[df["cnt"]>=5,"managerId"]
    df = employee.loc[employee["id"].isin(df), ["name"]]
    return df
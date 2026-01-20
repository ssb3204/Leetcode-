import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    cnt= accounts["income"]

    low =(cnt<20000).sum()
    mid =((cnt>=20000)&(cnt<=50000)).sum()
    high =(cnt>50000).sum()

    filtered = pd.DataFrame({
        "category":["Low Salary","Average Salary","High Salary"],
        "accounts_count": [low, mid, high]
    })

    return filtered.sort_values("accounts_count",ascending=False)
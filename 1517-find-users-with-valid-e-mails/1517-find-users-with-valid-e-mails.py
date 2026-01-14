import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    filtered = users[users["mail"].str.match(r"^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$")]
    return filtered[["user_id","name","mail"]] 

    
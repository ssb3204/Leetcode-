import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users=users.copy()
    users["name"]=users["name"].str.capitalize()
    
    return users[["user_id","name"]].sort_values("user_id")
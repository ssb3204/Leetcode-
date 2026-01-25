import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    filtered = pd.merge(employees,employee_uni,on="id",how="left")
    return filtered[["unique_id","name"]]

    
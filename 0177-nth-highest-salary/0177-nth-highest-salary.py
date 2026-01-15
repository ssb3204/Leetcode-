import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    col =f"getNthHighestSalary({N})"

    if N is None or N<=0:
        return pd.DataFrame({col:[None]})
    
    m = employee.salary.drop_duplicates().sort_values(ascending=False)

    value = m.iloc[N-1] if len(m) >= N else None
    return pd.DataFrame({col:[value]})
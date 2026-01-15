import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    filtered = employee.salary.drop_duplicates()
    value = filtered.nlargest(2).iloc[-1] if len(filtered) >=2 else None
    if value is None:
        return pd.DataFrame({"SecondHighestSalary":[None]})
    
    result = pd.DataFrame({"SecondHighestSalary":[value]})

    return result
    
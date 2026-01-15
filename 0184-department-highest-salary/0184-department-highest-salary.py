import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    filtered = pd.merge(employee,department, left_on ="departmentId",right_on="id",how="inner",suffixes=("_emp","_dept"))

    max_sal = filtered.groupby("name_dept")["salary"].transform("max")
    top = filtered[filtered["salary"].eq(max_sal)]
    
    return top[["name_dept", "name_emp", "salary"]].rename(
        columns={"name_dept": "Department", "name_emp": "Employee", "salary": "Salary"}
    )
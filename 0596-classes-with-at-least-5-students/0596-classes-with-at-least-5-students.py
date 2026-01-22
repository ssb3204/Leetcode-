import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df=courses.copy()
    cnt_df = df["class"].value_counts().reset_index(name="cnt")
    return cnt_df[cnt_df["cnt"]>=5][["class"]]
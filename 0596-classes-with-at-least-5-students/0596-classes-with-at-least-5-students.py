import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:

    cnt_df = courses["class"].value_counts().reset_index(name="cnt")
    cnt_df = cnt_df.rename(columns={"index":"class"})
    return cnt_df[cnt_df["cnt"]>=5][["class"]]
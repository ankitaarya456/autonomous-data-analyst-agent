import pandas as pd

def infer_task(df: pd.DataFrame, target: str) -> str:
    y = df[target]
    if y.dtype == object or y.nunique() <= 20:
        return "classification"
    return "regression"

import pandas as pd

class EDAAgent:
    def profile(self, df: pd.DataFrame) -> pd.DataFrame:
        return pd.DataFrame({
            "dtype": df.dtypes.astype(str),
            "missing": df.isnull().sum(),
            "unique": df.nunique()
        })

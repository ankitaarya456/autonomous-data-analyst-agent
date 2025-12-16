class InsightAgent:
    def generate(self, df):
        insights = []
        insights.append(f"Dataset has {df.shape[0]} rows and {df.shape[1]} columns")

        num_cols = df.select_dtypes(include="number").columns
        cat_cols = df.select_dtypes(exclude="number").columns

        insights.append(f"Numeric columns: {len(num_cols)}")
        insights.append(f"Categorical columns: {len(cat_cols)}")

        high_card = [c for c in cat_cols if df[c].nunique() > 50]
        if high_card:
            insights.append(f"High-cardinality categorical columns: {high_card}")

        return insights

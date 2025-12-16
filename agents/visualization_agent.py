import plotly.express as px

class VisualizationAgent:
    def histogram(self, df, col):
        return px.histogram(df, x=col, title=f"Distribution of {col}")

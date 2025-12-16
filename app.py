import streamlit as st
import pandas as pd

from utils.data_loader import load_csv
from utils.task_inference import infer_task
from agents.planner_agent import PlannerAgent
from agents.eda_agent import EDAAgent
from agents.insight_agent import InsightAgent
from agents.visualization_agent import VisualizationAgent
from agents.ml_agent import MLAgent

st.set_page_config(page_title="Autonomous Data Analyst Agent", layout="wide")

st.title("🧠 Autonomous Data Analyst Agent")

use_llm = st.toggle("Enable AI Mentor (High RAM)", value=False)

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = load_csv(uploaded_file)
    st.success("Dataset loaded successfully")

    user_goal = st.text_input(
        "What do you want to know?",
        placeholder="e.g. analyze this dataset, predict price"
    )

    planner = PlannerAgent()
    steps = planner.plan(user_goal, df)

    st.subheader("🔍 Agent Plan")
    st.write(steps)

    if "eda" in steps:
        st.subheader("📊 Exploratory Data Analysis")
        eda = EDAAgent()
        st.dataframe(eda.profile(df), use_container_width=True)

    if "visualize" in steps:
        st.subheader("📈 Visualizations")
        viz = VisualizationAgent()
        num_cols = df.select_dtypes(include="number").columns
        if len(num_cols) > 0:
            st.plotly_chart(viz.histogram(df, num_cols[0]))

    if "ml" in steps:
        st.subheader("🤖 Machine Learning")
        target = st.selectbox("Select target column", df.columns)
        task = infer_task(df, target)

        X = df.drop(columns=[target]).select_dtypes(include="number")
        y = df[target]

        if X.shape[1] == 0:
            st.warning("No numeric features available for ML.")
        else:
            ml = MLAgent()
            score = ml.train(X, y, task)
            st.success(f"{task.upper()} score: {score:.4f}")

    if "insights" in steps:
        st.subheader("💡 Insights")
        ins = InsightAgent()
        for insight in ins.generate(df):
            st.success(insight)

    if use_llm:
        st.subheader("🤖 AI Mentor Insight")
        from agents.llm_agent import llm_insight
        summary = df.describe(include="all").to_string()
        st.info(llm_insight(user_goal, summary))

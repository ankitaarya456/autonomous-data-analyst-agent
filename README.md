# 🧠 Autonomous Data Analyst Agent

A **Streamlit-based agentic AI application** that automatically analyzes CSV datasets and provides end-to-end data understanding — from exploratory data analysis (EDA) to visualizations, machine learning, and AI-generated insights.

🔗 **Live App**: [https://autonomous-data-analyst-agent-ankita-arya.streamlit.app/](https://autonomous-data-analyst-agent-ankita-arya.streamlit.app/)

🔗 **LinkedIn Project Post**:  
[https://www.linkedin.com/posts/ankita-arya-06a509234_agenticai-artificialintelligence-datascience-activity-7407001209657708545-0UI0](https://www.linkedin.com/posts/ankita-arya-06a509234_agenticai-artificialintelligence-datascience-activity-7407001209657708545-0UI0)


---

## 🚀 Key Features

* 📊 **Automatic Exploratory Data Analysis (EDA)**
  Generates dataset profiles including data types, missing values, and unique counts.

* 💡 **Actionable Insights Generation**
  Summarizes dataset characteristics such as numeric vs categorical columns and high-cardinality features.

* 📈 **Interactive Visualizations**
  Creates Plotly-based charts (e.g., histograms) for numeric features.

* 🤖 **Machine Learning Automation**

  * Automatically infers task type (classification / regression)
  * Trains appropriate ML models
  * Displays evaluation scores

* 🧠 **Optional AI Mentor (LLM-powered)**
  Uses a lightweight transformer model (FLAN-T5) to generate natural-language insights from the dataset.

* 📁 **CSV-first Workflow**
  Simply upload a CSV file and start analyzing.

---

## 🗂️ Project Structure

```
autonomous-data-analyst-agent/
│
├── app.py                     # Streamlit entry point
├── agents/                    # Agent-based architecture
│   ├── planner_agent.py       # Decides analysis steps
│   ├── eda_agent.py           # Dataset profiling
│   ├── visualization_agent.py # Charts & plots
│   ├── ml_agent.py            # ML training & evaluation
│   ├── insight_agent.py       # Rule-based insights
│   └── llm_agent.py           # LLM-powered insights
│
├── utils/                     # Utility functions
│   ├── data_loader.py         # CSV loader
│   └── task_inference.py      # ML task inference
│
├── memory/                    # Future memory extension
│   └── vector_store.py
│
├── reports/                   # Auto-generated reports
│   └── sample_report.md
│
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
├── LICENSE                    # MIT License
└── .gitignore
```

---

## 🧪 How the Agent Works

1. **User uploads a CSV file**
2. **PlannerAgent** decides what to do based on user intent
3. Agents are executed dynamically:

   * EDAAgent → profiling
   * VisualizationAgent → plots
   * MLAgent → model training
   * InsightAgent → insights
   * LLMAgent → AI-generated explanations (optional)

This modular design follows **agentic AI principles**.

---

## ▶️ Run Locally

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the app

```bash
streamlit run app.py
```

---

## 🌐 Deployment

The application is deployed on **Streamlit Community Cloud** and connected directly to this GitHub repository.

🔗 Live URL:
[https://autonomous-data-analyst-agent-ankita-arya.streamlit.app/](https://autonomous-data-analyst-agent-ankita-arya.streamlit.app/)

---

## 📦 Tech Stack

* **Frontend / App**: Streamlit
* **Data Handling**: Pandas, NumPy
* **Visualization**: Plotly
* **Machine Learning**: scikit-learn
* **LLM (Optional)**: Hugging Face Transformers (FLAN-T5)
* **Deployment**: Streamlit Cloud

---
## License
This project is licensed under the Apache License 2.0.
---


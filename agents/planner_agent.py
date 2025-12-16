class PlannerAgent:
    def plan(self, user_goal: str, df):
        if not user_goal:
            return ["eda", "insights"]

        goal = user_goal.lower()
        steps = []

        if any(k in goal for k in ["analyze", "eda", "summary"]):
            steps.append("eda")

        if any(k in goal for k in ["plot", "visual", "graph"]):
            steps.append("visualize")

        if any(k in goal for k in ["predict", "train", "model"]):
            steps.append("ml")

        steps.append("insights")
        return steps

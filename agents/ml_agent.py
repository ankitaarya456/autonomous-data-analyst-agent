from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, accuracy_score

class MLAgent:
    def train(self, X, y, task):
        Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2)

        if task == "classification":
            model = LogisticRegression(max_iter=300)
            model.fit(Xtr, ytr)
            return accuracy_score(yte, model.predict(Xte))

        model = LinearRegression()
        model.fit(Xtr, ytr)
        return r2_score(yte, model.predict(Xte))

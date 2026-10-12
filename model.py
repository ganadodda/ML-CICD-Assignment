from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def train_model():
    """Train a deterministic Decision Tree model on the Iris dataset."""
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return model, accuracy


def predict_sample(model, sample=None):
    """Predict an Iris class for one sample."""
    if sample is None:
        sample = [[5.1, 3.5, 1.4, 0.2]]
    return int(model.predict(sample)[0])


if __name__ == "__main__":
    model, accuracy = train_model()
    print("Model: Decision Tree Classifier")
    print("Dataset: Iris")
    print(f"Accuracy: {accuracy:.2%}")
    print(f"Example prediction (class number): {predict_sample(model)}")

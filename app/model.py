import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

def train_model():
    # Load dataset
    data = load_iris()
    X, y = data.data, data.target
    # Train a simple model
    model = RandomForestClassifier()
    model.fit(X, y)
    # Save the model to a file
    with open("model.pkl", "wb") as file:
        pickle.dump(model, file)
    print("Model saved as 'model.pkl'")

if __name__ == "__main__":
    train_model()

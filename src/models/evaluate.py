import pandas as pd
import sys
import joblib
from sklearn.metrics import mean_squared_error

def evaluate_model(model_path, X_test_path, y_test_path):
    model = joblib.load(model_path)
    X_test = pd.read_csv(X_test_path)
    y_test = pd.read_csv(y_test_path)
    
    predictions = model.predict(X_test)
    mse = mean_squared_error (y_test, predictions)
    print(f"Error Cuadrático Medio: {mse}")

if __name__ == '__main__':
    model_path = sys.argv[1]
    X_test_path = sys.argv[2]
    y_test_path = sys.argv[3]
    
    evaluate_model(model_path, X_test_path, y_test_path)


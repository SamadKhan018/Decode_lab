import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score

print("--- Starting AI Data Classification Pipeline ---")


iris = load_iris()
X = iris.data 
y = iris.target  

print(f"Dataset successfully loaded. Total samples: {X.shape[0]}, Total features: {X.shape[1]}")


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, shuffle=True)
print(f"Data split executed: {X_train.shape[0]} training items, {X_test.shape[0]} testing items.")


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("Feature scaling successfully applied. Attribute weights are now balanced.")


k_value = 3
knn_model = KNeighborsClassifier(n_neighbors=k_value)
knn_model.fit(X_train_scaled, y_train)
print(f"KNN Classification model successfully trained with K={k_value}.")


y_pred = knn_model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print("\n================ MODEL EVALUATION SUMMARY ================")
print(f"Overall Model Predictive Accuracy: {accuracy * 100:.2f}%")
print("\nDetailed Performance Metrics Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
print("==========================================================")
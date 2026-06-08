import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

from feature_extraction import extract_features


# Load dataset
df = pd.read_csv("dataset/malicious_phish.csv")

print("Dataset loaded successfully")
print(df.head())
print(df.columns)


# Adjust column names if needed
# Expected columns: url and type
# type usually contains: benign, phishing, malware, defacement

df = df[["url", "type"]]
print(df["type"].value_counts())

# Keep only benign and phishing websites
df["label"] = df["type"].apply(lambda x: 0 if x == "benign" else 1)
print(df["label"].value_counts())
# Convert labels into numbers
# benign = 0, phishing = 1


# Extract features from URLs
X = df["url"].apply(extract_features).tolist()
y = df["label"]

# Split data into training and testing parts
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    shuffle=True,
    stratify=y
)

# Train Random Forest model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Training Completed")
print("Accuracy:", round(accuracy * 100, 2), "%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Create model folder if it does not exist
os.makedirs("model", exist_ok=True)

# Save trained model
joblib.dump(model, "model/phishing_model.pkl")

print("\nModel saved successfully in model/phishing_model.pkl")
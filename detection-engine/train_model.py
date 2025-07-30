import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os

# Step 1: Load preprocessed dataset
data_file = "data/cicids2017_cleaned.csv"
df = pd.read_csv(data_file)
print(f"📄 Loaded dataset: {df.shape}")

# Step 2: Split features and labels
X = df.drop(columns=["Label"])
y = df["Label"]

# Step 3: Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Step 5: Train Random Forest model
clf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
clf.fit(X_train, y_train)

# Step 6: Evaluate model
y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\n✅ Accuracy: {acc:.4f}")
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))
print("\n🧾 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Step 7: Save model to models/ folder
model_dir = "detection-engine/models"
os.makedirs(model_dir, exist_ok=True)
model_path = os.path.join(model_dir, "random_forest_model.pkl")
joblib.dump(clf, model_path)
print(f"💾 Model saved to {model_path}")

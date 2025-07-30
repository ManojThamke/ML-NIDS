import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.metrics import classification_report, accuracy_score
from imblearn.over_sampling import SMOTE

# Step 1: Load dataset
df = pd.read_csv("data/cicids2017_cleaned.csv")
print(f"📊 Dataset shape: {df.shape}")

X = df.drop("Label", axis=1)
y = df["Label"]

# Step 2: Feature Selection (Top 30 features)
selector = SelectKBest(score_func=f_classif, k=30)
X_new = selector.fit_transform(X, y)
selected_features = X.columns[selector.get_support()]
print(f"✅ Top 30 features selected:\n{list(selected_features)}")

# Step 3: Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_new)

# Step 4: Handle Imbalance with SMOTE
sm = SMOTE(random_state=42, sampling_strategy='auto')
X_res, y_res = sm.fit_resample(X_scaled, y)
print(f"⚖️ After SMOTE: {X_res.shape}, {y_res.value_counts().to_dict()}")

# Step 5: Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.3, random_state=42)

# Step 6: Grid Search for best RandomForest
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [None, 20, 30],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2],
}
grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42, n_jobs=-1),
    param_grid,
    cv=3,
    verbose=1,
    scoring='f1_weighted'
)

print("🔍 Running GridSearchCV...")
grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_
print(f"🏆 Best Params: {grid_search.best_params_}")

# Step 7: Evaluate model
y_pred = best_model.predict(X_test)
print("\n✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

# Step 8: Save optimized model
joblib.dump(best_model, "detection-engine/models/random_forest_optimized.pkl")
print("💾 Optimized model saved to models/random_forest_optimized.pkl")

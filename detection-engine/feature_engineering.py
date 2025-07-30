import pandas as pd
import os

# Step 1: Load all CSVs
data_dir = "data/cicids2017"
all_files = [f for f in os.listdir(data_dir) if f.endswith(".csv")]
dataframes = []

print("📦 Loading datasets...")
for file in all_files:
    path = os.path.join(data_dir, file)
    df = pd.read_csv(path, low_memory=False)
    dataframes.append(df)
    print(f"✔ Loaded {file} - {df.shape}")

# Step 2: Concatenate all data
df_all = pd.concat(dataframes, ignore_index=True)
print("\n🧮 Combined shape:", df_all.shape)

# Step 3: Clean column names (remove leading/trailing spaces)
df_all.columns = df_all.columns.str.strip()

# Step 4: Drop columns with NaNs or infs
df_all.replace([float('inf'), float('-inf')], pd.NA, inplace=True)
df_all.dropna(axis=1, inplace=True)
print("🧹 Dropped columns with NaNs or infinite values")

# Step 5: Drop non-numeric and irrelevant columns
irrelevant = ['Flow ID', 'Source IP', 'Destination IP', 'Timestamp']
df_all.drop(columns=[col for col in irrelevant if col in df_all.columns], inplace=True)

# ✅ Confirm 'Label' column exists
if 'Label' not in df_all.columns:
    raise ValueError("❌ 'Label' column not found after cleanup. Please inspect CSV column names.")

# Step 6: Encode label column (Normal=0, Attack=1)
df_all['Label'] = df_all['Label'].apply(lambda x: 0 if x == 'BENIGN' else 1)

# Step 7: Save cleaned dataset
output_file = "data/cicids2017_cleaned.csv"
df_all.to_csv(output_file, index=False)
print(f"✅ Cleaned dataset saved as {output_file}")

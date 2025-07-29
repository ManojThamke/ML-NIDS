# detection-engine/inspect_cicids.py

import pandas as pd
import os

data_path = "data/cicids2017/"
files = sorted(os.listdir(data_path))

for file in files:
    if file.endswith(".csv"):
        print(f"\n📁 File: {file}")
        df = pd.read_csv(os.path.join(data_path, file), low_memory=False)
        print("🔹 Rows:", len(df))
        print("🔹 Columns:", len(df.columns))
        print("🔹 Missing values:", df.isnull().sum().sum())
        print("🔹 Labels:", df['Label'].value_counts().head())

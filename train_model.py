import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# Define columns
num_scaled_cols = ['ph', 'turbidity', 'conductivity', 'temperature']
other_cols = ['year', 'month']  # not scaled
feature_cols = other_cols + num_scaled_cols
target_col = 'coagulant_dosage'

# Load data
df = pd.read_csv("water_quality_cleaned.csv")

X = df[feature_cols]
y = df[target_col]

# ColumnTransformer: scale only selected numeric columns
scaler = StandardScaler()

preprocessor = ColumnTransformer(
    transformers=[
        ('scaled_nums', scaler, num_scaled_cols)
    ],
    remainder='passthrough'  # year/month stay as-is
)

model = RandomForestRegressor(random_state=10, n_jobs=-1)

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', model)
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=10
)

pipeline.fit(X_train, y_train)

joblib.dump(pipeline, "random_forest_pipeline.joblib")
print("Saved to random_forest_pipeline.joblib")
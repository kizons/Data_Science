import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, FunctionTransformer
from sklearn.model_selection import train_test_split, GridSearchCV
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline
import joblib
from feature_utils import feature_engineering

# --- Load and prepare data ---
df = pd.read_csv('train.csv')

X = df.drop(columns='churn')
y = df['churn'].map(dict(yes=1, no=0))


# Columns
categorical_cols = ['state', 'area_code']
binary_cols = ['international_plan', 'voice_mail_plan']
numeric_cols = [col for col in X.columns if col not in categorical_cols + binary_cols + [
    'total_day_minutes', 'total_eve_minutes', 'total_night_minutes',
    'total_day_charge', 'total_eve_charge', 'total_night_charge',
    'total_day_calls', 'total_eve_calls', 'total_night_calls'
]]

# Pipeline Steps
feature_engineer = FunctionTransformer(feature_engineering)

preprocessor = ColumnTransformer(transformers=[
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols),
    ('num', StandardScaler(), numeric_cols + ['total_minutes', 'total_charge', 'total_calls']),
    ('bin', 'passthrough', binary_cols)
])

# Build pipeline with SMOTE (on training only)
pipeline = ImbPipeline(steps=[
    ('feature_engineering', feature_engineer),
    ('preprocessing', preprocessor),
    ('smote', SMOTE(random_state=42)),
    ('classifier', XGBClassifier(use_label_encoder=False, eval_metric='logloss'))
])

# Hyperparameter tuning
param_grid = {
    'classifier__n_estimators': [100],
    'classifier__learning_rate': [0.1],
    'classifier__max_depth': [6]
}

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

# Save full pipeline
joblib.dump(grid_search.best_estimator_, 'pipeline.pkl')
print("Pipeline trained and saved successfully.")
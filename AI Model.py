import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, mean_squared_error
import numpy as np

# Load updated dataset
url = "https://data.cityofchicago.org/api/views/t2qc-9pjd/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

# Clean column names
df.columns = df.columns.str.strip()

# Drop missing values
df.dropna(subset=['CURRENT_SPEED', 'REGION', 'LAST_UPDATED'], inplace=True)

# Extract hour 
df['HOUR'] = pd.to_datetime(df['LAST_UPDATED']).dt.hour

# encode region
df = pd.get_dummies(df, columns=['REGION'], drop_first=True)

# Classification 
def congestion_level(speed):
    if speed >= 35:
        return 0  # Low
    elif speed >= 20:
        return 1  # Medium
    else:
        return 2  # High

df['CongestionLevel'] = df['CURRENT_SPEED'].apply(congestion_level)


features = ['HOUR'] + [col for col in df.columns if col.startswith('REGION_')]
X = df[features]

# Classification 
y_cls = df['CongestionLevel']

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X, y_cls, test_size=0.25, random_state=42)

pipeline_cls = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(class_weight='balanced'))
])

pipeline_cls.fit(X_train_c, y_train_c)
y_pred_cls = pipeline_cls.predict(X_test_c)

print("\n Classification Report:")
print(classification_report(y_test_c, y_pred_cls, zero_division=0))

# Regression 
y_reg = df['CURRENT_SPEED']
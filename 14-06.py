# Importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
import shap

# Load the Titanic dataset
titanic_df = pd.read_csv(r'C:\Users\ug2e6u0\OneDrive TIAA\Desktop\Jupyter Notebook Titanic-Dataset.csv')

# Preprocessing
titanic_df['Age'].fillna(titanic_df['Age'].median(), inplace=True)
titanic_df['Embarked'].fillna(titanic_df['Embarked'].mode()[0], inplace=True)
titanic_df['FamilySize'] = titanic_df['SibSp'] + titanic_df['Parch']
titanic_df['Sex'] = titanic_df['Sex'].map({'male': 0, 'female': 1}) 

X = titanic_df[['Pclass', 'Sex', 'Age', 'FamilySize', 'Fare']]
y = titanic_df['Survived']

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Training a Random Forest classifier
rf_classifier = RandomForestClassifier(random_state=42)
params = {'n_estimators': [100, 200, 300],
          'max_depth': [5, 10, 15]}
grid_search = GridSearchCV(rf_classifier, params, cv=5, scoring='accuracy')
grid_search.fit(X_train_scaled, y_train)

best_rf = grid_search.best_estimator_

# Evaluating the model
y_pred = best_rf.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of Random Forest model:", accuracy)

# Analyzing feature importance
feature_importance = pd.DataFrame({'Feature': X.columns, 'Importance': best_rf.feature_importances_})
feature_importance = feature_importance.sort_values(by='Importance', ascending=False)
print("Feature Importance:")
print(feature_importance)

# Visualizing explanations using SHAP
explainer = shap.Explainer(best_rf, X_train_scaled)
shap_values = explainer(X_test_scaled)
shap.summary_plot(shap_values, X_test_scaled, plot_type="bar")
# Importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import shap

# Load the Titanic dataset
titanic_df = pd.read_csv('train.csv')

# Preprocessing
titanic_df.dropna(subset=['Age', 'Embarked'], inplace=True)
titanic_df['Sex'] = titanic_df['Sex'].map({'male': 0, 'female': 1})
X = titanic_df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
y = titanic_df['Survived']

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training a logistic regression model
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# Evaluating the model
y_pred = logreg.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of Logistic Regression model:", accuracy)

# Analyzing feature importance
coefficients = logreg.coef_[0]
feature_names = X.columns
feature_importance = pd.DataFrame({'Feature': feature_names, 'Importance': coefficients})
feature_importance = feature_importance.sort_values(by='Importance', ascending=False)
print("Feature Importance:")
print(feature_importance)

# Fairness design pattern: Checking fairness across gender
female_indices = X_test[X_test['Sex'] == 1].index
male_indices = X_test[X_test['Sex'] == 0].index
female_accuracy = accuracy_score(y_test.loc[female_indices], y_pred[female_indices])
male_accuracy = accuracy_score(y_test.loc[male_indices], y_pred[male_indices])
print("Accuracy for females:", female_accuracy)
print("Accuracy for males:", male_accuracy)

# Heuristic benchmark design pattern: Using majority class as benchmark
majority_class_accuracy = accuracy_score(y_test, np.zeros_like(y_test))
print("Accuracy using majority class (benchmark):", majority_class_accuracy)

# Visualizing explanations using SHAP
explainer = shap.Explainer(logreg, X_train)
shap_values = explainer(X_test)
shap.summary_plot(shap_values, X_test, plot_type="bar")
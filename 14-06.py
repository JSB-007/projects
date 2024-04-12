# Fairness design pattern: Checking fairness across gender
female_indices = X_test[X_test['Sex'] == 1].index
male_indices = X_test[X_test['Sex'] == 0].index

# Filtering predictions for females and males
female_predictions = y_pred[X_test.index.intersection(female_indices)]
male_predictions = y_pred[X_test.index.intersection(male_indices)]

# Calculate accuracy for females and males if predictions are available
female_accuracy = accuracy_score(y_test.loc[female_indices.intersection(X_test.index)], female_predictions) if len(female_predictions) > 0 else 0.0
male_accuracy = accuracy_score(y_test.loc[male_indices.intersection(X_test.index)], male_predictions) if len(male_predictions) > 0 else 0.0

print("Accuracy for females:", female_accuracy)
print("Accuracy for males:", male_accuracy)
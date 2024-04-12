# Fairness design pattern: Checking fairness across gender
female_indices = X_test[X_test['Sex'] == 1].index
male_indices = X_test[X_test['Sex'] == 0].index
female_predictions = y_pred[female_indices]
male_predictions = y_pred[male_indices]

female_accuracy = accuracy_score(y_test.loc[female_indices], female_predictions) if len(female_predictions) > 0 else 0.0
male_accuracy = accuracy_score(y_test.loc[male_indices], male_predictions) if len(male_predictions) > 0 else 0.0

print("Accuracy for females:", female_accuracy)
print("Accuracy for males:", male_accuracy)
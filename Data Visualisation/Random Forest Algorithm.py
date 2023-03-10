import numpy as np
import pandas as pd  # for dataframes
import matplotlib.pyplot as plt  # for plotting graphs
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV  # import 'train_test_split'

# ACCESSING THE DATA
file = "/Users/tomcheung/Python/Data analysis/Metadata-Table 1.csv"
data = pd.read_csv(file)
data_copy = data.copy()

# REMOVE TARGET AND REDUNDANT FEATURE. (NO REDUNDANT FEATURES PRESENT IN DATA SET AS DATA HAS BEEN UPDATED)
target = data_copy['Left'].copy()
data_copy.drop(['Left'], axis=1, inplace=True)

# STRATIFY = TARGET TO SOLVE CLASS IMBALANCE. THIS WILL MAINTAIN SAME RATIO WHEN SPLITTING DATA
X_train, X_test, y_train, y_test = train_test_split(data_copy,
                                                    target,
                                                    test_size=0.25,
                                                    random_state=7,
                                                    stratify=target)

print(f"Number transactions X_train dataset: {X_train.shape}")
print(f"Number transactions y_train dataset: {y_train.shape}")
print(f"Number transactions X_test dataset: {X_test.shape}")
print(f"Number transactions y_test dataset: {y_test.shape}")

# RANDOM FOREST CLASSIFIER - used to solve for regression or classification problems. The random forest algorithm is
# made up of a collection of decision trees, and each tree in the ensemble is comprised of a data sample drawn from a
# training set with replacement, called the bootstrap sample.

rf_classifier = RandomForestClassifier(class_weight="balanced",
                                       random_state=7)
param_grid = {'n_estimators': [50, 75, 100, 125, 150, 175],
              'min_samples_split': [2, 4, 6, 8, 10],
              'min_samples_leaf': [1, 2, 3, 4],
              'max_depth': [5, 10, 15, 20, 25]}

grid_obj = GridSearchCV(rf_classifier,
                        return_train_score=True,
                        param_grid=param_grid,
                        scoring='roc_auc',
                        cv=10)

grid_fit = grid_obj.fit(X_train, y_train)
rf_opt = grid_fit.best_estimator_

print('=' * 20)
print("best params: " + str(grid_obj.best_estimator_))
print("best params: " + str(grid_obj.best_params_))
print('best score:', grid_obj.best_score_)
print('=' * 20)

# PLOT VARIABLES BASED ON RANDOM FOREST ANALYSIS
importances = rf_opt.feature_importances_
indices = np.argsort(importances)[::-1]  # Sort variable importance in descending order
names = [X_train.columns[i] for i in indices]  # Rearrange variables names so they match it's score of importance
plt.figure(figsize=(15, 7))  # Create graph
plt.title("Random Forrest - Variable importance")
plt.bar(range(X_train.shape[1]), importances[indices])  # Add bars
plt.xticks(range(X_train.shape[1]), names, rotation=90)  # Add feature names as x-axis labels
# plt.show()

# TABLE OF RESULTS
data_param_coeff = pd.DataFrame(columns=['Variable', 'Coefficient'])
for i in range(16):
    feat = X_train.columns[i]
    coeff = importances[i]
    data_param_coeff.loc[i] = (feat, coeff)
data_param_coeff.sort_values(by='Coefficient', ascending=False, inplace=True)
data_param_coeff = data_param_coeff.reset_index(drop=True)
data_param_coeff.head(10)


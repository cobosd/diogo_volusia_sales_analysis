# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 16:19:02 2021

@author: rossd
"""
import os
import pandas as pd
import numpy as np
import researchpy as rp

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import scikitplot as splt

import seaborn as sns
from sklearn.metrics import accuracy_score, roc_curve, auc
import matplotlib.pyplot as plt

from sklearn.inspection import permutation_importance

this_path = os.path.dirname(__file__)

full_path = this_path + '\\volusia_dataframe.csv'
df = pd.read_csv(full_path)
df = df[df.nbr_crimes != 0]
df.loc[df['nbr_crimes'] < 300, 'crime_rate'] = 'HIGH'
df.loc[df['nbr_crimes'] < 19, 'crime_rate'] = 'LOW'

df.head()
df.info()
df.describe()
corr = df.corr()
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 16}
plt.rc('font', **font)

ax = sns.heatmap(corr, vmin=-1, vmax=1, center=0,
                  cmap=sns.diverging_palette(20, 150, n=100), square=True)

ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right');

print(rp.summary_cat(df[["crime_rate"]]))

X = df.iloc[:,19:-3]
print(X.columns)
# Class
y = df.iloc[:,-3] 
print(X.columns)
 
# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=5)

# Gaussian Naive Bayes Model
model = GaussianNB()
model.fit(X_train, y_train)

NB_prob = model.predict_proba(X_test)
NB_prob = NB_prob[:, 1]
print(NB_prob)

y_train_predictions = model.predict(X_train)

y_test_predictions = model.predict(X_test)

y_score = model.fit(X_train, y_train).predict_proba(X_test)
y_score = y_score[:,1]

false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_score, pos_label='LOW')
roc_auc = auc(false_positive_rate, true_positive_rate)
print('AUC {}'.format(roc_auc))

plt.title('ROC')
plt.plot(false_positive_rate, true_positive_rate)
plt.style.use('default')
plt.legend(loc='lower right', prop={'size':8})
plt.plot([0,1],[0,1], color='lightgrey', linestyle='--')
plt.xlim([-0.05,1.0])
plt.ylim([0.0,1.0])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')

# Feature Importance
imps = permutation_importance(model, X_test, y_test)
importances = imps.importances_mean
features = X_test.columns
std = imps.importances_std
indices = np.argsort(importances)[::-1]
# Print the feature ranking
print("\nFeature ranking:")
for f in range(X_test.shape[1]):
    print("%d. %s (%f)" % (f + 1, features[indices[f]], importances[indices[f]]))
    
plt.figure(figsize=(10, 7))
plt.title("Feature importances")
plt.bar(range(X_test.shape[1]), importances[indices], color="b", yerr=std[indices], align="center")
plt.xticks(range(X_test.shape[1]), [features[indices[i]] for i in range(X_test.shape[1])])
plt.xlim([-1, X_test.shape[1]])
plt.show()
# Predict training data
predict_train = model.fit(X_train, y_train).predict(X_train)

# Accuracy score
# Training accuracy
accuracy_train = accuracy_score(y_train, predict_train)
print('\nModel accuracy_score on train dataset : ', accuracy_train)

# P the target on the test dataset
predict_test = model.predict(X_test)
# Accuracy Score on test dataset
accuracy_test = accuracy_score(y_test, predict_test)
print('\nModel accuracy score on test dataset : ', accuracy_test)

# Metrics Classification
print('\nMetrics Classification Report:\n', metrics.classification_report(y_test, predict_test))

# Confusion Matrix
splt.metrics.plot_confusion_matrix(y_test, predict_test)
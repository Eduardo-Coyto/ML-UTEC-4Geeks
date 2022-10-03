## Import libraries

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import OrdinalEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn import metrics
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline  

## Read dataset
url = 'https://raw.githubusercontent.com/4GeeksAcademy/linear-regression-project-tutorial/main/medical_insurance_cost.csv'
df = pd.read_csv(url)

## Transform the categorical features into dummies
# If a feature has n categoriess, it will be transformed into n-1 dummies
df = pd.get_dummies(df, drop_first=True)

## Separate data in features and target
X = df.drop('charges', axis=1)
y = df['charges']

## Separate data in train-test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=15)


## Model the data

#1# 
# Linear regression with intercept - baseline

model1 = LinearRegression()

# fit linear regression to train data
model1.fit(X_train, y_train)

# Prediction for test dataset
y_pred1 = model1.predict(X_test)


#2# 
# Linear regression without intercept

model2 = LinearRegression(fit_intercept=False)

# fit linear regression
model2.fit(X_train, y_train)

# predict
y_pred2 = model2.predict(X_test)


#3# 
# Hyperparameters tuning with grid search and cross-validation

def PolynomialRegression(degree=2, **kwargs):
    return make_pipeline(PolynomialFeatures(degree),
                         LinearRegression(**kwargs))

param_grid = {'polynomialfeatures__degree': np.arange(4), # polynomial up to 4
              'linearregression__fit_intercept': [True, False], # with and without intercept
              'linearregression__normalize': [True, False]} # normalize and not normalize

grid = GridSearchCV(PolynomialRegression(), param_grid) # 5 folds

grid.fit(X_train, y_train)

print('Best parameters:', grid.best_params_)

model3 = grid.best_estimator_

# fit model with the hiperaparameters selected by CV
y_pred3 = model3.fit(X_train, y_train).predict(X_test)


## Performance metrics for the three models

print('MAE - regression with intercept', metrics.mean_absolute_error(y_test, y_pred1))
print('MSE - regression with intercept', metrics.mean_squared_error(y_test, y_pred1))
print('RMSE- regression with intercept', metrics.mean_squared_error(y_test, y_pred1,squared=False))
print('---------------------------------------------------------------------')
print('MAE - regression without intercept', metrics.mean_absolute_error(y_test, y_pred2))
print('MSE - regression without intercept', metrics.mean_squared_error(y_test, y_pred2))
print('RMSE - regression without intercept', metrics.mean_squared_error(y_test, y_pred2,squared=False))
print('---------------------------------------------------------------------')
print('MAE - best hyperparameters', metrics.mean_absolute_error(y_test, y_pred3))
print('MSE - best hyperparameters', metrics.mean_squared_error(y_test, y_pred3))
print('RMSE - best hyperparameters', metrics.mean_squared_error(y_test, y_pred3,squared=False))
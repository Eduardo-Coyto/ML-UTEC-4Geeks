import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import classification_report

import pickle

df_raw = pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/random-forest-project-tutorial/main/titanic_train.csv',index_col=0)

df_raw = df_raw.drop(columns='Cabin', axis=1)

df_raw['Age'] = df_raw['Age'].fillna(df_raw['Age'].mean())
df_raw['Embarked'] = df_raw['Embarked'].fillna(df_raw['Embarked'].mode()[0])

df = df_raw.copy()

X = df.drop(columns=['Ticket', 'Name', 'Survived'])
y= df['Survived']

X [['Sex', 'Embarked']] = X [['Sex', 'Embarked']].astype('category')

X['Sex'] = X['Sex'].cat.codes

X['Embarked'] = X['Embarked'].cat.codes

X_train, X_test, y_train, y_test = train_test_split (X, y, random_state=1107)

classifer = RandomForestClassifier()

classifer.fit(X_train, y_train)

y_pred = classifer.predict(X_test)

from sklearn.model_selection import RandomizedSearchCV
# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]

# Number of features to consider at every split
max_features = ['auto', 'sqrt'] # común es auto, sqrt le hace al valor que le pase

# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)

# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]

# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]

# Method of selecting samples for training each tree
bootstrap = [True, False]

# Criterio
criterion = ['gini', 'entropy']

# Create the random grid
random_grid = {'n_estimators': n_estimators,
               #'max_features': max_features, #son pocas variables
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap,
               'criterion': criterion}

print(random_grid)

classifer_grid = RandomForestClassifier(random_state=1107)
classifer_grid_random = RandomizedSearchCV (estimator=classifer_grid, n_iter=100, cv=5, random_state=1107, param_distributions= random_grid)

classifer_grid_random.fit(X_train, y_train)

classifer_with_grid = RandomForestClassifier(n_estimators= 400, min_samples_split= 10, min_samples_leaf = 2, max_depth = 90, criterion= 'entropy', bootstrap= True)

classifer_with_grid.fit(X_train, y_train)

y_pred_with_grid = classifer_with_grid.predict(X_test)

filename = '/workspace/Random-Forest-Clase/models/finalized_model.sav' 
pickle.dump(classifer_with_grid, open(filename, 'wb'))
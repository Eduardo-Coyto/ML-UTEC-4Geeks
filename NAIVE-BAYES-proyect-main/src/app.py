import pandas as pd 
import numpy as np
import unicodedata
import re

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import precision_recall_fscore_support
from sklearn import metrics
from sklearn.pipeline import Pipeline
import pickle

df_raw = pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/naive-bayes-project-tutorial/main/playstore_reviews_dataset.csv')

df_raw['review'] = df_raw['review'].str.strip().str.lower()
df_raw['review'] = df_raw['review'].str.replace('!', '')
df_raw['review'] = df_raw['review'].str.replace(',', '')
df_raw['review'] = df_raw['review'].str.replace('&', '')
df_raw['review'] = df_raw['review'].str.normalize('NFKC') #toma el texto no latino y lo trata de arreglar
df_raw['review'] = df_raw['review'].str.replace(r'([a-zA-Z])\1{2,}', r'\1', regex=True) # REGEX detecta palabras que empiezan con Mayus o minisculas con letras repetidas tipo goooood se queda con good. Comprime el texto de una palabra grande tipo looooveeeee a love

def normalize_string (text_string):
    if text_string is not None:
        result = unicodedata.normalize('NFD', text_string).encode('ascii', 'ignore').decode()
    else:
        result = None

    return (result)

df_raw['review'] = df_raw['review'].apply(normalize_string)
df = df_raw.copy()

X = df['review']
y = df['polarity']

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=2007,stratify=y)

modelo_1 = Pipeline([('cont_vect', CountVectorizer()), ('clf', MultinomialNB())])
modelo_1.fit(X_train, y_train)
pred_1 = modelo_1.predict(X_test)

modelo_2 = Pipeline([('tfidf_vect', TfidfVectorizer()), ('clf', MultinomialNB())])
modelo_2.fit(X_train, y_train)
pred_2 = modelo_2.predict(X_test)

modelo_3 = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB())])
modelo_3.fit(X_train, y_train)
pred_3 = modelo_3.predict(X_test)

print('Naive Bayes Train Accuracy = ',metrics.accuracy_score(y_train,modelo_1.predict(X_train)))
print('Naive Bayes Test Accuracy = ',metrics.accuracy_score(y_test,modelo_1.predict(X_test)))

print('Naive Bayes Train Accuracy = ',metrics.accuracy_score(y_train,modelo_2.predict(X_train)))
print('Naive Bayes Test Accuracy = ',metrics.accuracy_score(y_test,modelo_2.predict(X_test)))

print('Naive Bayes Train Accuracy = ',metrics.accuracy_score(y_train,modelo_3.predict(X_train)))
print('Naive Bayes Test Accuracy = ',metrics.accuracy_score(y_test,modelo_3.predict(X_test)))

n_iter_search = 5
parameters = {'cont_vect__ngram_range': [(1, 1), (1, 2)], 'clf__alpha': (1e-2, 1e-3)}
RS_CV_1 = RandomizedSearchCV(modelo_1, parameters, n_iter = n_iter_search)
RS_CV_1.fit(X_train, y_train)
pred_1_grid = RS_CV_1.predict(X_test)

RS_CV_1.best_params_

n_iter_search = 5
parameters = {'clf__alpha': (1e-2, 1e-3)}
RS_CV_2 = RandomizedSearchCV(modelo_2, parameters, n_iter = n_iter_search)
RS_CV_2.fit(X_train, y_train)
pred_2_grid = RS_CV_2.predict(X_test)

RS_CV_2.best_params_

n_iter_search = 5
parameters = {'vect__ngram_range': [(1, 1), (1, 2)], 'tfidf__use_idf': (True, False), 'clf__alpha': (1e-2, 1e-3)}
RS_CV_3 = RandomizedSearchCV(modelo_3, parameters, n_iter = n_iter_search)
RS_CV_3.fit(X_train, y_train)
pred_3_grid = RS_CV_3.predict(X_test)

RS_CV_3.best_params_

print('RS_CV_1 = ',metrics.accuracy_score(y_test,RS_CV_1.predict(X_test)))
print('RS_CV_2 = ',metrics.accuracy_score(y_test,RS_CV_2.predict(X_test)))
print('RS_CV_3 = ',metrics.accuracy_score(y_test,RS_CV_3.predict(X_test)))

best_model = RS_CV_1.best_estimator_

pickle.dump(best_model, open('../models/best_model.pickle', 'wb')) # save the model
# modelo = pickle.load(open('../models/best_model.pickle', 'rb')) # read the model in the future
# modelo.predict(X_test) # use it to predict with new data
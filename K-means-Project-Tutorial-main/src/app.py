import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

from sklearn import decomposition
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

url='https://raw.githubusercontent.com/4GeeksAcademy/k-means-project-tutorial/main/housing.csv'
df_raw = pd.read_csv(url)

df_raw = df_raw[['Latitude', 'Longitude', 'MedInc']]

df = df_raw.copy()

scaler = StandardScaler()
df_scale = scaler.fit_transform(df)
df_scale

Sum_of_squared_distances = []
K = range(1,15)
for k in K:
    k_means = KMeans(n_clusters=k)
    k_means = k_means.fit(df_scale)
    Sum_of_squared_distances.append(k_means.inertia_)

rango_n_clusters = [2, 3, 4, 5, 6, 7, 8,9,10]
silhouette_avg = []
for num_clusters in rango_n_clusters:
# fit Kmeans
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(df_scale)
    cluster_labels = kmeans.labels_
# calcular silhouette
    silhouette_avg.append(silhouette_score(df_scale, cluster_labels))

kmeans = KMeans(init="random",n_clusters=2, random_state=0, n_init=10,max_iter=300)

kmeans.fit(df_scale)

df_2 = scaler.inverse_transform(df_scale)

df_2=pd.DataFrame(df_2,columns=['Latitude','Longitude','MedInc'])

df_2['Cluster'] = kmeans.labels_

df_2['Cluster'] = pd.Categorical(df_2.Cluster)

pickle.dump(kmeans, open('../models/kmeans.pickle', 'wb')) # save the model
# modelo = pickle.load(open('../models/kmeans.pickle', 'rb')) # read the model in the future
# modelo.predict(X_test) # use it to predict with new data

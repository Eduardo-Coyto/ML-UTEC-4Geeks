import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import folium
from folium.plugins import MarkerCluster
from folium import plugins
from folium.plugins import FastMarkerCluster
from folium.plugins import HeatMap

df= pd.read_csv('../data/raw/AB_NYC_2019.csv')

df.hist(figsize=(10,5))
plt.show()

df=df.astype({'name':'str','host_name':'str','neighbourhood_group':'category','neighbourhood':'category','room_type':'category'})
df['last_review'] = pd.to_datetime(df['last_review'], format="%Y/%m/%d")
df.dtypes

print ('Tipo de alojamientos')
df['room_type'].value_counts(normalize=True)

plt.figure(figsize=(12,8))
sns.scatterplot(x=df.longitude,y=df.latitude,hue=df.neighbourhood_group)
plt.show()

Long=-73.80
Lat=40.80
locations = list(zip(df.latitude, df.longitude))

map1 = folium.Map(location=[Lat,Long], zoom_start=7)
FastMarkerCluster(data=locations).add_to(map1)
map1

df['host_id'].value_counts(sort=True)[:10]

df.groupby('host_id')[['number_of_reviews','id']].agg({'id':pd.Series.nunique, 'number_of_reviews':sum}).sort_values(by='id', ascending=False)df.groupby('host_id')[['number_of_reviews','id']].agg({'id':pd.Series.nunique, 'number_of_reviews':sum}).sort_values(by='id', ascending=False)

## Is there any noticeable difference of traffic among different areas and what could be the reason for it?

round(df.groupby('host_id')[['number_of_reviews','id', 'price']].agg({'id':pd.Series.nunique, 'number_of_reviews':['sum', 'mean'], 'price': 'mean'}).sort_values(by=('id','nunique'), ascending=False))[0:10]
df_hn = df.groupby(['host_id','neighbourhood_group'])[['number_of_reviews','id']].agg({'id':pd.Series.nunique, 'number_of_reviews':['sum', 'mean']}).sort_values(by=('id','nunique'), ascending=False)[0:10]
list(df_hn.reset_index()['host_id'])

df_hn_filt = df[df['host_id'].isin(list(df_hn.reset_index()['host_id']))]
df_hn_filt

pd.set_option('display.max_rows', 110)
round(df_hn_filt.groupby(['host_id','neighbourhood_group','neighbourhood'])[['number_of_reviews','id','price']].agg({'id':pd.Series.nunique, 'number_of_reviews':['sum', 'mean'],'price': 'mean'}).sort_values(by=['host_id', ('id','nunique')], ascending=False).dropna())
df.groupby(['host_id','neighbourhood_group','neighbourhood'])[['number_of_reviews','id']].agg({'id':pd.Series.nunique, 'number_of_reviews':['sum', 'mean']}).sort_values(by=['host_id', ('id','nunique')], ascending=False).dropna()

## What can we learn about different hosts and areas?

df[['neighbourhood_group','neighbourhood']].value_counts(sort=True)
df_nei = round(df.groupby(['neighbourhood_group','neighbourhood']).agg({'price': 'mean'})).sort_values(by=['neighbourhood_group','price'], ascending=False).dropna()
df_nei.reset_index(inplace=True)
list(df_nei.neighbourhood_group.unique())

for barrio in list(df_nei.neighbourhood_group.unique()):
    display(df_nei[df_nei['neighbourhood_group'] == barrio].head(5))
    #display(df_nei[df_nei['neighbourhood_group'] == barrio].tail(5))

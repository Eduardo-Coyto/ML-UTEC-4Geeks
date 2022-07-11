# your app code here
import sqlite3
import requests

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
pag = requests.get(url)

print(pag) # si responde 200 está ok

pag_texto = pag.text
pag_texto

from bs4 import BeautifulSoup

text_beaut = BeautifulSoup(pag_texto, "html.parser")
text_beaut

tablas = text_beaut.findAll("table")
print(len(tablas))

id_tabla_quarter = None

for i in range(len(tablas)):
    if "Tesla Quarterly Revenue" in str(tablas[i]):
        id_tabla_quarter = i
        print("La tabla es la número", id_tabla_quarter)
        break

tabla_quarter = tablas[1]
tabla_quarter_body = tabla_quarter.tbody
lista_tr = tabla_quarter_body.find_all("tr") # el objeto fin_all devuelve una lista

for tr in lista_tr:
    date= tr.find_all("td")
    print("*"*10)
    print(len(date), date)
    print(date[0].text, date[1].text)

revenue_ls = []

from tqdm.auto import tqdm # libreria que me permite saber en que elemento está dentro de todo el ciclo for y cuál es su tiempo. Además carga la barra de forma iterativa

for tr in tqdm(lista_tr):
    all_tr = tr.find_all("td")
    date = all_tr[0].text
    revenue = all_tr[1].text 
    revenue_ls.append([date,revenue])
print(revenue_ls)

import pandas as pd

revenue_df = pd.DataFrame(revenue_ls, columns=["Date", "Revenue"])
revenue_df.head()

elemento = revenue_df["Revenue"][0]
elemento = elemento.replace("$","")
elemento = elemento.replace(",","")
elemento

import numpy as np

def preproc_revenue(texto):
    texto = texto.replace("$","")
    texto = texto.replace(",","")
    if texto == "":
        return np.nan
    return float(texto)

revenue_df["Revenue"]=revenue_df["Revenue"].apply(preproc_revenue) # aplico la función a mi columna que le hago el cambio

revenue_df = revenue_df.dropna(subset="Revenue") # borro nan de la columna Revenue

revenue_df.to_csv("revenue_df.csv", index=None) # Guardo dataset con nombre revenue_df.csv

connection = sqlite3.Connection("Tesla.db")

c = connection.cursor()

c.execute('''CREATE TABLE revenue
         (Date, Revenue)''')        # Creo tabla

records = revenue_df.to_records(index=False)
list_of_tuples = list(records)

c.executemany('INSERT INTO revenue (Date, Revenue) values (2022-06-16,5000)', list_of_tuples) # Inserto valores

connection.commit() # Guardo (commit) los cambios
connection.close()

import pickle
import pandas as pd 
import numpy as np 

country = 'Colombia'
variety = 'Caturra'
aroma = 7.83
aftertaste = 7.67
acidity = 7.33
body = 7.67
balance = 7.67
moisture = 0.11

cols = ['country_of_origin', 'variety', 'aroma', 'aftertaste', 'acidity', 'body', 'balance', 'moisture']
data = [country, variety, aroma, aftertaste, acidity, body, balance, moisture]
posted = pd.DataFrame(np.array(data).reshape(1,8), columns= cols)

loaded_model = pickle.load(open('../models/coffee_model.pkl', 'rb'))
result = loaded_model.predict(posted)
text_result = result.tolist()[0]
print(text_result)
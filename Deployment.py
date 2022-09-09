import pandas as pd
import xgboost as xgb
import numpy as np
from sklearn.preprocessing import  LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_percentage_error
import pickle
import streamlit as st

features = st.container()

df1 = pd.read_csv('Processed_data.csv')
df1.drop(columns='Unnamed: 0',inplace=True)

x = df1.drop(columns=['Price','Model'])

#%%
le = LabelEncoder()
x1 = le.fit_transform(x.Brand.values)
x2 = le.fit_transform(x['Operating System'].values)
x.Brand = x1

y = df1.Price
#%%
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

filename = 'Xgboost.sav'

model = pickle.load(open(filename, 'rb'))


with features:
    brand = st.selectbox(
        'Select Brand:',
        ('Apple', 'Samsung', 'Huawei', 'Mi', 'Oppo', 'Realme', 'Reeder', 'TCL', 'GM'))

    CPU = st.selectbox(
        'Select CPU -Ghz-:',
        (1.8, 2.3, 2.5, 2.8, 3.2))

    RAM = st.selectbox(
        'Select RAM -GB-:',
        (2, 4, 6, 8))

    Storage = st.selectbox(
        'Select Storage - GB-:',
        (32,64,128,256))

    Resolution = st.selectbox(
        'Select Camera Resolution -MP-:',
        (8,12,20,40,60))

    Size = st.selectbox(
        'Select Screen Size -Inch-:',
        (4.25, 5.25, 6, 6.5, 10))

if brand == 'Apple':
    OS = 1
else:
    OS = 0

feat= np.array([brand,CPU,RAM,Storage,OS,Resolution,Size])

if st.button('Calculate'):
    pricex = model.predict(feat)
    st.write('The estimated price of the device is:', pricex)



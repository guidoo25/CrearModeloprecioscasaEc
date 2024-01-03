# -*- coding: utf-8 -*-
"""entrenamiento2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13pXXRlKDuaxJYla1euV2bMSU4A1q_2qT
"""

import numpy as np
import pandas as pd

from sklearn.linear_model import Ridge

from sklearn.metrics import mean_squared_error , mean_absolute_error
from sklearn.model_selection import cross_val_score, cross_val_predict , KFold,GridSearchCV

from sklearn.pipeline import Pipeline
from sklearn.compose import TransformedTargetRegressor

from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler, OneHotEncoder

import joblib
import matplotlib.pyplot as plt

df_casas = pd.read_csv('limpio.csv')

df_casas.head()

x,y = df_casas.drop(['precio','ventaoalquiler','ciudad_casa','ubicacion','unidadterreno'], axis=1), df_casas['precio']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, random_state=42)



from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder

categorias = ['zona','descripespecif']
numerical_features = ['habitaciones','banos','area','parqueaderos','estrato','tiempodeconstruido','latitud','longitud']

preprocessor = make_column_transformer(
    (OneHotEncoder(drop='if_binary', handle_unknown='ignore'), categorias),
    remainder='passthrough',
    verbose_feature_names_out=False)

model = make_pipeline(
    preprocessor,
    TransformedTargetRegressor(
        regressor=Ridge(alpha=0.1),
        func=np.log10,
        inverse_func=sp.special.exp10
    )
)

# Luego ajustas y transformas tus datos de entrenamiento
model.fit(x_train, y_train)

# Y transformas tus datos de prueba (no ajustas)
y_pred_test = model.predict(x_test)

from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge
from sklearn.compose import TransformedTargetRegressor
import scipy as sp

model = make_pipeline(
    preprocessor,
    TransformedTargetRegressor(
        regressor=Ridge(alpha=0.1),
        func=np.log10,
        inverse_func=sp.special.exp10
    )
)

model.fit(x_train, y_train)

y_pred_train = model.predict(x_train)
mae_train = mean_absolute_error(y_train, y_pred_train)
print(f"MAE en train: {mae_train:.2f}")

# Predecir en los datos de prueba y calcular el error absoluto medio
y_pred_test = model.predict(x_test)
mae_test = mean_absolute_error(y_test, y_pred_test)
print(f"MAE en test: {mae_test:.2f}")

# Asegúrate de que estás haciendo predicciones para todos los elementos de y_test
y_pred = model.predict(x_test)

# Ahora y_test y y_pred deberían tener la misma longitud
print(len(y_test), len(y_pred))

# Ahora deberías poder hacer el gráfico de dispersión sin problemas
fig, ax = plt.subplots(figsize=(8, 8))
plt.scatter(y_test, y_pred)
ax.plot([0, 1], [0, 1], transform=ax.transAxes, ls="--", c="red")
plt.text(500000000, 1000000000, string_score)
plt.title('Ridge')
plt.ylabel('Predicciones')
plt.xlabel('Valores reales')
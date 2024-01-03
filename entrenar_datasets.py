import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer

# Cargar el dataset
df = pd.read_csv('ruta_al_archivo.csv')
calidad_zonas = {
    'zona1': 1,  # 1 representa la peor calidad
    'zona2': 2,
    'zona3': 3,
    'zona4': 4,
    'zona5': 5   # 5 representa la mejor calidad
}
df['calidad_zona'] = df['zona'].map(calidad_zonas)

# Preprocesar los datos
imputer = SimpleImputer(strategy='mean')
ohe = OneHotEncoder()
preprocessor = make_column_transformer(
    (imputer, ['metrajeconstruc', 'metrajeterreno']),  # Agregamos 'metrajeterreno' aquí
    (ohe, ['zona','ciudad']),
    remainder='passthrough'
)

# Dividir los datos en conjuntos de entrenamiento y prueba
X = df[['zona', 'metrajeconstruc', 'metrajeterreno','calidad_zonas']]  
y = df['precio']  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = make_pipeline(preprocessor, LinearRegression())
model.fit(X_train, y_train)

# Evaluar el modelo
score = model.score(X_test, y_test)
print(f'El score del modelo es: {score}')